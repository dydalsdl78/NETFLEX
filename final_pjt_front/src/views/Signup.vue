<template>
  <div class="container" style="width: 300px">
    <form class="mt-5 form-signin">
      <!-- <img
        class="mb-4"
        src="https://s3.ap-northeast-2.amazonaws.com/elasticbeanstalk-ap-northeast-2-176213403491/media/magazine_img/magazine_283/5-2-%EC%8D%B8%EB%84%A4%EC%9D%BC.jpg"
        alt=""
        width="72"
        height="72"
      /> -->
      <h1 class="h3 mb-3 font-weight-normal">회원가입</h1>
      <label for="username" class="sr-only"></label>
      <input
        v-model="credentials.username"
        type="text"
        id="username"
        class="m-auto form-control"
        placeholder="영문 아이디"
        required=""
        autofocus=""
        maxlength=""
        style="width: 300px"
      />
      <label for="inputPassword" class="sr-only"></label>
      <input
        v-model="credentials.password"
        @keypress.enter="signup"
        type="text"
        id="inputPassword"
        class="m-auto form-control"
        placeholder="비밀번호"
        required=""
        minlength=""
        style="width: 300px"
      />
      <label for="passwordConfirmation" class="sr-only"></label>
      <input
        type="text"
        id="passwordConfirmation"
        class="m-auto form-control"
        placeholder="비밀번호 확인"
        required=""
        minlength="10"
        v-model="credentials.passwordConfirmation"
        @keypress.enter="signup"
        style="width: 300px"
      />
      <div class="checkbox mt-2">
        <label for="cb">
          <input id="cb" type="checkbox" value="remember-me" />
          <span class="blurtext"> 아이디 저장 </span>
        </label>
        <br />
        <label for="cb">
          <input id="cb" type="checkbox" value="agreement" />
          <span class="blurtext"> 전체 약관에 동의합니다. </span>
        </label>
        <br />
        <label for="cb">
          <input id="cb" type="checkbox" value="14gte" />
          <span class="blurtext"> 14세 이상입니다. </span>
        </label>
      </div>
      <button
        @click="signup"
        class="m-auto btn btn-lg btn-success btn-block"
        type="submit"
        style="width: 300px"
      >
        Sign in
      </button>
      <p class="mt-3">다른 방법으로 회원가입하기</p>
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

    <!-- <div>
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
  </div> -->
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

<style scoped>
/* body {
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
} */

.blurtext {
  opacity: 0.5;
}

input[id="cb"] + label {
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 2px solid #bcbcbc;
  cursor: pointer;
}

input[id="cb"]:checked + label {
  background-color: #666666;
}
</style>