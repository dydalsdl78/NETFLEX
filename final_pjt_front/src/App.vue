<template>
  <div id="app">
    <nav
      class="navbar navbar-expand-lg sticky-top zindex"
      style="color: white; background-color: black"
    >
      <router-link class="navbar-brand" :to="{ name: 'Home' }">
        <img
          src="./assets/netflex(red).png"
          height="80"
          class="d-inline-block align-top"
          alt=""
        />
      </router-link>
      <router-link
        style="color: white"
        v-if="login"
        :to="{
          name: 'Mypage',
        }"
        >{{ this.username }} 님 반갑습니다!
      </router-link>

      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
          <!-- 로그인 했을 때 -->
          <span v-if="login" class="form-inline">
            <li class="nav-item">
              <Search class="mb-5 mr-3" />
            </li>
            <li class="nav-item">
              <router-link class="nav-link" @click.native="logout" to="#"
                >Logout</router-link
              >
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'Community' }"
                >Community</router-link
              >
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'Mypage' }"
                >Mypage</router-link
              >
            </li>
          </span>

          <!-- 로그인 안 했을 때 -->
          <span v-else class="form-inline">
            <li class="nav-item">
              <Search class="mb-5 mr-3" />
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'Home' }">
                Home
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'Login' }"
                >Log in
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'Signup' }"
                >Sign up</router-link
              >
            </li>
          </span>
        </ul>
      </div>
    </nav>
    <div class="loader">
      <ChatBot />
    </div>
    <router-view @login="login = true" />
    <div class="mb-5 mt-5"></div>
    <br />
    <br />
    <MovieFooter />
  </div>
</template>


<script>
import ChatBot from "@/components/ChatBot";
import MovieFooter from "@/components/MovieFooter";
import Search from "@/components/Search";
import axios from "axios";

export default {
  name: "App",
  components: {
    ChatBot,
    MovieFooter,
    Search,
  },
  data: function () {
    return {
      login: false,
      username: "",
    };
  },
  methods: {
    logout: function () {
      localStorage.removeItem("jwt");
      this.login = false;
      this.$router.replace({ name: "Login" });
    },
    setToken: function () {
      const token = localStorage.getItem("jwt");
      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },
    getUsername: function () {
      const config = this.setToken();
      axios
        .get("http://127.0.0.1:8000/accounts/username/", config)
        .then((res) => {
          console.log(res.data);
          this.username = res.data.username;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created: function () {
    this.getUsername();
    document.title = "NETFLEX";
    const token = localStorage.getItem("jwt");

    if (token) {
      this.login = true;
    }
  },
  watch: {
    username: function () {
      this.getUsername();
    },
  },
};
</script>


<style>
@import "./assets/chat_css.css";

@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap");

#app {
  font-family: "Noto Sans KR", sans-serif;
}

.loader {
  z-index: 1000;
}

.zindex {
  z-index: 100;
}

#app {
  background-color: black;
  color: white;
}
nav .navbar-nav li a {
  color: white;
}
</style>
