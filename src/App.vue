<!-- src/App.vue -->
<!-- <template> -->
  <!-- Only show drawer when the route is protected -->
  <!-- <NavigationDrawer v-if="route.meta.requiresAuth" /> -->

  <!-- Always render the page itself -->
  <!-- <router-view />
</template>

<script setup>
import { useRoute } from 'vue-router'
import NavigationDrawer from '@/components/navigation/NavigationDrawer.vue'

const route = useRoute()
</script> -->

<template>
  <MasterLayout />
</template>

<script setup>
import MasterLayout from '@/layouts/MasterLayout.vue'
</script>



<style>
/* Global styles (optional) */

body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
}

a {
  color: #42b983;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

button {
  cursor: pointer;
  background-color: #42b983;
  border: none;
  color: white;
  border-radius: 4px;
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>
