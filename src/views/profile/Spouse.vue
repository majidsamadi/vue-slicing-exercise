<!-- src/views/profile/Spouse.vue -->
<template>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" md="8">
          <v-card elevation="2" class="pa-4">
            <v-card-title>
              <span class="text-h5">Spouse Details</span>
            </v-card-title>
            <v-card-text>
              <div v-if="!hasSpouse">
                <p>No spouse details provided.</p>
              </div>
              <v-list v-else dense>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>First Name</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.spouse.firstName }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Last Name</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.spouse.lastName }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Date of Birth</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.spouse.dob }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Email</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.spouse.email }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Phone Number</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.spouse.phone }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
              <v-btn color="primary" class="mt-4" @click="goToEditSpouse">
                Edit Spouse Details
              </v-btn>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup>
  import { ref, onMounted, computed } from 'vue'
  import { useRouter } from 'vue-router'
  import { getProfile } from '@/services/authService'
  
  const router = useRouter()
  const profile = ref({ spouse: {} })
  
  onMounted(async () => {
    try {
      const data = await getProfile()
      profile.value = data
    } catch {
      router.push('/login')
    }
  })
  
  const hasSpouse = computed(() => {
    const s = profile.value.spouse || {}
    return !!(s.firstName || s.lastName || s.dob || s.email || s.phone)
  })
  
  function goToEditSpouse() {
    router.push('/edit/spouse')
  }
  </script>
  
  <style scoped>
  .pa-4 {
    padding: 16px !important;
  }
  .mt-4 {
    margin-top: 16px !important;
  }
  </style>
  