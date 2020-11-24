<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top">
      <router-link class="navbar-brand" :to="{ name: 'Home' }"
        >TQDB</router-link
      >
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
          <!-- 로그인 했을 때 -->
          <span v-if="login" class="form-inline">
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
    <router-view @login="login = true" />

    <!-- chatting box -->
    <noscript>
      <strong></strong>
    </noscript>
    <div id="app"></div>

    <button class="chatbox-open">
      <i
        ><font-awesome-icon :icon="faCommentDots" size="2x" aria-hidden="true"
      /></i>
    </button>
    <button class="chatbox-close">
      <i><font-awesome-icon :icon="faTimes" size="2x" aria-hidden="true" /></i>
    </button>
    <section class="chatbox-popup">
      <header class="chatbox-popup__header">
        <aside style="flex: 1">
          <i
            ><font-awesome-icon
              :icon="faUserCircle"
              size="3x"
              aria-hidden="true"
          /></i>
        </aside>
        <aside style="flex: 1">
          <h1>채팅봇</h1>
        </aside>
        <aside style="flex: 1">
          <button class="chatbox-maximize">
            <i
              ><font-awesome-icon
                :icon="faWindowMaximize"
                size="2x"
                aria-hidden="true"
            /></i>
            <!-- <i class="fa fa-window-maximize" aria-hidden="true"></i> -->
          </button>
        </aside>
      </header>
      <main id="chatting_box" class="chatbox-popup__main">
        <p v-if="chattings">{{ chattings }}</p>
        <p v-else>사이트에 궁금한 점이 있으시면 물어봐주세요</p>
      </main>
      <footer class="chatbox-popup__footer">
        <aside style="flex: 1; color: #888; text-align: center">
          <i class="fa fa-camera" aria-hidden="true"></i>
        </aside>
        <aside style="flex: 10">
          <textarea
            v-model="query"
            id="text"
            type="text"
            placeholder="채팅을 입력하세요"
            autofocus
            @keypress.enter="transferQuery"
          ></textarea>
        </aside>
        <aside style="flex: 1; color: #888; text-align: center">
          <i class="fa fa-paper-plane" aria-hidden="true"></i>
        </aside>
      </footer>
    </section>
    <section class="chatbox-panel">
      <header class="chatbox-panel__header">
        <aside style="flex: 1">
          <i
            ><font-awesome-icon
              :icon="faUserCircle"
              size="3x"
              aria-hidden="true"
              class="chatbox-popup__avatar"
          /></i>
          <!-- <i
            class="fa fa-user-circle fa-3x chatbox-popup__avatar"
            aria-hidden="true"
          ></i> -->
        </aside>
        <aside style="flex: 1">
          <h1>채팅봇</h1>
        </aside>
        <aside style="flex: 1; text-align: right">
          <button class="chatbox-minimize">
            <i
              ><font-awesome-icon
                :icon="faWindowRestore"
                size="2x"
                aria-hidden="true"
            /></i>
          </button>
          <button class="chatbox-panel-close">
            <i
              ><font-awesome-icon
                :icon="faWindowClose"
                size="2x"
                aria-hidden="true"
            /></i>
          </button>
        </aside>
      </header>
      <main class="chatbox-panel__main" style="flex: 1">
        <div v-for="(message, idx) in Messages" :key="idx">
          <p class="text-left bot-message" v-if="idx % 2">봇 : {{ message }}</p>
          <p class="text-right my-message" v-else>나 : {{ message }}</p>
        </div>
      </main>
      <footer class="chatbox-panel__footer">
        <aside style="flex: 1; color: #888; text-align: center">
          <i class="fa fa-camera" aria-hidden="true"></i>
        </aside>
        <aside style="flex: 10">
          <textarea
            v-model="query"
            type="text"
            placeholder="채팅을 입력하세요!"
            autofocus
            @keypress.enter="transferQuery"
          ></textarea>
        </aside>
        <aside style="flex: 1; color: #888; text-align: center">
          <i class="fa fa-paper-plane" aria-hidden="true"></i>
        </aside>
      </footer>
    </section>
  </div>
</template>

<script src="path/jquery-3.3.1.min.js"></script>
<script src="//code.jquery.com/jquery-3.3.1.min.js"></script>

<script>
import jQuery from "jquery";
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faWindowMaximize } from "@fortawesome/free-solid-svg-icons";
import { faUserCircle } from "@fortawesome/free-solid-svg-icons";
import { faWindowClose } from "@fortawesome/free-solid-svg-icons";
import { faWindowRestore } from "@fortawesome/free-solid-svg-icons";
import { faTimes } from "@fortawesome/free-solid-svg-icons";
import { faCommentDots } from "@fortawesome/free-solid-svg-icons";

export default {
  name: "App",
  components: {
    FontAwesomeIcon,
  },
  data: function () {
    return {
      login: false,
      query: "",
      chattings: "",
      Messages: [],
      faWindowMaximize,
      faUserCircle,
      faWindowClose,
      faWindowRestore,
      faTimes,
      faCommentDots,
    };
  },
  methods: {
    logout: function () {
      localStorage.removeItem("jwt");
      this.login = false;
      this.$router.push({ name: "Login" });
    },
    transferQuery: function () {
      const query = {
        query: this.query,
      };

      axios
        .post("http://127.0.0.1:8000/movies/pingpong/", query)
        .then((res) => {
          // this.chattings.push(this.query);
          this.Messages.push(this.query);
          this.chattings = res.data;
          this.Messages.push(this.chattings);
          this.query = "";
          console.log(res.data);
        });
    },
  },
  created: function () {
    const token = localStorage.getItem("jwt");

    if (token) {
      this.login = true;
    }
  },
};

const chatbox = jQuery.noConflict();

chatbox(() => {
  chatbox(".chatbox-open").click(() =>
    chatbox(".chatbox-popup, .chatbox-close").fadeIn()
  );

  chatbox(".chatbox-close").click(() =>
    chatbox(".chatbox-popup, .chatbox-close").fadeOut()
  );

  chatbox(".chatbox-maximize").click(() => {
    chatbox(".chatbox-popup, .chatbox-open, .chatbox-close").fadeOut();
    chatbox(".chatbox-panel").fadeIn();
    chatbox(".chatbox-panel").css({ display: "flex" });
  });

  chatbox(".chatbox-minimize").click(() => {
    chatbox(".chatbox-panel").fadeOut();
    chatbox(".chatbox-popup, .chatbox-open, .chatbox-close").fadeIn();
  });

  chatbox(".chatbox-panel-close").click(() => {
    chatbox(".chatbox-panel").fadeOut();
    chatbox(".chatbox-open").fadeIn();
  });
});


</script>


<style scoped>
@import "./assets/chat_css.css";
</style>
