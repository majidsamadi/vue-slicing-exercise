<template>
  <div class="login-container">
    <div class="auth-card">
      <img src="/assets/logo.png" alt="Logo" class="logo" />
      <h1 class="welcome-text">Welcome to <strong>myApp</strong></h1>
      <form @submit.prevent="onSubmit" novalidate>
        <div class="form-group">
          <label for="userID">User ID<span>*</span></label>
          <input
            id="userID"
            v-model="form.userID"
            @blur="validateField('userID')"
            :class="{'has-error': errors.userID}"
            required
          />
          <span v-if="errors.userID" class="error-message">{{ errors.userID }}</span>
        </div>

        <div class="form-group">
          <label for="password">Password<span>*</span></label>
          <div class="password-wrapper">
            <input
              id="password"
              :type="showPassword ? 'text' : 'password'"
              v-model="form.password"
              @blur="validateField('password')"
              :class="{'has-error': errors.password}"
              required
            />
            <span
              class="toggle-eye"
              @click="showPassword = !showPassword"
              :aria-label="showPassword ? 'Hide password' : 'Show password'"
            >
              {{ showPassword ? 'Hide' : 'Show' }}
            </span>
          </div>
          <span v-if="errors.password" class="error-message">{{ errors.password }}</span>
        </div>

        <div class="form-group checkbox-group">
          <input
            id="keepMeLoggedIn"
            type="checkbox"
            v-model="form.keepMeLoggedIn"
          />
          <label for="keepMeLoggedIn">Keep me logged in</label>
        </div>

        <div class="button-group">
          <button class="btn login-btn" :disabled="!isFormValid" type="submit">LOGIN</button>
          <button class="btn cancel-btn" type="button" @click="onCancel">Cancel</button>
        </div>

        <p v-if="error" class="global-error">{{ error }}</p>
        <p class="register-link">
          No account? <RouterLink to="/register">Register here.</RouterLink>
        </p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, computed } from 'vue'
import { useRouter, RouterLink } from 'vue-router'
import { login } from '@/services/authService'

const router = useRouter()
const form = reactive({ userID: '', password: '', keepMeLoggedIn: false })
const errors = reactive({ userID: '', password: '' })
const error = ref('')

// **Password toggle state**
const showPassword = ref(false)

function validateField(field) {
  errors[field] = ''
  if (!form[field]?.trim()) {
    errors[field] = field === 'userID' ? 'User ID is required.' : 'Password is required.'
  }
}

const isFormValid = computed(() => {
  return (
    form.userID.trim() !== '' &&
    form.password.trim() !== '' &&
    !errors.userID &&
    !errors.password
  )
})

async function onSubmit() {
  validateField('userID')
  validateField('password')
  if (!isFormValid.value) return
  error.value = ''
  try {
    await login({
      userID: form.userID,
      password: form.password,
      keepMeLoggedIn: form.keepMeLoggedIn
    })
    router.push('/dashboard')
  } catch {
    error.value = 'Your user ID and/or password does not match.'
  }
}

function onCancel() {
  router.push('/register')
}
</script>

<style scoped>
/* (styles unchanged from your original file) */
.login-container {
  min-height: 100vh;
  /* background: url('/assets/bg.jpg') center/cover no-repeat; */
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}

.auth-card {
  background: #ffffffcc;
  border-radius: 12px;
  padding: 2rem;
  width: 100%;
  max-width: 360px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.logo {
  width: 80px;
  margin-bottom: 1rem;
}

.welcome-text {
  font-size: 1.75rem;
  margin-bottom: 1.5rem;
}

.form-group {
  margin-bottom: 1.25rem;
  text-align: left;
}

.form-group label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 1rem;
  box-sizing: border-box;
}

input.has-error {
  border-color: #e74c3c;
}

.error-message {
  color: #e74c3c;
  font-size: 0.875rem;
  margin-top: 0.25rem;
  display: block;
}

.password-wrapper {
  position: relative;
}

.password-wrapper input {
  padding-right: 4rem;
}

.toggle-eye {
  position: absolute;
  top: 50%;
  right: 0.75rem;
  transform: translateY(-50%);
  cursor: pointer;
  font-size: 0.875rem;
  user-select: none;
  z-index: 2;
}

.checkbox-group {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.checkbox-group input {
  width: auto;
}

.button-group {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.btn {
  padding: 0.75rem;
  font-size: 1rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

.login-btn {
  background-color: #000;
  color: #fff;
  text-transform: uppercase;
}

.login-btn:disabled {
  background-color: #777;
  cursor: not-allowed;
}

.cancel-btn {
  background-color: #f0f0f0;
  color: #333;
}

.global-error {
  background: rgba(231, 76, 60, 0.9);
  color: #fff;
  padding: 0.75rem;
  border-radius: 6px;
  margin-top: 1rem;
}

.register-link {
  margin-top: 1rem;
  font-size: 0.875rem;
}

.register-link a {
  color: #000;
  text-decoration: underline;
}
</style>
