import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  
}

export default new Vuex.Store({
  state: {
    Authorization: localStorage.getItem('Authorization') ? localStorage.getItem('Authorization') : '',
  },
  getters: {
  },
  mutations: {
      changeLogin (state, value) {
        state.Authorization = value;
        localStorage.setItem('Authorization', value)
      },
      removeStorage (state) {
        localStorage.removeItem('Authorization');
      }
  },
  actions: {
  },
  modules: {
  }
})
