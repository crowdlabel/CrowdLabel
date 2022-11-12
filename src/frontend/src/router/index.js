import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import receiverlogin from '@/views/receiverlogin.vue'
import senderlogin from '@/views/senderlogin.vue'
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
    component: receiverlogin
  },
  {
    path: '/senderlogin',
    name: 'senderlogin',
    component: senderlogin
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
