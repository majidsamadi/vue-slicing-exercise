<!-- src/views/ProfilePage.vue -->
<template>
    <div class="profile-page" v-if="user">
      <h1>Edit Your Profile</h1>
      <form @submit.prevent="onSave">
        <!-- Additional Details -->
        <fieldset>
          <legend>Additional Details</legend>
          <div>
            <label for="dob">Date of Birth</label>
            <input id="dob" v-model="form.additional.dob" type="date" />
          </div>
          <div>
            <label for="phone">Phone Number</label>
            <input id="phone" v-model="form.additional.phone" type="tel" />
          </div>
          <div>
            <label for="address">Address</label>
            <input id="address" v-model="form.additional.address" />
          </div>
          <div>
            <label for="nationality">Nationality</label>
            <input id="nationality" v-model="form.additional.nationality" />
          </div>
        </fieldset>
  
        <!-- Spouse Details -->
        <fieldset>
          <legend>Spouse Details</legend>
          <div>
            <label for="spouseFirstName">First Name</label>
            <input id="spouseFirstName" v-model="form.spouse.firstName" />
          </div>
          <div>
            <label for="spouseLastName">Last Name</label>
            <input id="spouseLastName" v-model="form.spouse.lastName" />
          </div>
          <div>
            <label for="spouseDob">Date of Birth</label>
            <input id="spouseDob" v-model="form.spouse.dob" type="date" />
          </div>
          <div>
            <label for="spouseEmail">Email</label>
            <input id="spouseEmail" v-model="form.spouse.email" type="email" />
          </div>
          <div>
            <label for="spousePhone">Phone Number</label>
            <input id="spousePhone" v-model="form.spouse.phone" type="tel" />
          </div>
        </fieldset>
  
        <!-- Personal Preferences -->
        <fieldset>
          <legend>Personal Preferences</legend>
          <div
            class="preference"
            v-for="(pref, idx) in form.preferences"
            :key="idx"
          >
            <label :for="`pref-${idx}`">Preference</label>
            <input :id="`pref-${idx}`" v-model="pref.preference" />
            <label :for="`value-${idx}`">Value</label>
            <input :id="`value-${idx}`" v-model="pref.value" />
          </div>
          <button type="button" @click="addPreference">+ Add Preference</button>
        </fieldset>
  
        <button type="submit">Save Profile</button>
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
    additional: { dob: '', phone: '', address: '', nationality: '' },
    spouse: { firstName: '', lastName: '', dob: '', email: '', phone: '' },
    preferences: []
  })
  
  onMounted(async () => {
  try {
    const u = await getProfile()
    user.value = u
    Object.assign(form.additional, u.additional || {})
    Object.assign(form.spouse, u.spouse || {})
    form.preferences = u.preferences ? [...u.preferences] : []
  } catch (err) {
    router.push('/login')
  }
})

  async function onSave() {
    const updated = {
      ...user.value,
      additional: { ...form.additional },
      spouse: { ...form.spouse },
      preferences: [...form.preferences]
    }
    await updateProfile(updated)
    router.push('/dashboard')
  }
  </script>
  
  <style scoped>
  .profile-page {
    max-width: 600px;
    margin: 2rem auto;
    padding: 1.5rem;
    background: #fff;
    border-radius: 8px;
  }
  .profile-page fieldset {
    margin-bottom: 1.5rem;
    padding: 1rem;
    border: 1px solid #ccc;
  }
  .profile-page div {
    margin-bottom: 1rem;
  }
  .profile-page label {
    display: block;
    margin-bottom: 0.5rem;
  }
  .profile-page input {
    width: 100%;
    padding: 0.5rem;
    box-sizing: border-box;
  }
  button {
    padding: 0.75rem 1.5rem;
    margin-top: 1rem;
  }
  </style>
  