import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ReceiverLogin from '../views/ReceiverLogin.vue'
import SenderLogin from '../views/SenderLogin.vue'
import ProjectsHallView from '../views/ProjectsHallView.vue'
import HistoryView from '../views/HistoryView.vue'
import CreditsView from '../views/CreditsView.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueRouter)
Vue.use(VueAxios, axios)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/receiverlogin',
    name: 'receiverlogin',
    component: ReceiverLogin
  },
  {
    path: '/senderlogin',
    name: 'senderlogin',
    component: SenderLogin
  },
  {
    path: '/projects',
    name: 'projects',
    component: ProjectsHallView
  },
  {
    path: '/history',
    name: 'history',
    component: HistoryView
  },
  {
    path: '/credits',
    name: 'credits',
    component: CreditsView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
