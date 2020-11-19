<template>
  <div>
      <h1>Login</h1>
      <div>
          <label for="username">사용자 이름: </label>
          <input type="text" id="username" v-model="credentials.username">
      </div>
      <div>
          <label for="password">비밀번호: </label>
          <input 
            type="text" 
            id="password" 
            v-model="credentials.password"
            @keypress.enter="login">
      </div>
      <button @click="login">login</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Login',
    data: function () {
        return {
            credentials: {
                username: '',
                password: '',
            }
        }
    },
    methods: {
        login: function () {
            axios.post("http://127.0.0.1:8000/accounts/api-token-auth/", this.credentials)
                .then((res) => {
                    localStorage.setItem('jwt', res.data.token)
                    this.$emit('login')
                    this.$router.push({ name: 'Signup' }) // 무비 리스트로 ㄱㄱ
                })
                .catch((err) => {
                    console.log(err)
                })
        }
    }
}
</script>

<style>

</style>