<!-- src/views/edit/Spouse.vue -->
<template>
    <v-form ref="formRef" v-model="isValid">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="12">
            <v-card elevation="2" class="pa-4">
              <v-card-title>Edit Spouse Details</v-card-title>
              <v-card-text>
                <v-row>
                  <!-- First Name -->
                  <v-col cols="12" sm="6">
                    <v-text-field
                      v-model="form.firstName"
                      label="First Name"
                      :rules="[v => !!v.trim() || 'First name is required']"
                      required
                    />
                  </v-col>
  
                  <!-- Last Name -->
                  <v-col cols="12" sm="6">
                    <v-text-field
                      v-model="form.lastName"
                      label="Last Name"
                      :rules="[v => !!v.trim() || 'Last name is required']"
                      required
                    />
                  </v-col>
  
                  <!-- Date of Birth -->
                  <v-col cols="12" sm="6">
                    <v-text-field
                      v-model="form.dob"
                      label="Date of Birth"
                      type="date"
                      :rules="[v => !!v || 'DOB is required']"
                      required
                    />
                  </v-col>
  
                  <!-- Email -->
                  <v-col cols="12" sm="6">
                    <v-text-field
                      v-model="form.email"
                      label="Email"
                      :rules="[
                        v => !!v.trim() || 'Email is required',
                        v => /.+@.+\..+/.test(v) || 'Enter a valid email'
                      ]"
                      required
                    />
                  </v-col>
  
                  <!-- Phone Number -->
                  <v-col cols="12" sm="6">
                    <v-text-field
                      v-model="form.phone"
                      label="Phone Number"
                      :rules="[
                        v => !!v || 'Phone is required',
                        v => /^\d{7,15}$/.test(v) || 'Enter 7–15 digits'
                      ]"
                      required
                    />
                  </v-col>
                </v-row>
              </v-card-text>
              <v-card-actions>
                <v-spacer />
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
  import { getProfile, updateSpouse } from '@/services/profileService'
  
  const router = useRouter()
  const formRef = ref(null)
  const isValid = ref(false)
  const form = ref({
    firstName: '',
    lastName: '',
    dob: '',
    email: '',
    phone: ''
  })
  
  onMounted(async () => {
    try {
      const user = await getProfile()
      const s = user.spouse || {}
      form.value = {
        firstName: s.firstName || '',
        lastName: s.lastName || '',
        dob: s.dob || '',
        email: s.email || '',
        phone: s.phone || ''
      }
      isValid.value = true
    } catch {
      router.push('/login')
    }
  })
  
  async function onSave() {
    if (formRef.value.validate()) {
      await updateSpouse({ spouse: { ...form.value } })
      router.push('/profile/spouse')
    }
  }
  </script>
  
  <style scoped>
  .pa-4 { padding: 16px !important; }
  </style>
  