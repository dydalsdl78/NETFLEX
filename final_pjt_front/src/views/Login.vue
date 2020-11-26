<template>
  <div class="wrapper">
    <div class="d-flex justify-content-center">
      <form class="mt-5 form-signin" style="z-index: 100">
        <div>
          <p class="font-weight-normal">로그인</p>
          <p class="password-find">비밀 번호를 잊어버리셨나요?</p>
        </div>
        <label for="username" class="sr-only"></label>
        <input
          v-model="credentials.username"
          type="text"
          id="username"
          class="form-control"
          placeholder="영문 아이디"
          required=""
          autofocus=""
          maxlength="10"
        />
        <label for="inputPassword" class="sr-only"></label>
        <input
          v-model="credentials.password"
          @keypress.enter="login"
          type="password"
          id="inputPassword"
          class="mt-1 form-control"
          placeholder="비밀번호"
          required=""
          minlength="10"
        />
        <div class="checkbox mt-2">
          <label>
            <input type="checkbox" value="remember-me" /> 아이디 저장
          </label>
        </div>
        <button
          @click="login"
          class="m-auto btn btn-lg btn-danger btn-block"
          type="submit"
        >
          로그인
        </button>
        <p class="mt-3">다른 방법으로 로그인하기</p>
        <div class="d-flex justify-content-around">
          <div class="d-flex justify-content-around" style="width: 300px">
            <span class="d-inline">
              <a href="https://www.google.com/" target="_blank">
                <img
                  src="https://www.flaticon.com/svg/static/icons/svg/270/270799.svg"
                  alt=""
                  width="40"
                  height="40"
                />
              </a>
            </span>
            <span class="d-inline">
              <a href="https://www.naver.com/" target="_blank">
                <img
                  src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile21.uf.tistory.com%2Fimage%2F236A893A57C3AA6629BF4F"
                  alt=""
                  width="40"
                  height="40"
                />
              </a>
            </span>
            <span class="d-inline">
              <a
                href="https://www.kakaocorp.com/service/KakaoTalk"
                target="_blank"
              >
                <img
                  src="https://t1.daumcdn.net/cfile/tistory/2368144B56FFF8620A"
                  alt=""
                  width="40"
                  height="40"
                />
              </a>
            </span>
            <span class="d-inline">
              <a href="https://ko-kr.facebook.com/" target="_blank">
                <img
                  src="https://www.flaticon.com/svg/static/icons/svg/174/174848.svg"
                  alt=""
                  width="40"
                  height="40"
                />
              </a>
            </span>
            <span class="d-inline">
              <a href="https://twitter.com/?lang=ko" target="_blank">
                <img
                  src="https://cdn2.iconfinder.com/data/icons/metro-uinvert-dock/256/Twitter_NEW.png"
                  alt=""
                  width="40"
                  height="40"
                />
              </a>
            </span>
          </div>
        </div>
        <p class="mt-5 mb-3 text-muted">© 2020</p>
      </form>
    </div>
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

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");

.password-find {
  font-size: 10px;
}

.wrapper {
  z-index: 1;
  position: relative;
  width: auto;
  height: 600;
  /* border: 1px solid; */
  /* border-radius: 1px; */
}

.wrapper:after {
  width: 100%;
  height: 830px;
  z-index: 10;
  position: absolute;
  top: 0;
  left: 0;
  content: "";
  background-image: url("https://t1.daumcdn.net/cfile/tistory/99713B485DE860D201");
  background-repeat: no-repeat;
  background-position: center;
  background-origin: content-box;
  background-size: 100%;
  opacity: 0.3 !important;
  filter: alpha(opacity=30);
}

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