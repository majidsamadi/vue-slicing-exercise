<!-- src/layouts/EditProfileLayout.vue -->
<template>
    <v-container fluid class="edit-profile-layout">
      <v-row>
        <!-- Steps Navigation -->
        <v-col cols="12" md="3">
          <v-list nav>
            <v-list-item
              v-for="step in steps"
              :key="step.to"
              :to="step.to"
              link
              exact
              class="edit-step"
              active-class="active-step"
            >
              <v-list-item-title>{{ step.label }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-col>
        <!-- Content Area -->
        <v-col cols="12" md="8" class="page-container">
          <router-view />
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue'
  import { getProfile } from '@/services/authService'
  
  const profile = ref(null)
  const maritalStatus = ref('')
  
  onMounted(async () => {
    try {
      const user = await getProfile()
      profile.value = user
      maritalStatus.value = user.additional?.maritalStatus || ''
    } catch {
      // auth guard covers
    }
  })
  
  const steps = computed(() => {
    const base = [
      { label: 'Basic', to: '/edit/basic' },
      { label: 'Additional', to: '/edit/additional' }
    ]
    if (maritalStatus.value === 'Married') {
      base.push({ label: 'Spouse', to: '/edit/spouse' })
    }
    base.push({ label: 'Preferences', to: '/edit/preferences' })
    return base
  })
  </script>
  
  <style scoped>
  .page-container {
    margin: -18px;
  }

  .edit-step {
    cursor: pointer;
  }
  .active-step {
    font-weight: bold;
    color: #42b983;
  }

   /* sidebar nav styling */
 .edit-profile-layout .v-list {
    background-color: #FFFFFF;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    padding: 1rem 0;
 }

  /* content column (md-9) styling */
 .edit-profile-layout .col-md-9 {
    background-color: #FFFFFF;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    padding: 1.5rem;
}
  </style>
  