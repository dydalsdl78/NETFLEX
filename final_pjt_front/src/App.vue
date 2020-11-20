<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">TQDB</a>
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
              <router-link class="nav-link" :to="{ name: 'Home' }">
                Home
              </router-link>
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
              <router-link class="nav-link" :to="{ name: 'Recommendation' }"
                >Recommendation</router-link
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

    <noscript>
      <strong
        >We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work
        properly without JavaScript enabled. Please enable it to
        continue.</strong
      >
    </noscript>
    <div id="app"></div>

    <button class="chatbox-open">
      <i class="fa fa-comment fa-2x" aria-hidden="true"></i>
    </button>
    <button class="chatbox-close">
      <i class="fa fa-close fa-2x" aria-hidden="true"></i>
    </button>
    <section class="chatbox-popup">
      <header class="chatbox-popup__header">
        <aside style="flex: 3">
          <i
            class="fa fa-user-circle fa-4x chatbox-popup__avatar"
            aria-hidden="true"
          ></i>
        </aside>
        <aside style="flex: 8">
          <h1>기현용민</h1>
          채팅봇
        </aside>
        <aside style="flex: 1">
          <button class="chatbox-maximize">
            <i class="fa fa-window-maximize" aria-hidden="true"></i>
          </button>
        </aside>
      </header>
      <main id="chatting_box" class="chatbox-popup__main">
        아;;<br />
        화면 스크롤 따라서<br />
        안움직이네ㅋㅋㅋㅋㅋㅋ
      </main>
      <footer class="chatbox-popup__footer">
        <aside style="flex: 1; color: #888; text-align: center">
          <i class="fa fa-camera" aria-hidden="true"></i>
        </aside>
        <aside style="flex: 10">
          <textarea
            id="text"
            type="text"
            placeholder="채팅을 입력하세요"
            autofocus
          ></textarea>
        </aside>
        <aside style="flex: 1; color: #888; text-align: center">
          <i class="fa fa-paper-plane" aria-hidden="true"></i>
        </aside>
      </footer>
    </section>
    <section class="chatbox-panel">
      <header class="chatbox-panel__header">
        <aside style="flex: 3">
          <i
            class="fa fa-user-circle fa-3x chatbox-popup__avatar"
            aria-hidden="true"
          ></i>
        </aside>
        <aside style="flex: 6">
          <h1>Sussanah Austin</h1>
          Agent (Online)
        </aside>
        <aside style="flex: 3; text-align: right">
          <button class="chatbox-minimize">
            <i class="fa fa-window-restore" aria-hidden="true"></i>
          </button>
          <button class="chatbox-panel-close">
            <i class="fa fa-close" aria-hidden="true"></i>
          </button>
        </aside>
      </header>
      <main class="chatbox-panel__main" style="flex: 1">
        We make it simple and seamless for<br />
        bussiness and people to talk to each<br />
        other. Ask us anything.
      </main>
      <footer class="chatbox-panel__footer">
        <aside style="flex: 1; color: #888; text-align: center">
          <i class="fa fa-camera" aria-hidden="true"></i>
        </aside>
        <aside style="flex: 10">
          <textarea
            type="text"
            placeholder="Type your message here..."
            autofocus
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

export default {
  name: "App",
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

// const text = document.querySelector('#text')
// const chatting_box = document.querySelector('#chatting_box')
// axios.post("")
// drf서버로 axios 요청을 보내고 받아와서
// message에 넣고
// const message = document.createElement('p')
// chatting_box.appendChild(message)
</script>


<style>
@import "./assets/chat_css.css";
</style>
