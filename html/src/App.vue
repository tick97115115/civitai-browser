<template>
  <v-card height="100vh">
    <v-layout height="100%">
      <v-app-bar color="primary">
        <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

        <v-toolbar-title>Civitai Browser</v-toolbar-title>

        <v-spacer></v-spacer>

        <!-- <template v-if="$vuetify.display.mdAndUp">
          <v-btn icon="mdi-dots-vertical" variant="text"></v-btn>

          <v-btn icon="mdi-filter" variant="text"></v-btn>
        </template> -->
        <SearchButton></SearchButton>
      </v-app-bar>

      <v-navigation-drawer
        v-model="drawer"
        :location="$vuetify.display.mobile ? 'bottom' : undefined"
        temporary
      >
        <v-list>
          <v-list-item
            v-for="route in routes"
            :key="route"
            :title="route.name"
            :to="route.path"
          ></v-list-item>
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

const drawer = ref(false)
const group = ref(null)

watch(group, () => {
  drawer.value = false
})
</script>
