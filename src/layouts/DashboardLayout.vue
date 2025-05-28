<template>
    <v-container fluid class="dashboard-layout">
      <v-row>
        <v-col>
          <!-- Nested page content -->
          <router-view />
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup>
  // No additional script needed here
  </script>
  
  <style scoped>
  .dashboard-layout {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem 1rem;
    background-color: #FFFFFF;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
  </style>
  