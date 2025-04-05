<template>
  <v-infinite-scroll :height="300" :items="items" @load="load">
    <template v-for="(item, index) in items" :key="item">
      <div :class="['pa-2', index % 2 === 0 ? 'bg-grey-lighten-2' : '']">
        Item number #{{ item }}
      </div>
    </template>
  </v-infinite-scroll>
</template>
<script setup lang="ts">
import { ref } from 'vue'
import {
  creators_response_creator,
  creators_request_opts,
  creators_response,
} from '../../models/creators_endpoint'
import type { CreatorsResponse, CreatorsRequestOpts, Creator } from '../../models/creators_endpoint'
import ky from 'ky'
import { type } from 'arktype'

const params = ref<CreatorsRequestOpts>({
  page: 1,
  limit: 20,
  query: '',
})
const creators: Array<Creator> = []

type DoneFunction = (status: 'ok' | 'empty' | 'loading' | 'error') => void
interface OnLoad {
  (done: DoneFunction): void
}
async function load(param: OnLoad) {
  const res = await ky.get('https://civitai.com/api/v1/creators', {
    searchParams: params.value,
  })
}

async function civitai_api_creators(params: CreatorsRequestOpts) {
  const res = await ky.get('https://civitai.com/api/v1/creators', {
    searchParams: params,
  })

  if (res.ok) {
    const data = await res.json()
    const out = creators_response(data)
    if (out instanceof type.errors) {
      // hover out.summary to see validation errors
      console.error(out.summary)
    } else {
      // hover out to see your validated data
      console.log(`Hello, ${out.name}`)
    }
  } else {
    throw new Error('Failed to fetch creators')
  }
}
</script>
