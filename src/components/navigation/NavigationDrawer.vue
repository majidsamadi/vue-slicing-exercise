<!-- src/components/navigation/NavigationDrawer.vue -->
<template>
  <transition name="slide">
    <nav v-if="open" class="drawer">
      <ul>
        <li>
          <RouterLink to="/dashboard" @click.native="closeDrawer">
            <v-icon left small>mdi-home</v-icon>
            Home
          </RouterLink>
        </li>
        <li>
          <RouterLink to="/profile/basic" @click.native="closeDrawer">
            <v-icon left small>mdi-account</v-icon>
            My Profile
          </RouterLink>
        </li>
        <li>
          <RouterLink to="/edit/basic" @click.native="closeDrawer">
            <v-icon left small>mdi-pencil</v-icon>
            Edit Profile
          </RouterLink>
        </li>
        <li>
          <a @click.prevent="handleLogout">
            <v-icon left small>mdi-logout</v-icon>
            Logout
          </a>
        </li>
      </ul>
    </nav>
  </transition>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'
import { useRouter, RouterLink } from 'vue-router'
import { logout } from '@/services/authService'

const props = defineProps({ open: Boolean })
const emit = defineEmits(['update:open'])
const router = useRouter()

function closeDrawer() {
  emit('update:open', false)
}

async function handleLogout() {
  try { await logout() } catch {}
  closeDrawer()
  router.push('/login')
}
</script>

<style scoped>
.drawer {
  position: fixed;
  top: 0;
  right: 0;
  width: 260px;
  height: 100vh;
  background: white;
  box-shadow: -2px 0 8px rgba(0, 0, 0, 0.1);
  padding-top: 64px;

  /* NEW: keep the drawer above everything else */
  z-index: 1000;
}

.drawer ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.drawer li {
  margin: 0;
  padding: 0;
}

.drawer li a,
.drawer li RouterLink {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  text-decoration: none;
  color: #333;
  font-weight: bold;
  border-radius: 4px;
  transition: background-color 0.2s, color 0.2s;
}

.drawer li a:hover,
.drawer li RouterLink:hover {
  background-color: rgba(25, 118, 210, 0.1);
  color: #1976D2;
}

.drawer li v-icon {
  margin-right: 8px;
}

.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s ease;
}

.slide-enter-from,
.slide-leave-to {
  transform: translateX(100%);
}

.slide-enter-to,
.slide-leave-from {
  transform: translateX(0);
}
</style>
