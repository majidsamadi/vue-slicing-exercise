# backend/main.py
# Install dependencies:
#   pip install fastapi uvicorn pydantic

import json
import uuid
from fastapi import FastAPI, HTTPException, Depends, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
from typing import Dict, Optional, List, Any
from pathlib import Path
from datetime import datetime, timedelta, date

app = FastAPI()

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup data directory and files
data_dir = Path(__file__).parent / "data"
data_dir.mkdir(exist_ok=True)
users_file = data_dir / "users.json"
sessions_file = data_dir / "sessions.json"


def save_json(path: Path, data: Any):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def load_json(path: Path, default: Any):
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return default

# In-memory stores
users_db: Dict[str, Any] = load_json(users_file, {})
sessions: Dict[str, Any] = load_json(sessions_file, {})


# Models
class Additional(BaseModel):
    maritalStatus: Optional[str] = None
    dob: Optional[date] = None
    phone: Optional[str] = None
    homeAddress: Optional[str] = None
    country: Optional[str] = None
    postalCode: Optional[str] = None
    nationality: Optional[str] = None

    @validator('dob')
    def check_age(cls, v):
        if v:
            today = date.today()
            age = today.year - v.year - ((today.month, today.day) < (v.month, v.day))
            if age < 17:
                raise ValueError('User must be at least 17 years old')
        return v

class User(BaseModel):
    userID: str
    password: str
    email: Optional[str] = ""
    salutation: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    avatar: Optional[str] = None
    additional: Additional = Field(default_factory=Additional)
    spouse: Dict[str, Any] = Field(default_factory=dict)
    preferences: Dict[str, List[str]] = Field(default_factory=dict)

# Specific update models
class BasicUpdate(BaseModel):
    avatar: Optional[str] = None
    email: Optional[str] = None
    salutation: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None

class AdditionalUpdate(BaseModel):
    maritalStatus: Optional[str] = None
    dob: Optional[date] = None
    phone: Optional[str] = None
    homeAddress: Optional[str] = None
    country: Optional[str] = None
    postalCode: Optional[str] = None
    nationality: Optional[str] = None

    @validator('dob')
    def check_age(cls, v):
        if v:
            today = date.today()
            age = today.year - v.year - ((today.month, today.day) < (v.month, v.day))
            if age < 17:
                raise ValueError('User must be at least 17 years old')
        return v

class SpouseUpdate(BaseModel):
    spouse: Dict[str, Any]

class PreferencesUpdate(BaseModel):
    preferences: Dict[str, List[str]]

# Legacy unified update
class ProfileUpdate(BaseModel):
    avatar: Optional[str] = None
    email: Optional[str] = None
    salutation: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    additional: Optional[Additional] = None
    spouse: Optional[Dict[str, Any]] = None
    preferences: Optional[Dict[str, List[str]]] = None

# Login models
class UserLogin(BaseModel):
    userID: str
    password: str
    keepMeLoggedIn: bool = False

class TokenResponse(BaseModel):
    token: str

# Persistence helpers
def persist_users():
    save_json(users_file, users_db)

def persist_sessions():
    save_json(sessions_file, sessions)

# Auth dependency
def get_current_user(authorization: str = Header(...)) -> User:
    try:
        scheme, token = authorization.split()
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid auth header")
    if scheme.lower() != "bearer" or token not in sessions:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    session = sessions[token]
    expires_at = datetime.fromisoformat(session["expires_at"])
    if datetime.utcnow() > expires_at:
        del sessions[token]
        persist_sessions()
        raise HTTPException(status_code=401, detail="Token expired")
    user_data = users_db.get(session["userID"])
    if not user_data:
        raise HTTPException(status_code=401, detail="User not found")
    return User(**user_data)

# Routes
@app.post("/api/register", status_code=201)
async def register(payload: dict):
    userID = payload.get("userID")
    password = payload.get("password")
    email = payload.get("email", "")
    if not userID or not password:
        raise HTTPException(status_code=400, detail="userID and password required")
    if userID in users_db:
        raise HTTPException(status_code=400, detail="UserID already registered")
    users_db[userID] = {
        "userID": userID,
        "password": password,
        "email": email,
        "salutation": None,
        "firstName": None,
        "lastName": None,
        "avatar": None,
        "additional": {},
        "spouse": {},
        "preferences": {}
    }
    persist_users()
    return {"message": "User registered"}

@app.post("/api/login", response_model=TokenResponse)
async def login(form: UserLogin):
    stored = users_db.get(form.userID)
    if not stored or stored.get("password") != form.password:
        raise HTTPException(status_code=400, detail="Incorrect userID or password")
    token = str(uuid.uuid4())
    days_valid = 365 if form.keepMeLoggedIn else 1
    expires_at = (datetime.utcnow() + timedelta(days=days_valid)).isoformat()
    sessions[token] = {"userID": form.userID, "expires_at": expires_at}
    persist_sessions()
    return {"token": token}

@app.post("/api/logout")
async def logout_endpoint(current: User = Depends(get_current_user), authorization: str = Header(...)):
    _, token = authorization.split()
    sessions.pop(token, None)
    persist_sessions()
    return {"message": "Logged out"}

@app.get("/api/profile", response_model=User)
async def read_profile(current: User = Depends(get_current_user)):
    return current

# Unified update (optional)
@app.put("/api/profile", response_model=User)
async def update_profile(request: Request, update: ProfileUpdate, current: User = Depends(get_current_user)):
    raw = await request.json()
    print("[DEBUG] Raw JSON payload:", raw)
    data = update.dict(exclude_unset=True)
    # Merge additional if present
    if "additional" in data:
        add = data.pop("additional") or {}
        existing = current.additional.dict()
        existing.update({k: (v.isoformat() if isinstance(v, date) else v) for k, v in add.items()})
        data["additional"] = existing
    users_db[current.userID].update(data)
    persist_users()
    return User(**users_db[current.userID])

# New segmented update endpoints
@app.put("/api/profile/basic", response_model=User)
async def update_basic(update: BasicUpdate, current: User = Depends(get_current_user)):
    data = update.dict(exclude_unset=True)
    users_db[current.userID].update(data)
    persist_users()
    return User(**users_db[current.userID])

@app.put("/api/profile/additional", response_model=User)
async def update_additional(update: AdditionalUpdate, current: User = Depends(get_current_user)):
    data = update.dict(exclude_unset=True)
    existing = users_db[current.userID].get("additional", {})
    for k, v in data.items():
        existing[k] = v.isoformat() if isinstance(v, date) else v
    users_db[current.userID]["additional"] = existing
    persist_users()
    return User(**users_db[current.userID])

@app.put("/api/profile/spouse", response_model=User)
async def update_spouse(update: SpouseUpdate, current: User = Depends(get_current_user)):
    users_db[current.userID]["spouse"] = update.spouse
    persist_users()
    return User(**users_db[current.userID])

@app.put("/api/profile/preferences", response_model=User)
async def update_preferences(update: PreferencesUpdate, current: User = Depends(get_current_user)):
    users_db[current.userID]["preferences"] = update.preferences
    persist_users()
    return User(**users_db[current.userID])
