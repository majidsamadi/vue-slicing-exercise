<!-- src/components/Header.vue -->
<template>
  <header class="site-header">
    <h1 class="logo">MySite</h1>
    <nav class="nav-links">
      <a href="#">Home</a>
      <a href="#">About</a>
      <a href="#">Contact</a>
    </nav>
  </header>
</template>

<script setup>
// No logic needed yet
</script>

<style scoped>
.site-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 2rem;
  background-color: #f2f2f2;
}
.logo {
  font-size: 1.5rem;
  font-weight: bold;
}
.nav-links a {
  margin-left: 1.5rem;
  text-decoration: none;
  color: #333;
  font-weight: 500;
}
</style>
