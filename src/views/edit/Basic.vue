<!-- src/views/edit/Basic.vue -->
<template>
    <v-form ref="formRef" v-model="isValid">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="12">
            <v-card elevation="2" class="pa-4">
              <v-card-title>Edit Basic Details</v-card-title>
              <v-card-text>
                <v-row>
                  <!-- Profile Image Upload -->
                  <v-col cols="12" class="text-center">
                    <v-avatar size="100" class="mb-2">
                      <v-img :src="previewUrl || form.avatar || '/assets/default-avatar.png'" />
                    </v-avatar>
                    <v-file-input
                      v-model="form.avatarFile"
                      accept="image/*"
                      label="Profile Image"
                      prepend-icon="mdi-camera"
                      @change="onFileChange"
                    />
                  </v-col>
  
                  <!-- Email Address -->
                  <v-col cols="12">
                    <v-text-field
                      v-model="form.email"
                      label="Email Address"
                      :rules="[
                        v => !!v || 'Email is required',
                        v => /.+@.+\..+/.test(v) || 'Enter a valid email'
                      ]"
                      required
                    />
                  </v-col>
  
                  <!-- Salutation -->
                  <v-col cols="12" sm="4">
                    <v-select
                      v-model="form.salutation"
                      :items="['Mr.','Ms.','Dr.','Prof.']"
                      label="Salutation"
                      :rules="[v => !!v || 'Required']"
                      required
                    />
                  </v-col>
  
                  <!-- First Name -->
                  <v-col cols="12" sm="4">
                    <v-text-field
                      v-model="form.firstName"
                      label="First Name"
                      :rules="[v => !!v.trim() || 'Required']"
                      required
                    />
                  </v-col>
  
                  <!-- Last Name -->
                  <v-col cols="12" sm="4">
                    <v-text-field
                      v-model="form.lastName"
                      label="Last Name"
                      :rules="[v => !!v.trim() || 'Required']"
                      required
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
  import { getProfile, updateBasic } from '@/services/profileService';
  
  const router = useRouter();
  const formRef = ref(null);
  const isValid = ref(false);
  const form = ref({
    avatar: '',
    avatarFile: '',
    email: '',
    salutation: '',
    firstName: '',
    lastName: ''
  });
  const previewUrl = ref('');
  
  onMounted(async () => {
    try {
      const user = await getProfile();
      form.value.avatar = user.avatar || '';
      form.value.email = user.email || '';
      form.value.salutation = user.salutation || '';
      form.value.firstName = user.firstName || '';
      form.value.lastName = user.lastName || '';
      previewUrl.value = user.avatar || '';
      isValid.value = true;
    } catch {
      router.push('/login');
    }
  });
  
  function onFileChange(file) {
    if (file) {
      const reader = new FileReader();
      reader.onload = e => (previewUrl.value = e.target.result);
      reader.readAsDataURL(file);
      form.value.avatarFile = file;
    }
  }
  
  async function onSave() {
    if (formRef.value.validate()) {
      let avatarData = form.value.avatar;
      if (form.value.avatarFile) {
        avatarData = await new Promise(resolve => {
          const reader = new FileReader();
          reader.onload = e => resolve(e.target.result);
          reader.readAsDataURL(form.value.avatarFile);
        });
      }
      const payload = {
        avatar: avatarData,
        email: form.value.email,
        salutation: form.value.salutation,
        firstName: form.value.firstName,
        lastName: form.value.lastName
      };
      await updateBasic(payload);
      router.push('/profile/basic');
    }
  }
  </script>
  
  <style scoped>
  .pa-4 { padding: 16px !important; }
  .mb-2 { margin-bottom: 8px !important; }
  </style>
  