<!-- src/components/Testimonial.vue -->
<template>
    <section class="testimonials">
      <h2 class="testimonials-title">What Our Users Say</h2>
      <div class="testimonial-cards">
        <div 
          class="testimonial-card" 
          v-for="(t, i) in testimonials" 
          :key="i"
        >
          <p class="quote">“{{ t.quote }}”</p>
          <div class="author">
            <strong>{{ t.name }}</strong>, {{ t.role }}
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const testimonials = ref([
    { quote: 'Vue makes UI development a breeze!', name: 'Alice', role: 'Frontend Engineer' },
    { quote: 'Hot reload is a game changer.', name: 'Bob', role: 'Designer' },
    { quote: 'Component-based code keeps us organized.', name: 'Carol', role: 'Product Manager' }
  ])
  </script>
  
  <style scoped>
  .testimonials {
    padding: 4rem 2rem;
    background-color: #f9fafb;
    text-align: center;
  }
  
  .testimonials-title {
    font-size: 2rem;
    margin-bottom: 2rem;
  }
  
  .testimonial-cards {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    justify-content: center;
  }
  
  .testimonial-card {
    max-width: 300px;
    padding: 2rem;
    border-radius: 8px;
    background-color: white;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  }
  
  .quote {
    font-style: italic;
    margin-bottom: 1rem;
  }
  
  .author {
    font-size: 0.9rem;
    color: #555;
  }
  </style>
  