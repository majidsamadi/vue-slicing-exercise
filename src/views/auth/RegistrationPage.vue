<template>
    <div class="login-container">
      <div class="auth-card">
        <img src="/assets/logo.png" alt="Logo" class="logo" />
        <h1 class="welcome-text">Register for <strong>myApp</strong></h1>
        <form @submit.prevent="onSubmit" novalidate>
          <div class="form-group">
            <label for="userID">User ID<span>*</span></label>
            <input
              id="userID"
              v-model="form.userID"
              @blur="validateField('userID')"
              :class="{ 'has-error': errors.userID }"
              required
            />
            <span v-if="errors.userID" class="error-message">{{ errors.userID }}</span>
          </div>
  
          <div class="form-group">
            <label for="password">Password<span>*</span></label>
            <input
              id="password"
              type="password"
              v-model="form.password"
              @blur="validateField('password')"
              :class="{ 'has-error': errors.password }"
              required
            />
            <span v-if="errors.password" class="error-message">{{ errors.password }}</span>
          </div>
  
          <div class="form-group">
            <label for="confirm">Confirm Password<span>*</span></label>
            <input
              id="confirm"
              type="password"
              v-model="form.confirm"
              @blur="validateField('confirm')"
              :class="{ 'has-error': errors.confirm }"
              required
            />
            <span v-if="errors.confirm" class="error-message">{{ errors.confirm }}</span>
          </div>
  
          <div class="button-group">
            <button class="btn login-btn" :disabled="!isFormValid" type="submit">REGISTER</button>
            <button class="btn cancel-btn" type="button" @click="onCancel">Cancel</button>
          </div>
  
          <p v-if="error" class="global-error">{{ error }}</p>
          <p class="register-link">
            Already have an account? <RouterLink to="/login">Login here.</RouterLink>
          </p>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { reactive, ref, computed } from 'vue'
  import { useRouter, RouterLink } from 'vue-router'
  import { register } from '@/services/authService'
  
  const router = useRouter()
  const form = reactive({ userID: '', password: '', confirm: '' })
  const errors = reactive({ userID: '', password: '', confirm: '' })
  const error = ref('')
  
  function validateField(field) {
    errors[field] = ''
    const value = form[field]?.trim()
    if (!value) {
      errors[field] = field === 'userID'
        ? 'User ID is required.'
        : field === 'password'
        ? 'Password is required.'
        : 'Please confirm your password.'
    }
    if (field === 'confirm' && form.confirm && form.confirm !== form.password) {
      errors.confirm = 'Passwords do not match.'
    }
  }
  
  const isFormValid = computed(() => {
    return (
      form.userID.trim() !== '' &&
      form.password !== '' &&
      form.confirm !== '' &&
      form.password === form.confirm &&
      !errors.userID &&
      !errors.password &&
      !errors.confirm
    )
  })
  
  async function onSubmit() {
    validateField('userID')
    validateField('password')
    validateField('confirm')
    if (!isFormValid.value) return
    error.value = ''
    try {
      await register({
        userID: form.userID,
        password: form.password
      })
      router.push('/login')
    } catch (e) {
      error.value = e.message
    }
  }
  
  function onCancel() {
    router.push('/login')
  }
  </script>
  
  <style scoped>
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
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
  }
  
  .form-group {
    margin-bottom: 1rem;
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
  
  .button-group {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin-top: 1rem;
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
  