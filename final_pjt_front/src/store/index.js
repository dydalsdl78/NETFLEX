import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username: '',
  },
  getters: {
    transferUsername: function (state) {
      return state.username
    }
  },
  mutations: {
    USERNAME_SAVE: function (state, username) {
      state.username = username
    }
  },
  actions: {
    usernameSave: function (context, username) {
      context.commit('USERNAME_SAVE', username)
    }
  },
})
