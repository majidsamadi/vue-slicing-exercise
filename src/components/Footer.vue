<!-- src/components/Footer.vue -->
<template>
    <footer class="site-footer">
      <div class="footer-content">
        <p>&copy; 2025 MySite. All rights reserved.</p>
        <nav class="footer-nav">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
        </nav>
      </div>
    </footer>
  </template>
  
  <script setup>
  // No logic needed
  </script>
  
  <style scoped>
  .site-footer {
    background-color: #333;
    color: #fff;
    padding: 2rem;
    text-align: center;
  }
  
  .footer-nav {
    margin-top: 1rem;
  }
  
  .footer-nav a {
    margin: 0 1rem;
    color: #ccc;
    text-decoration: none;
    font-size: 0.9rem;
  }
  </style>
  