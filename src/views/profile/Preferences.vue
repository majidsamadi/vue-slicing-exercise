<!-- src/views/profile/Preferences.vue -->
<template>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" md="8">
          <v-card elevation="2" class="pa-4">
            <v-card-title>
              <span class="text-h5">Personal Preferences</span>
            </v-card-title>
            <v-card-text>
              <div v-if="!hasPreferences">
                <p>No preferences provided.</p>
              </div>
              <div v-else>
                <!-- Hobbies and Interests -->
                <div class="mb-4">
                  <h3>Hobbies and Interests</h3>
                  <v-chip-group column>
                    <v-chip
                      v-for="(item, i) in preferences.hobbies"
                      :key="`hobby-${i}`"
                    >
                      {{ item }}
                    </v-chip>
                  </v-chip-group>
                </div>
                <!-- Favorite Sports -->
                <div class="mb-4">
                  <h3>Favorite Sport(s)</h3>
                  <v-chip-group column>
                    <v-chip
                      v-for="(item, i) in preferences.favoriteSports"
                      :key="`sport-${i}`"
                    >
                      {{ item }}
                    </v-chip>
                  </v-chip-group>
                </div>
                <!-- Music Genres -->
                <div class="mb-4">
                  <h3>Preferred Music Genre(s)</h3>
                  <v-chip-group column>
                    <v-chip
                      v-for="(item, i) in preferences.musicGenres"
                      :key="`music-${i}`"
                    >
                      {{ item }}
                    </v-chip>
                  </v-chip-group>
                </div>
                <!-- Movies/TV Shows -->
                <div class="mb-4">
                  <h3>Preferred Movie/TV Show(s)</h3>
                  <v-chip-group column>
                    <v-chip
                      v-for="(item, i) in preferences.moviesShows"
                      :key="`movie-${i}`"
                    >
                      {{ item }}
                    </v-chip>
                  </v-chip-group>
                </div>
              </div>
              <v-btn color="primary" class="mt-4" @click="goToEditPreferences">
                Edit Preferences
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
  const preferences = ref({
    hobbies: [],
    favoriteSports: [],
    musicGenres: [],
    moviesShows: []
  })
  
  onMounted(async () => {
    try {
      const user = await getProfile()
      const p = user.preferences || {}
      preferences.value.hobbies = Array.isArray(p.hobbies) ? p.hobbies : []
      preferences.value.favoriteSports = Array.isArray(p.favoriteSports) ? p.favoriteSports : []
      preferences.value.musicGenres = Array.isArray(p.musicGenres) ? p.musicGenres : []
      preferences.value.moviesShows = Array.isArray(p.moviesShows) ? p.moviesShows : []
    } catch {
      router.push('/login')
    }
  })
  
  const hasPreferences = computed(() =>
    preferences.value.hobbies.length ||
    preferences.value.favoriteSports.length ||
    preferences.value.musicGenres.length ||
    preferences.value.moviesShows.length
  )
  
  function goToEditPreferences() {
    router.push('/edit/preferences')
  }
  </script>
  
  <style scoped>
  .pa-4 { padding: 16px !important; }
  .mb-4 { margin-bottom: 16px !important; }
  </style>
  