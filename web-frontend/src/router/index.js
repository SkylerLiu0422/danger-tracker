import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import BodyIndicator from '@/views/BodyIndicator.vue'
import VoiceRecognition from '@/views/VoiceRecognition.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    redirect:'/body-indicator',
    meta: {
      title: "Danger Tracker"
    },
    children: [
      {
        path: 'body-indicator',
        name: 'body-indicator',
        component: BodyIndicator,
        meta: {
          title: "Body Indicators -- Danger Tracker"
        },
      },
      {
        path: 'voice-recognition',
        name: 'voice-recognition',
        component: VoiceRecognition,
        meta: {
          title: "Voice Recognition -- Danger Tracker"
        },
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})

export default router
