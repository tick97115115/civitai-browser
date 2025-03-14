<template>
  <v-main></v-main>
  <v-footer app="true" class="d-flex justify-center">
    <v-pagination v-model="page" :length="15" :total-visible="7"></v-pagination>
  </v-footer>
</template>
<script setup>
import { ref } from 'vue'

const page = ref(1)
</script>
