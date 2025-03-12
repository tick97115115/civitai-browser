<template>
  <v-btn icon="mdi-magnify" variant="text" id="menu-activator"> </v-btn>

  <v-menu activator="#menu-activator" :close-on-content-click="false">
    <v-card>
      <v-tabs v-model="tab" align-tabs="center" bg-color="deep-purple-accent-4" stacked>
        <v-tab value="tab-1">
          <v-icon icon="mdi-cards-playing"></v-icon>

          Models
        </v-tab>

        <v-tab value="tab-2">
          <v-icon icon="mdi-image-multiple"></v-icon>

          Images
        </v-tab>

        <v-tab value="tab-3">
          <v-icon icon="mdi-account-box"></v-icon>

          Creators
        </v-tab>
        <v-tab value="tab-4">
          <v-icon icon="mdi-tag-multiple"></v-icon>

          Tags
        </v-tab>
      </v-tabs>

      <v-tabs-window v-model="tab">
        <v-tabs-window-item v-for="i in 4" :key="i" :value="'tab-' + i">
          <v-card>
            <v-card-text>{{ text }}</v-card-text>
          </v-card>
        </v-tabs-window-item>
      </v-tabs-window>
    </v-card>
  </v-menu>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const tab = ref(null)

const text = `current tab: ${tab.value}
  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.`
</script>
