<template>
  <v-dialog v-model="dialog" scrollable width="auto" min-width="400px">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn icon="mdi-magnify" v-bind="activatorProps" variant="text"> </v-btn>
    </template>

    <v-card>
      <v-card-text>
        <v-tabs v-model="tab" align-tabs="center" bg-color="deep-purple-accent-4" stacked>
          <v-tab value="tab-1">
            <v-icon icon="mdi-cards-playing"></v-icon>
            Models
          </v-tab>

          <!-- <v-tab value="tab-2">
            <v-icon icon="mdi-image-multiple"></v-icon>
            Images
          </v-tab> -->

          <v-tab value="tab-2">
            <v-icon icon="mdi-account-box"></v-icon>
            Creators
          </v-tab>
          <v-tab value="tab-3">
            <v-icon icon="mdi-tag-multiple"></v-icon>
            Tags
          </v-tab>
        </v-tabs>
        <v-divider></v-divider>

        <v-tabs-window v-model="tab">
          <v-tabs-window-item value="tab-1" @click="console.log(tab)">
            <SearchButtonModelsTab></SearchButtonModelsTab>
          </v-tabs-window-item>

          <!-- <v-tabs-window-item value="tab-2" @click="console.log(tab)"> tab2 </v-tabs-window-item> -->

          <v-tabs-window-item value="tab-2" @click="console.log(tab)">
            <SearchButtonCreatorsTab></SearchButtonCreatorsTab>
          </v-tabs-window-item>

          <v-tabs-window-item value="tab-3" @click="console.log(tab)">
            <SearchButtonTagsTab></SearchButtonTagsTab>
          </v-tabs-window-item>
        </v-tabs-window>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script lang="ts" setup>
import SearchButtonModelsTab from './ModelsSearchContext.vue'
import SearchButtonCreatorsTab from './SearchButtonCreatorsTab.vue'
import SearchButtonTagsTab from './SearchButtonTagsTab.vue'
import { ref, shallowRef } from 'vue'

const tab = ref(null)

const dialog = shallowRef(false)

const text = `current tab: ${tab.value}
  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.`
</script>
