// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '@/views/auth/LoginPage.vue'
import RegistrationPage from '@/views/auth/RegistrationPage.vue'
import DashboardLayout from '@/layouts/DashboardLayout.vue'
import Dashboard from '@/views/dashboard/Dashboard.vue'
import ProfileLayout from '@/layouts/ProfileLayout.vue'
import EditProfileLayout from '@/layouts/EditProfileLayout.vue'
import { isLoggedIn } from '@/services/authService'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: LoginPage },
  { path: '/register', component: RegistrationPage },
  {
    path: '/dashboard',
    component: DashboardLayout,
    meta: { requiresAuth: true },
    children: [
      { path: '', component: Dashboard }
    ]
  },
  {
    path: '/profile',
    component: ProfileLayout,
    meta: { requiresAuth: true },
    children: [
      { path: 'basic', component: () => import('@/views/profile/Basic.vue') },
      { path: 'additional', component: () => import('@/views/profile/Additional.vue') },
      { path: 'spouse', component: () => import('@/views/profile/Spouse.vue') },
      { path: 'preferences', component: () => import('@/views/profile/Preferences.vue') }
    ]
  },
  {
    path: '/edit',
    component: EditProfileLayout,
    meta: { requiresAuth: true },
    children: [
      { path: 'basic', component: () => import('@/views/edit/Basic.vue') },
      { path: 'additional', component: () => import('@/views/edit/Additional.vue') },
      { path: 'spouse', component: () => import('@/views/edit/Spouse.vue') },
      { path: 'preferences', component: () => import('@/views/edit/Preferences.vue') }
    ]
  },
  // fallback
  { path: '/:pathMatch(.*)*', redirect: '/dashboard' }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const authRequired = to.meta.requiresAuth
  if (authRequired && !isLoggedIn()) {
    next({ path: '/login' })
  } else if ((to.path === '/login' || to.path === '/register') && isLoggedIn()) {
    next({ path: '/dashboard' })
  } else {
    next()
  }
})

export default router
