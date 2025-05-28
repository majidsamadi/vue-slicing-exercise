<!-- src/views/EditProfile.vue -->
<template>
    <div class="edit-page" v-if="user">
      <header class="profile-header">
        <h1>Edit Profile</h1>
        <button class="cancel-btn" @click="goBack">Cancel</button>
      </header>
      <form @submit.prevent="onSave">
        <!-- Basic Info -->
        <fieldset>
          <legend>Basic Details</legend>
          <label>Salutation</label>
          <select v-model="form.salutation" required>
            <option disabled value="">Select...</option>
            <option>Mr.</option>
            <option>Ms.</option>
            <option>Dr.</option>
          </select>
          <label>First Name</label>
          <input v-model="form.firstName" required />
          <label>Last Name</label>
          <input v-model="form.lastName" required />
        </fieldset>
  
        <!-- Additional Info -->
        <fieldset>
          <legend>Additional Details</legend>
          <label>Date of Birth</label>
          <input type="date" v-model="form.additional.dob" />
          <label>Phone</label>
          <input type="tel" v-model="form.additional.phone" />
          <label>Address</label>
          <input v-model="form.additional.address" />
          <label>Nationality</label>
          <input v-model="form.additional.nationality" />
        </fieldset>
  
        <!-- Spouse Info -->
        <fieldset>
          <legend>Spouse Details</legend>
          <label>First Name</label>
          <input v-model="form.spouse.firstName" />
          <label>Last Name</label>
          <input v-model="form.spouse.lastName" />
          <label>Date of Birth</label>
          <input type="date" v-model="form.spouse.dob" />
          <label>Email</label>
          <input type="email" v-model="form.spouse.email" />
          <label>Phone</label>
          <input v-model="form.spouse.phone" />
        </fieldset>
  
        <!-- Preferences -->
        <fieldset>
          <legend>Personal Preferences</legend>
          <div v-for="(pref, i) in form.preferences" :key="i">
            <label>Preference</label>
            <input v-model="pref.preference" placeholder="e.g. Hobby" />
            <label>Value</label>
            <input v-model="pref.value" placeholder="e.g. Reading" />
          </div>
          <button type="button" @click="addPreference">+ Add Preference</button>
        </fieldset>
  
        <button type="submit">Save</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, reactive, onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  import { getProfile, updateProfile } from '../services/authService'
  
  const router = useRouter()
  const user = ref(null)
  const form = reactive({
    salutation: '',
    firstName: '',
    lastName: '',
    additional: { dob: '', phone: '', address: '', nationality: '' },
    spouse: { firstName: '', lastName: '', dob: '', email: '', phone: '' },
    preferences: []
  })
  
  onMounted(async () => {
    try {
      const u = await getProfile()
      user.value = u
      Object.assign(form, {
        salutation: u.salutation || '',
        firstName: u.firstName || '',
        lastName: u.lastName || '',
        additional: u.additional || {},
        spouse: u.spouse || {},
        preferences: u.preferences ? [...u.preferences] : []
      })
    } catch {
      router.push('/login')
    }
  })
  
  function addPreference() {
    form.preferences.push({ preference: '', value: '' })
  }
  
  async function onSave() {
    const payload = {
      salutation: form.salutation,
      firstName: form.firstName,
      lastName: form.lastName,
      additional: form.additional,
      spouse: form.spouse,
      preferences: form.preferences.filter(p => p.preference && p.value)
    }
    await updateProfile(payload)
    router.push('/my-profile')
  }
  
  function goBack() {
    router.push('/my-profile')
  }
  </script>
  
  <style scoped>
  .edit-page {
    max-width: 600px;
    margin: 2rem auto;
    padding: 1rem;
    background: #fff;
    border-radius: 8px;
  }
  fieldset {
    margin-bottom: 1.5rem;
    border: 1px solid #ccc;
    padding: 1rem;
  }
  label {
    display: block;
    margin: 0.5rem 0 0.25rem;
  }
  input, select {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
  }
  button {
    padding: 0.5rem 1rem;
    margin-top: 1rem;
  }
  </style>
  