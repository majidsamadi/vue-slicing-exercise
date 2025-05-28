<!-- src/layouts/MasterLayout.vue -->
<template>
  <v-app class="app-bg">
    <!-- Top App Bar (only on authenticated pages) -->
    <v-app-bar
      v-if="showDrawer"
      app
      color="white"
      flat
      elevate-on-scroll
      class="px-0"
    >
      <!-- Logo on the far left -->
      <v-toolbar-title class="logo-title">
        <v-img
          src="/assets/logo.png"
          alt="Logo"
          contain
          height="40"
          width="40"
        />
      </v-toolbar-title>
      <v-spacer />
      <!-- Hamburger menu on the right -->
      <v-btn icon @click="drawerOpen = !drawerOpen">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
    </v-app-bar>

    <!-- Navigation drawer -->
    <NavigationDrawer v-if="showDrawer" v-model:open="drawerOpen" />

    <!-- Main application content -->
    <v-main class="main-content">
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import NavigationDrawer from '@/components/navigation/NavigationDrawer.vue'

const route = useRoute()
const showDrawer = computed(() => route.matched.some(rec => rec.meta.requiresAuth))
const drawerOpen = ref(false)
</script>

<style scoped>
.app-bg {
  /* changed from full-bleed image to a simple light background */
  background-color: #F5F7FA;
  min-height: 100vh;
}

.v-main.main-content {
  background-color: transparent !important;
  padding-top: 64px;    /* offset for app-bar */
  padding-inline: 16px;
}

/* Remove default toolbar padding */
.v-app-bar.px-0,
.v-app-bar.px-0 .v-toolbar__content {
  padding-left: 0 !important;
  padding-right: 0 !important;
}

/* Ensure logo is flush to the left */
.logo-title {
  margin: 0;
  padding-left: 16px;
}
</style>
