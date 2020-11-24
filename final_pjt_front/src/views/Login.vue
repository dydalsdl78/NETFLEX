<template>
  <div class="container">
    <form class="mt-5 form-signin">
      <img
        class="mb-4"
        src="https://s3.ap-northeast-2.amazonaws.com/elasticbeanstalk-ap-northeast-2-176213403491/media/magazine_img/magazine_283/5-2-%EC%8D%B8%EB%84%A4%EC%9D%BC.jpg"
        alt=""
        width="72"
        height="72"
      />
      <h1 class="h3 mb-3 font-weight-normal">Please Log in</h1>
      <label for="username" class="sr-only"></label>
      <input
        v-model="credentials.username"
        type="text"
        id="username"
        class="m-auto form-control"
        placeholder="영문 아이디"
        required=""
        autofocus=""
        maxlength="10"
        style="width: 300px"
      />
      <label for="inputPassword" class="sr-only"></label>
      <input
        v-model="credentials.password"
        @keypress.enter="login"
        type="password"
        id="inputPassword"
        class="m-auto form-control"
        placeholder="비밀번호"
        required=""
        minlength="10"
        style="width: 300px"
      />
      <div class="checkbox mt-2">
        <label>
          <input type="checkbox" value="remember-me" /> 아이디 저장
        </label>
      </div>
      <button
        @click="login"
        class="m-auto btn btn-lg btn-primary btn-block"
        type="submit"
        style="width: 300px"
      >
        Sign in
      </button>
      <p class="mt-3">다른 방법으로 로그인하기</p>
      <div class="d-flex justify-content-around">
        <div class="d-flex justify-content-around" style="width: 300px">
          <span class="d-inline">
            <img
              src="https://www.flaticon.com/svg/static/icons/svg/270/270799.svg"
              alt=""
              width="40"
              height="40"
            />
          </span>
          <span class="d-inline">
            <img
              src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile21.uf.tistory.com%2Fimage%2F236A893A57C3AA6629BF4F"
              alt=""
              width="40"
              height="40"
            />
          </span>
          <span class="d-inline">
            <img
              src="https://t1.daumcdn.net/cfile/tistory/2368144B56FFF8620A"
              alt=""
              width="40"
              height="40"
            />
          </span>
          <span class="d-inline">
            <img
              src="https://www.flaticon.com/svg/static/icons/svg/174/174848.svg"
              alt=""
              width="40"
              height="40"
            />
          </span>
          <span class="d-inline">
            <img
              src="https://cdn2.iconfinder.com/data/icons/metro-uinvert-dock/256/Twitter_NEW.png"
              alt=""
              width="40"
              height="40"
            />
          </span>
        </div>
      </div>

      <p class="mt-5 mb-3 text-muted">© 2020</p>
    </form>
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