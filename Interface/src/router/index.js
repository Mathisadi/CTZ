import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/edition',
      name: 'Edition',
      component: () => import('../views/Edition.vue'),
    },
    {
      path: '/simulation',
      name: 'Simulation',
      component: () => import('../views/Simulation.vue'),
    },
    {
      path: '/lecture',
      name: 'Lecture',
      component: () => import('../views/Lecture.vue'),
    },
    {
      // Pour Vue Router v4 (Vue 3) :
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: () => import('../views/404.vue'),
    }
  ],
})

export default router
