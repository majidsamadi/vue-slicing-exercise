<!-- src/views/dashboard/Dashboard.vue -->
<template>
  <!-- Hero Section -->
  <v-row align="center" justify="center" class="mb-12">
    <v-col cols="12" md="8" class="text-center">
      <h1 class="display-2 font-weight-bold">Welcome to MyApp</h1>
      <p class="subtitle-1 mb-6">Manage your profile, settings, and preferences all in one place.</p>
      <v-btn color="primary" large @click="goToProfile">
        Get Started
      </v-btn>
    </v-col>
  </v-row>

  <!-- Features Grid -->
  <v-row class="mb-12" dense>
    <v-col
      v-for="(feature, i) in features"
      :key="i"
      cols="12"
      sm="6"
      md="4"
    >
      <v-card outlined class="pa-4 text-center">
        <v-icon size="48" class="mb-4">{{ feature.icon }}</v-icon>
        <h3 class="headline mb-2">{{ feature.title }}</h3>
        <p>{{ feature.desc }}</p>
      </v-card>
    </v-col>
  </v-row>

  <!-- Testimonial Section -->
  <v-row align="center" justify="center">
    <v-col cols="12" md="8">
      <v-carousel hide-delimiter-background height="200">
        <v-carousel-item
          v-for="(testimonial, i) in testimonials"
          :key="i"
        >
          <div class="text-center">
            <p class="subtitle-1 mb-4">"{{ testimonial.quote }}"</p>
            <p class="caption font-italic">— {{ testimonial.author }}</p>
          </div>
        </v-carousel-item>
      </v-carousel>
    </v-col>
  </v-row>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

function goToProfile() {
  router.push('/profile/basic')
}

const features = ref([
  {
    icon: 'mdi-account-circle',
    title: 'Profile Management',
    desc: 'Update your personal information and settings.'
  },
  {
    icon: 'mdi-lock',
    title: 'Secure Login',
    desc: 'Keep your account safe with token-based authentication.'
  },
  {
    icon: 'mdi-cog',
    title: 'Customization',
    desc: 'Set your preferences and adjust your experience.'
  }
])

const testimonials = ref([
  { quote: 'This app made managing my profile a breeze!', author: 'Jane Doe' },
  { quote: 'I love the intuitive design and ease of use.', author: 'John Smith' },
  { quote: 'The best user experience I have ever had.', author: 'Emily Johnson' }
])
</script>

<style scoped>
.display-2 {
  font-size: 3rem;
}
.subtitle-1 {
  font-size: 1.25rem;
}
.pa-4 {
  padding: 16px !important;
}
.mb-12 {
  margin-bottom: 3rem;
}
.text-center {
  text-align: center;
}
</style>
