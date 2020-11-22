<template>
  <div>
    <h2>Login</h2>
    <div>
      <label for="username">사용자 이름: </label>
      <input
        placeholder="영문입력하세요"
        type="text"
        id="username"
        v-model="credentials.username"
      />
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input
        type="text"
        id="password"
        v-model="credentials.password"
        @keypress.enter="login"
      />
    </div>
    <button @click="login">login</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data: function () {
    return {
      credentials: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    login: function () {
      const username = this.credentials.username;
      // username 데이터를 전송
      this.$store.dispatch("usernameSave", username);
      axios
        .post(
          "http://127.0.0.1:8000/accounts/api-token-auth/",
          this.credentials
        )
        .then((res) => {
          console.log(this.$store.state.username);
          // jwt 토큰 생성
          localStorage.setItem("jwt", res.data.token);
          this.$emit("login");
          this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // 여기서 vuex써서 dispatch로 username을 보내고 actions, mutaions 차례로 state에 username을 저장한다.
    // 그리고 recommend를 누를 때 $store.state로 username을 받아 url에 같이 요청한다.
  },
};
</script>

<style>
</style>