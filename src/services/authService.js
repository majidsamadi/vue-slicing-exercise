// src/services/authService.js
import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || ''
const TOKEN_KEY = 'app_token'

// Configure Axios Authorization header
function setAuthToken(token) {
  if (token) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
  } else {
    delete axios.defaults.headers.common['Authorization']
  }
}

// Initialize auth on app startup
export function initAuth() {
  const token = localStorage.getItem(TOKEN_KEY) || sessionStorage.getItem(TOKEN_KEY)
  if (token) {
    setAuthToken(token)
  }
}

// Registration
export async function register(user) {
  const resp = await axios.post(`${API_URL}/api/register`, user)
  return resp.data
}

// Login with "Keep Me Logged In" option
export async function login({ userID, password, keepMeLoggedIn }) {
  const resp = await axios.post(`${API_URL}/api/login`, { userID, password, keepMeLoggedIn })
  const token = resp.data.token
  if (keepMeLoggedIn) {
    localStorage.setItem(TOKEN_KEY, token)
  } else {
    sessionStorage.setItem(TOKEN_KEY, token)
  }
  setAuthToken(token)
  return token
}

// Logout: inform backend and clear token
export async function logout() {
  try {
    await axios.post(`${API_URL}/api/logout`)
  } catch (e) {
    // ignore backend logout errors
  }
  localStorage.removeItem(TOKEN_KEY)
  sessionStorage.removeItem(TOKEN_KEY)
  setAuthToken(null)
}

// Check login status
export function isLoggedIn() {
  return !!(localStorage.getItem(TOKEN_KEY) || sessionStorage.getItem(TOKEN_KEY))
}

// Fetch user profile
export async function getProfile() {
  const resp = await axios.get(`${API_URL}/api/profile`)
  return resp.data
}

// Update user profile
export async function updateProfile(data) {
  const resp = await axios.put(`${API_URL}/api/profile`, data)
  return resp.data
}
