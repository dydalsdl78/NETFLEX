<template>
  <div>
    <h2>Singup</h2>
    <div>
      <label for="username">사용자 이름: </label>
      <input
        placeholder="영문으로 입력하세요"
        type="text"
        id="username"
        v-model="credentials.username"
      />
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="text" id="password" v-model="credentials.password" />
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input
        type="text"
        id="passwordConfirmation"
        v-model="credentials.passwordConfirmation"
        @keypress.enter="signup"
      />
    </div>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Signup",
  data: function () {
    return {
      credentials: {
        username: "",
        password: "",
        passwordConfirmation: "",
      },
    };
  },
  methods: {
    signup: function () {
      axios
        .post("http://127.0.0.1:8000/accounts/signup/", this.credentials)
        .then((res) => {
          console.log(res);
          this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
body {
  position: relative;
  z-index: 1;
}

body:after {
  background-image: url("../../src/assets/background.jpg");
  top: 0;
  left: 0;
  position: absolute;
  background-size: 100%;
  opacity: 0.5 !important;
  filter: alpha(opacity=50);
  z-index: -1;
  content: "";
  width: 100%;
  height: 100%;
}
</style>