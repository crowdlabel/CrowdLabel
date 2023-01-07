import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Element from "element-ui"
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.prototype.$axios = axios;
Vue.use(Element)
Vue.use(VueAxios, axios)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  data: function(){
    return {
      basePath:  'http://localhost:8000' //'https://api.crowdlabel.org'
    }
  },
  render: h => h(App)
}).$mount('#app')

// axios.interceptors.request.use(
//   config => {
//     if (localStorage.getItem('Authorization')) {
//       config.headers.Authorization = localStorage.getItem('Authorization');
//     }
//     return config;
//   }, error => {
//     return Promise.reject(error);
//   }
// );