<template>
  <div v-if="errorMessage">
    <v-alert :text="errorMessage" type="error" title="Data Validation Error"></v-alert>
  </div>
  <div v-else>
    {{ modelIdData }}
  </div>
</template>

<script lang="ts" setup>
import { modelId_response } from "../../models/modelId_endpoint";
import { ref } from "vue";
import { type } from "arktype";
type ModelIDResponse = typeof modelId_response.infer

const props = defineProps<{
  modelIdResponse: unknown
}>()

// State for error message
const errorMessage = ref<string | null>(null);
const modelIdData = ref<ModelIDResponse | null>(null);

// Validation function
function validateData(data: unknown): boolean {
  // validation logic here
  const result = modelId_response(data)
  if (result instanceof type.errors) {
    errorMessage.value = result.summary
    modelIdData.value = null
    return false
  } else {
    errorMessage.value = null
    modelIdData.value = result
    return true
  }
}

validateData(props.modelIdResponse)

</script>