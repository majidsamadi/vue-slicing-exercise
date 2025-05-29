<!-- src/views/profile/Basic.vue -->
<template>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" md="12">
          <v-card elevation="2" class="pa-4">
            <v-card-title>
              <span class="text-h5">Basic Details</span>
            </v-card-title>
            <v-card-text class="text-center">
              <!-- Profile Image -->
              <v-avatar size="100" class="mx-auto mb-4">
                <v-img :src="profile.avatar || '/assets/default-avatar.png'" />
              </v-avatar>
            </v-card-text>
            <v-card-text>
              <v-list dense>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Salutation</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.salutation || 'N/A' }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>First Name</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.firstName || 'N/A' }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Last Name</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.lastName || 'N/A' }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Email Address</v-list-item-title>
                    <v-list-item-subtitle>{{ profile.email }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn color="primary" @click="goToEditBasic">
                Edit Basic Details
              </v-btn>
            </v-card-actions>
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
  const profile = ref({})
  
  onMounted(async () => {
    try {
      const data = await getProfile()
      profile.value = data
    } catch {
      router.push('/login')
    }
  })
  
  function goToEditBasic() {
    router.push('/edit/basic')
  }
  </script>
  
  <style scoped>
  .pa-4 { padding: 16px !important; }
  .mb-4 { margin-bottom: 16px !important; }
  </style>
  