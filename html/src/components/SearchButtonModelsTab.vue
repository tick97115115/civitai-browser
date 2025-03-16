<template>
  <v-container>
    <v-text-field label="Search Models"></v-text-field>

    <!-- <v-row>
        <v-col><v-btn type="submit">Save</v-btn></v-col>
        <v-col><v-btn type="submit">Run</v-btn></v-col>
      </v-row> -->
    <v-row dense>
      <v-col cols="12" md="8">
        <v-text-field density="compact" label="APIKEY"></v-text-field
      ></v-col>
      <v-col cols="12" md="4"><v-checkbox density="compact" label="NSFW"></v-checkbox></v-col
    ></v-row>
    <v-combobox
      v-model="select"
      :items="model_type_items"
      label="Types"
      chips
      multiple
      clearable
      density="compact"
    ></v-combobox>
    <v-row dense>
      <v-col cols="12" md="4"><v-text-field density="compact" label="Tag"></v-text-field></v-col>
      <v-col cols="12" md="8"
        ><v-text-field density="compact" label="Username"></v-text-field
      ></v-col>
    </v-row>
    <v-row dense>
      <v-col cols="12" md="7"
        ><v-combobox density="compact" label="Sort" :items="models_sort_items"></v-combobox
      ></v-col>
      <v-col cols="12" md="5"
        ><v-combobox density="compact" label="Period" :items="models_period_items"></v-combobox
      ></v-col>
    </v-row>
    <v-row dense>
      <v-col cols="12" md="6">
        <v-text-field density="compact" label="Page Size"></v-text-field
      ></v-col>
      <v-col cols="12" md="6">
        <v-text-field density="compact" label="Current Page"></v-text-field
      ></v-col>
    </v-row>
    <v-row justify="space-evenly">
      <v-btn type="submit">Save</v-btn
      ><v-btn type="submit" @click="console.log('Hiiiii')">Run</v-btn>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import {
  model_types,
  models_request_sort,
  models_request_period,
  // ModelsRequestOpts,
} from '../models/baseModels/misc'


import { convert_arktype_enum_to_array } from '../utils/misc'

const select = ref([])

const model_type_items = convert_arktype_enum_to_array(model_types)
const models_sort_items = convert_arktype_enum_to_array(models_request_sort)
const models_period_items = convert_arktype_enum_to_array(models_request_period)

// const props = defineProps<{
//   models_query_opts?: ModelsRequestOpts
// }>()
</script>