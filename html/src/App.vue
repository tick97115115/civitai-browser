<template>
  <v-card height="100vh">
    <v-layout height="100%">
      <v-navigation-drawer permanent rail expand-on-hover>
        <v-list>
          <v-list-item prepend-icon="mdi-web" title="Civitai" to="/"> </v-list-item>
          <v-list-item prepend-icon="mdi-home" title="Local" to="/local"> </v-list-item>
          <v-list-item prepend-icon="mdi-cog" title="Settings" to="/settings"> </v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-main><RouterView></RouterView></v-main>
    </v-layout>
  </v-card>
</template>

<script setup>
import { useRouter } from 'vue-router'
import SearchButton from './components/SearchButton.vue'
import { ref, watch } from 'vue'

const router = useRouter()
const routes = ref(router.getRoutes())
</script>
