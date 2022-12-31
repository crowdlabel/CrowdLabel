import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    Authorization: localStorage.getItem('Authorization') ? localStorage.getItem('Authorization') : '',
    TaskID: localStorage.getItem('TaskID') ? localStorage.getItem('TaskID'): '',
    QuestionIndex: localStorage.getItem('QuestionIndex') ? localStorage.getItem('QuestionIndex') : '',
    QuestionList: localStorage.getItem('QuestionList') ? localStorage.getItem('QuestionList') : '',
  },
  getters: {
  },
  mutations: {
      changeLogin (state, value) {
        state.Authorization = value;
        localStorage.setItem('Authorization', value)
      },
      changeTaskID (state, value) {
        state.TaskID = value;
        localStorage.setItem('TaskID', value)
      },
      changeQuestionIndex (state, value) {
        state.QuestionIndex = value;
        localStorage.setItem('QuestionIndex', value)
      },
      changeQuestionList (state, value) {
        state.QuestionList = JSON.stringify(value)
        localStorage.setItem('QuestionList', JSON.stringify(value))
      },
      removeStorage (state) {
        localStorage.removeItem('Authorization');
      },
  },
  actions: {
  },
  modules: {
  }
})
