<!-- src/views/edit/Additional.vue -->
<template>
    <v-form ref="formRef" v-model="isValid">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="12">
            <v-card elevation="2" class="pa-4">
              <v-card-title>Edit Additional Details</v-card-title>
              <v-card-text>
                <v-row>
                  <!-- Marital Status -->
                  <v-col cols="12">
                    <v-select
                      v-model="form.maritalStatus"
                      :items="['Single', 'Married', 'Divorced', 'Widowed']"
                      label="Marital Status"
                    />
                  </v-col>
  
                  <!-- Date of Birth -->
                  <v-col cols="12">
                    <v-text-field
                      v-model="form.dob"
                      label="Date of Birth"
                      type="date"
                    />
                  </v-col>
  
                  <!-- Phone -->
                  <v-col cols="12">
                    <v-text-field
                      v-model="form.phone"
                      label="Phone Number"
                    />
                  </v-col>

                  <!-- Home Address -->
                  <v-col cols="12">
                    <v-text-field
                      v-model="form.homeAddress"
                      label="Home Address"
                    />
                  </v-col>
  
                  <!-- Country -->
                  <v-col cols="12">
                    <v-text-field
                      v-model="form.country"
                      label="Country"
                    />
                  </v-col>
  
                  <!-- Postal Code -->
                  <v-col cols="12">
                    <v-text-field
                      v-model="form.postalCode"
                      label="Postal Code"
                    />
                  </v-col>
  
                  <!-- Nationality -->
                  <v-col cols="12">
                    <v-text-field
                      v-model="form.nationality"
                      label="Nationality"
                    />
                  </v-col>
                </v-row>
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
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { getProfile, updateAdditional } from '@/services/profileService';
  
  const router = useRouter();
  const formRef = ref(null);
  const isValid = ref(false);
  const form = ref({
    maritalStatus: '',
    dob: '',
    phone: '',
    homeAddress: '',
    country: '',
    postalCode: '',
    nationality: ''
  });
  
  onMounted(async () => {
    try {
      const user = await getProfile();
      const add = user.additional || {};
      form.value.maritalStatus = add.maritalStatus || '';
      form.value.dob = add.dob || '';
      form.value.phone = add.phone || '';
      form.value.address = add.address || '';
      form.value.homeAddress = add.homeAddress || '';
      form.value.country = add.country || '';
      form.value.postalCode = add.postalCode || '';
      form.value.nationality = add.nationality || '';
      isValid.value = true;
    } catch {
      router.push('/login');
    }
  });
  
  async function onSave() {
    if (formRef.value.validate()) {
      // Prepare payload, converting empty strings to null
      const payload = {
        maritalStatus: form.value.maritalStatus || null,
        dob: form.value.dob || null,
        phone: form.value.phone || null,
        address: form.value.address || null,
        homeAddress: form.value.homeAddress || null,
        country: form.value.country || null,
        postalCode: form.value.postalCode || null,
        nationality: form.value.nationality || null
      };
      await updateAdditional(payload);
      router.push('/profile/additional');
    }
  }
  </script>
  
  <style scoped>
  .pa-4 { padding: 16px !important; }
  </style>
  