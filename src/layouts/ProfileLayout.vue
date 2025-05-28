<!-- src/layouts/ProfileLayout.vue -->
<template>
    <v-container fluid class="profile-layout pa-4">
      <v-row
        no-gutters
        align="start"
        class="profile-row"
      >
        <!-- Sidebar Navigation Card -->
        <v-col cols="12" md="3" class="pa-2">
          <v-card elevation="2" rounded class="h-100">
            <v-list nav dense>
              <v-list-item
                v-for="tab in tabs"
                :key="tab.to"
                :to="tab.to"
                link
                exact
                class="profile-tab"
                active-class="active-tab"
              >
                <v-list-item-title>{{ tab.label }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>
  
        <!-- Main Content Area: your pages render their own cards -->
        <v-col
          cols="12"
          md="8"
          class="pager-container"
        >
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
      // route guard handles unauthenticated
    }
  })
  
  const tabs = computed(() => {
    const base = [
      { label: 'Basic Details', to: '/profile/basic' },
      { label: 'Additional Details', to: '/profile/additional' }
    ]
    if (maritalStatus.value === 'Married') {
      base.push({ label: 'Spouse Details', to: '/profile/spouse' })
    }
    base.push({ label: 'Preferences', to: '/profile/preferences' })
    return base
  })
  </script>
  
  <style scoped>

  /* flex container with a 32px gap and top-aligned items */
  .profile-row {
    display: flex;

    align-items: flex-start;
  }

  .pager-container {
    margin: -10px;
  }
  
  /* highlight active tab */
  .profile-tab.active-tab {
    background-color: rgba(25, 118, 210, 0.1);
    color: var(--v-primary-base);
    border-radius: 4px;
  }
  </style>
  