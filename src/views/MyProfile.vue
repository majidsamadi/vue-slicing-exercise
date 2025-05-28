// src/views/MyProfile.vue
<template>
  <div class="profile-page" v-if="user">
    <header class="profile-header">
      <h1>My Profile</h1>
      <button class="edit-btn" @click="goToEdit">Edit Profile</button>
    </header>
    <div class="profile-layout">
      <aside class="tabs">
        <ul>
          <li :class="{ active: currentTab === 'Basic' }" @click="currentTab = 'Basic'">Basic Details</li>
          <li :class="{ active: currentTab === 'Additional' }" @click="currentTab = 'Additional'">Additional Details</li>
          <li v-if="hasSpouse" :class="{ active: currentTab === 'Spouse' }" @click="currentTab = 'Spouse'">Spouse Details</li>
          <li v-if="hasPreferences" :class="{ active: currentTab === 'Preferences' }" @click="currentTab = 'Preferences'">Personal Preferences</li>
        </ul>
      </aside>
      <section class="content">
        <div v-if="currentTab === 'Basic'">
          <img v-if="user.avatar" :src="user.avatar" alt="Avatar" class="avatar" />
          <p><strong>Salutation:</strong> {{ user.salutation }}</p>
          <p><strong>First Name:</strong> {{ user.firstName }}</p>
          <p><strong>Last Name:</strong> {{ user.lastName }}</p>
          <p><strong>User ID:</strong> {{ user.userID }}</p>
        </div>
        <div v-if="currentTab === 'Additional'">
          <p v-if="!hasAdditional">No additional details provided.</p>
          <div v-else>
            <p><strong>Date of Birth:</strong> {{ user.additional.dob }}</p>
            <p><strong>Phone:</strong> {{ user.additional.phone }}</p>
            <p><strong>Address:</strong> {{ user.additional.address }}</p>
            <p><strong>Nationality:</strong> {{ user.additional.nationality }}</p>
          </div>
        </div>
        <div v-if="currentTab === 'Spouse'">
          <p v-if="!hasSpouse">No spouse details provided.</p>
          <div v-else>
            <p><strong>First Name:</strong> {{ user.spouse.firstName }}</p>
            <p><strong>Last Name:</strong> {{ user.spouse.lastName }}</p>
            <p><strong>Date of Birth:</strong> {{ user.spouse.dob }}</p>
            <p><strong>Email:</strong> {{ user.spouse.email }}</p>
            <p><strong>Phone:</strong> {{ user.spouse.phone }}</p>
          </div>
        </div>
        <div v-if="currentTab === 'Preferences'">
          <p v-if="!hasPreferences">No personal preferences provided.</p>
          <ul v-else>
            <li v-for="(pref, i) in user.preferences" :key="i">
              <strong>{{ pref.preference }}:</strong> {{ pref.value }}
            </li>
          </ul>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getProfile } from '../services/authService'

const router = useRouter()
const user = ref(null)
const currentTab = ref('Basic')

const hasAdditional = computed(() => {
  const a = user.value?.additional || {}
  return Object.values(a).some(v => v)
})
const hasSpouse = computed(() => {
  const s = user.value?.spouse || {}
  return Object.values(s).some(v => v)
})
const hasPreferences = computed(() => {
  return Array.isArray(user.value?.preferences) && user.value.preferences.length > 0
})

async function load() {
  try {
    user.value = await getProfile()
  } catch {
    router.push('/login')
  }
}

function goToEdit() {
  router.push('/edit-profile')
}

onMounted(load)
</script>

<style scoped>
.profile-page {
  max-width: 800px;
  margin: 2rem auto;
  background: #fff;
  border-radius: 8px;
  padding: 1rem;
}
.profile-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}
.edit-btn {
  padding: 0.5rem 1rem;
  background: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
}
.profile-layout {
  display: flex;
}
.tabs ul {
  list-style: none;
  padding: 0;
}
.tabs li {
  padding: 0.5rem 1rem;
  cursor: pointer;
}
.tabs .active {
  font-weight: bold;
  border-left: 4px solid #42b983;
}
.content {
  flex: 1;
  padding: 0 1rem;
}
.avatar {
  max-width: 120px;
  border-radius: 50%;
  margin-bottom: 1rem;
}
</style>

