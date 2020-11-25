<template>
  <div id="app">
    <nav
      class="navbar navbar-expand-lg sticky-top mb-5"
      style="color: white; background-color: transparent"
    >
      <router-link class="navbar-brand" :to="{ name: 'Home' }">
        <img
          src="./assets/ssaflix(white).png"
          height="40"
          class="d-inline-block align-top"
          alt=""
        />
      </router-link>
      <!-- <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button> -->
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
    <hr class="mb-5 mt-0 bg-light" style="width: 1200px" />
    <MovieFooter />
  </div>
</template>


<script>
import ChatBot from "@/components/ChatBot";
import MovieFooter from "@/components/MovieFooter";
import Search from "@/components/Search";

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
    };
  },
  methods: {
    logout: function () {
      localStorage.removeItem("jwt");
      this.login = false;
      this.$router.push({ name: "Login" });
    },
  },
  created: function () {
    const token = localStorage.getItem("jwt");

    if (token) {
      this.login = true;
    }
  },
};
</script>


<style>
@import "./assets/chat_css.css";

.loader {
  z-index: 1000;
}

#app {
  background-color: black;
  color: white;
}
nav .navbar-nav li a {
  color: white;
}
</style>
