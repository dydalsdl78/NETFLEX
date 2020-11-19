<template>
  <div>
      <h1>Singup</h1>
      <div>
          <label for="username">사용자 이름: </label>
          <input type="text" id="username" v-model="credentials.username">
      </div>
      <div>
          <label for="username">비밀번호: </label>
          <input type="text" id="username" v-model="credentials.password">
      </div>
      <div>
          <label for="username">비밀번호 확인: </label>
          <input 
            type="text" 
            id="username"
            v-model="credentials.passwordConfirmation"
            @keypress.enter="signup"
            >
      </div>
      <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Signup',
    data: function () {
        return {
            credentials: {
                username: '',
                password: '',
                passwordConfirmation: '',
            }
        }
    },
    methods: {
        signup: function () {
            axios.post('http://127.0.0.1:8000/accounts/signup/')
                .then((res) => {
                    console.log(res)
                })
        }
    }
}
</script>

<style>

</style>