// src/main.js

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'

// ←– Make sure this matches the file you created:
import '@/styles/global.scss'

import { initAuth } from './services/authService'

// Initialize auth (loads any existing token)
initAuth()

// Create and mount the app
const app = createApp(App)

app.use(router)
app.use(vuetify)

app.mount('#app')
