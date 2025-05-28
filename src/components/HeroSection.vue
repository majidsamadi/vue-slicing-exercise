<template>
    <section class="hero">
      <div class="hero-content">
        <h2 class="hero-title">Welcome to MySite</h2>
        <p class="hero-subtitle">
          We build amazing experiences with Vue.js.
        </p>
        <button class="hero-cta">Get Started</button>
      </div>
      <div class="hero-image">
        <!-- You can replace this with an <img> or background-image -->
        <div class="placeholder-image">[Image]</div>
      </div>
    </section>
  </template>
  
  <script setup>
  // No logic needed yet
  </script>
  
  <style scoped>
  .hero {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 4rem 2rem;
    background-color: #eef2f5;
  }
  
  .hero-content {
    max-width: 50%;
  }
  
  .hero-title {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }
  
  .hero-subtitle {
    font-size: 1.125rem;
    margin-bottom: 2rem;
    line-height: 1.5;
  }
  
  .hero-cta {
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    border: none;
    cursor: pointer;
  }
  
  .placeholder-image {
    width: 300px;
    height: 200px;
    background-color: #ccc;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  </style>
  