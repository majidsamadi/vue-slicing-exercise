<!-- src/components/FeatureGrid.vue -->
<template>
    <section class="feature-grid">
      <div class="feature-card" v-for="(feature, i) in features" :key="i">
        <div class="icon">{{ feature.icon }}</div>
        <h3 class="title">{{ feature.title }}</h3>
        <p class="description">{{ feature.description }}</p>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const features = ref([
    { icon: '🚀', title: 'Fast Performance', description: 'Blazing-fast load times with Vite & Vue.' },
    { icon: '🔧', title: 'Easy to Customize', description: 'Component-based architecture makes tweaks a breeze.' },
    { icon: '🎨', title: 'Modern Design', description: 'Clean, responsive layouts out of the box.' },
    { icon: '⚡', title: 'Hot Module Reload', description: 'See changes instantly without page reloads.' }
  ])
  </script>
  
  <style scoped>
  .feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
    padding: 4rem 2rem;
    background-color: #fff;
  }
  
  .feature-card {
    text-align: center;
    padding: 2rem;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
  }
  
  .icon {
    font-size: 2rem;
    margin-bottom: 1rem;
  }
  
  .title {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
  }
  
  .description {
    font-size: 1rem;
    color: #666;
  }
  </style>
  