<!-- src/views/profile/Additional.vue -->
<template>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" md="8">
          <v-card elevation="2" class="pa-4">
            <v-card-title>
              <span class="text-h5">Additional Details</span>
            </v-card-title>
            <v-card-text>
              <v-list dense>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Marital Status</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.additional?.maritalStatus || 'N/A' }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Date of Birth</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.additional?.dob || 'N/A' }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Phone Number</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.additional?.phone || 'N/A' }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Home Address</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.additional?.homeAddress || 'N/A' }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Country</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.additional?.country || 'N/A' }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Postal Code</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.additional?.postalCode || 'N/A' }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Nationality</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.additional?.nationality || 'N/A' }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
              <v-btn color="primary" class="mt-4" @click="goToEditAdditional">
                Edit Additional Details
              </v-btn>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  import { getProfile } from '@/services/authService'
  
  const router = useRouter()
  const profile = ref({ additional: {} })
  
  onMounted(async () => {
    try {
      const data = await getProfile()
      profile.value = data
    } catch {
      router.push('/login')
    }
  })
  
  function goToEditAdditional() {
    router.push('/edit/additional')
  }
  </script>
  
  <style scoped>
  .pa-4 { padding: 16px !important; }
  .mt-4 { margin-top: 16px !important; }
  </style>
  