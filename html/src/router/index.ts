import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import ModelsView from '../views/civitai/Models.vue'
import CreatorsView from '../views/civitai/Creators.vue'
import TagsView from '../views/civitai/Tags.vue'
import LocalView from '../views/Local.vue'
const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'civitai_models',
    component: ModelsView,
  },
  {
    path: '/creators',
    name: 'civitai_creators',
    component: CreatorsView,
  },
  {
    path: '/tags',
    name: 'civitai_tags',
    component: TagsView,
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
