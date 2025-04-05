import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import ModelsView from '../views/civitai/Models.vue'
import ModelIdView from '../views/civitai/ModelId.vue'
import CreatorsView from '../views/civitai/Creators.vue'
import LocalView from '../views/civitai/Local.vue'
import CivitAIView from '../views/CivitAI.vue'
const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'civitai',
    component: CivitAIView,
  },
  {
    path: '/local',
    name: 'local',
    component: LocalView,
  },
  // {
  //   path: '/local',
  //   name: 'local',
  //   // route level code-splitting
  //   // this generates a separate chunk (About.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import('../views/AboutView.vue'),
  // },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
