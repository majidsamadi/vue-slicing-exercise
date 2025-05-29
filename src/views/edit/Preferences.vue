<!-- src/views/edit/Preferences.vue -->
<template>
    <v-form ref="formRef" v-model="isValid">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="12">
            <v-card elevation="2" class="pa-4">
              <v-card-title>Edit Personal Preferences</v-card-title>
              <v-card-text>
                <!-- Hobbies and Interests -->
                <v-combobox
                  v-model="form.preferences.hobbies"
                  :items="[]"
                  label="Hobbies and Interests"
                  multiple
                  chips
                />

                <!-- Favorite Sports -->
                <v-combobox
                  v-model="form.preferences.favoriteSports"
                  :items="[]"
                  label="Favorite Sports"
                  multiple
                  chips
                />

                <!-- Music Genres -->
                <v-combobox
                  v-model="form.preferences.musicGenres"
                  :items="[]"
                  label="Music Genres"
                  multiple
                  chips
                />

                <!-- Movies and Shows -->
                <v-combobox
                  v-model="form.preferences.moviesShows"
                  :items="[]"
                  label="Movies & Shows"
                  multiple
                  chips
                />
              </v-card-text>
              <v-card-actions>
                <v-btn color="primary" :disabled="!isValid" @click="onSave">
                  Save
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getProfile, updatePreferences } from '@/services/profileService'

const router = useRouter()
const formRef = ref(null)
const isValid = ref(false)
const form = ref({
  preferences: {
    hobbies: [],
    favoriteSports: [],
    musicGenres: [],
    moviesShows: []
  }
})

onMounted(async () => {
  try {
    const user = await getProfile()
    const p = user.preferences || {}
    form.value.preferences.hobbies = p.hobbies || []
    form.value.preferences.favoriteSports = p.favoriteSports || []
    form.value.preferences.musicGenres = p.musicGenres || []
    form.value.preferences.moviesShows = p.moviesShows || []
    isValid.value = true
  } catch {
    router.push('/login')
  }
})

async function onSave() {
  if (formRef.value.validate()) {
    const payload = { preferences: { ...form.value.preferences } }
    await updatePreferences(payload)
    router.push('/profile/preferences')
  }
}
</script>

<style scoped>
.pa-4 { padding: 16px !important; }
.mb-4 { margin-bottom: 16px !important; }
</style>
