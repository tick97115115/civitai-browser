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
} from '../models/models'

import { convert_arktype_enum_to_array } from '../utils/misc'

const select = ref([])

const model_type_items = convert_arktype_enum_to_array(model_types)
const models_sort_items = convert_arktype_enum_to_array(models_request_sort)
const models_period_items = convert_arktype_enum_to_array(models_request_period)

// const props = defineProps<{
//   models_query_opts?: ModelsRequestOpts
// }>()
</script>

<!-- <template>
  <div class="pa-4 text-center">
    <v-dialog width="auto" scrollable>
      <template v-slot:activator="{ props: activatorProps }">
        <v-btn
          color="brown"
          prepend-icon="mdi-earth"
          text="Select Country"
          variant="outlined"
          v-bind="activatorProps"
        ></v-btn>
      </template>

      <template v-slot:default="{ isActive }">
        <v-card prepend-icon="mdi-earth" title="Select Country">
          <v-divider class="mt-3"></v-divider>

          <v-card-text class="px-4" style="height: 300px">
            <v-radio-group v-model="dialog" messages="Select a Country from the radio group">
              <v-radio label="Bahamas, The" value="bahamas"></v-radio>

              <v-radio label="Bahrain" value="bahrain"></v-radio>

              <v-radio label="Bangladesh" value="bangladesh"></v-radio>

              <v-radio label="Barbados" value="barbados"></v-radio>

              <v-radio label="Belarus" value="belarus"></v-radio>

              <v-radio label="Belgium" value="belgium"></v-radio>

              <v-radio label="Belize" value="belize"></v-radio>

              <v-radio label="Benin" value="benin"></v-radio>

              <v-radio label="Bhutan" value="bhutan"></v-radio>

              <v-radio label="Bolivia" value="bolivia"></v-radio>

              <v-radio label="Bosnia and Herzegovina" value="bosnia"></v-radio>

              <v-radio label="Botswana" value="botswana"></v-radio>

              <v-radio label="Brazil" value="brazil"></v-radio>

              <v-radio label="Brunei" value="brunei"></v-radio>

              <v-radio label="Bulgaria" value="bulgaria"></v-radio>

              <v-radio label="Burkina Faso" value="burkina"></v-radio>

              <v-radio label="Burma" value="burma"></v-radio>

              <v-radio label="Burundi" value="burundi"></v-radio>
            </v-radio-group>
          </v-card-text>

          <v-divider></v-divider>

          <v-card-actions>
            <v-btn text="Close" @click="isActive.value = false"></v-btn>

            <v-spacer></v-spacer>

            <v-btn
              color="surface-variant"
              text="Save"
              variant="flat"
              @click="isActive.value = false"
            ></v-btn>
          </v-card-actions>
        </v-card>
      </template>
    </v-dialog>
  </div>
</template> -->
