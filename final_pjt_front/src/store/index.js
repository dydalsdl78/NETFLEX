import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username: '',
    movieRating: []
  },
  getters: {
    transferUsername: function (state) {
      return state.username
    }
  },
  mutations: {
    USERNAME_SAVE: function (state, username) {
      state.username = username
    },
    TRANSFER_RATING: function (state, movieRating) {
      // 같은 값이 없을 때는 그냥추가
      state.movieRating.push(movieRating)

    }
  },
  actions: {
    usernameSave: function (context, username) {
      context.commit('USERNAME_SAVE', username)
    },
    transferRating: function (context, movieRating) {
      context.commit('TRANSFER_RATING', movieRating)
    }
  },
})
