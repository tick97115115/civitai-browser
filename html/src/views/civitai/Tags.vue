<template>
  <div class="text-center">
    <v-pagination v-model="page" :length="15" :total-visible="7"></v-pagination>
  </div>
</template>
<script setup>
import { ref } from 'vue'

const page = ref(1)
</script>
