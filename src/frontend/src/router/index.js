import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ReceiverLogin from '../views/ReceiverLogin.vue'
import SenderLogin from '../views/SenderLogin.vue'
import ProjectsHallView from '../views/ProjectsHallView.vue'
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
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
