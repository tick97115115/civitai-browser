<template>
  <v-container style="height: 100vh">
    <v-layout class="rounded rounded-md border" style="height: 100%">
      <v-app-bar title="Application bar">
        <v-btn icon variant="outlined" ref="search_btn">
          <v-icon>mdi-search-web</v-icon>
        </v-btn>
        <!-- @vue-ignore-->
        <v-dialog :activator="search_btn" max-width="340">
          <template v-slot:default="{ isActive }">
            <v-card
              prepend-icon="mdi-variable"
              text="When using a ref, the dialog will bind its listeners to the ref element. This works for any element and custom components."
              title="Ref Activator"
            >
              <template v-slot:actions>
                <!-- <v-btn class="ml-auto" text="Close" @click="isActive.value = false"></v-btn> -->
                <v-container>
                  <v-text-field label="Search Models" v-model="params.query"></v-text-field>
                  <v-row dense>
                    <v-col cols="12" md="8">
                      <v-text-field
                        density="compact"
                        label="APIKEY"
                        v-model="params.token"
                      ></v-text-field
                    ></v-col>
                    <v-col cols="12" md="4"
                      ><v-checkbox
                        density="compact"
                        label="NSFW"
                        v-model="params.nsfw"
                      ></v-checkbox></v-col
                  ></v-row>
                  <v-combobox
                    v-model="params.types"
                    :items="model_type_items"
                    label="Types"
                    chips
                    multiple
                    clearable
                    density="compact"
                  ></v-combobox>
                  <v-row dense>
                    <v-col cols="12" md="4"
                      ><v-text-field
                        density="compact"
                        label="Tag"
                        v-model="params.tag"
                      ></v-text-field
                    ></v-col>
                    <v-col cols="12" md="8"
                      ><v-text-field
                        density="compact"
                        label="Username"
                        v-model="params.username"
                      ></v-text-field
                    ></v-col>
                  </v-row>
                  <v-row dense>
                    <v-col cols="12" md="7"
                      ><v-combobox
                        density="compact"
                        label="Sort"
                        v-model="params.sort"
                        :items="models_sort_items"
                      ></v-combobox
                    ></v-col>
                    <v-col cols="12" md="5"
                      ><v-combobox
                        density="compact"
                        label="Period"
                        v-model="params.period"
                        :items="models_period_items"
                      ></v-combobox
                    ></v-col>
                  </v-row>
                  <v-row dense>
                    <v-col cols="12" md="6">
                      <v-text-field
                        density="compact"
                        label="Page Size"
                        v-model="params.limit"
                      ></v-text-field
                    ></v-col>
                    <v-col cols="12" md="6">
                      <v-text-field
                        density="compact"
                        label="Current Page"
                        v-model="params.page"
                      ></v-text-field
                    ></v-col>
                  </v-row>
                  <v-row justify="space-evenly">
                    <v-btn type="submit">Save</v-btn
                    ><v-btn type="submit" @click="fetch_models">Run</v-btn>
                  </v-row>
                </v-container>
              </template>
            </v-card>
          </template>
        </v-dialog>
      </v-app-bar>

      <v-main class="d-flex align-center justify-center" height="100%">
        <v-container>
          <v-infinite-scroll :items="items" @load="load" height="500">
            <template v-for="(item, index) in items" :key="index">
              <div>{{ item.name }}</div>
            </template> 
          </v-infinite-scroll>
        </v-container>
      </v-main>
    </v-layout></v-container
  >
</template>

<script setup lang="ts">
import { ref } from 'vue'
const search_btn = ref(null)
import { models_response, models_request_opts } from '../models/models_endpoint'
import type { ModelsResponse, ModelsRequestOpts } from '../models/models_endpoint'
import { modelId_response } from '../models/modelId_endpoint'
import type { ModelIdResponse } from '../models/modelId_endpoint'
import ModelsSearchContext from '../components/ModelsSearchContext.vue'
import ky from 'ky'
import { type } from 'arktype'
import {
  model_types,
  models_request_sort,
  models_request_period,
  // ModelsRequestOpts,
} from '../models/baseModels/misc'
import { convert_arktype_enum_to_array } from '../utils/misc'

const tab = ref(null)
const model_type_items = convert_arktype_enum_to_array(model_types)
const models_sort_items = convert_arktype_enum_to_array(models_request_sort)
const models_period_items = convert_arktype_enum_to_array(models_request_period)
const params = ref<ModelsRequestOpts>({})

type InfiniteScrollStatus = 'ok' | 'empty' | 'loading' | 'error'
type InfiniteScrollDoneCallback = (status: InfiniteScrollStatus) => void
type InfiniteScrollLoadParams = {
  done: InfiniteScrollDoneCallback
}

// 响应式数据
const items = ref<ModelIdResponse[]>([])
const nextPage = ref(undefined)

// API请求
async function fetch_models(): Promise<void> {
  const res = await ky.get('https://civitai.com/api/v1/models', {
    // @ts-ignore
    searchParams: params.value,
  })
  if (!res.ok) {
    throw new Error('Failed to fetch models')
  }
  const data = await res.json()
  const out = models_response(data)
  if (out instanceof type.errors) {
    // hover out.summary to see validation errors
    console.error(out.summary)
    throw new Error('Failed to validate models')
  }
  // hover out to see your validated data
  nextPage.value = out.metadata.nextPage ?? ''
  items.value = out.items
}

// 加载更多数据
async function load({ done }: InfiniteScrollLoadParams): Promise<void> {
  try {
    if (nextPage.value === '') {
      console.log('No more pages to load')
      done('empty')
      return
    }
    console.log(nextPage.value)
    const res = await ky.get<ModelsResponse>(nextPage.value)
    if (!res.ok) {
      throw new Error('Failed to fetch models')
    }
    const data = await res.json()
    const out = models_response(data)
    if (out instanceof type.errors) {
      // hover out.summary to see validation errors
      console.error(out.summary)
      throw new Error('Failed to validate models')
    }
    // hover out to see your validated data
    nextPage.value = out.metadata.nextPage ? out.metadata.nextPage : ''
    // items.value.push(...out.items.slice(1)) // 请求数据的下一页第一项和当前页最后一项相同
    // 需要判断是否是同一项
    // 如果是同一项，则不添加
    // 否则添加
    if (out.items[0].id === items.value[items.value.length - 1].id) {
      items.value.push(...out.items.slice(1))
    } else {
      items.value.push(...out.items)
    }
    done('ok')
  } catch (error) {
    console.error('Loading Error:', error)
    done('error')
  }
}
</script>
