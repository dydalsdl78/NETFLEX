<template>
  <div id="MovieCard" class="card" style="width: 12rem; backgroud-color: black">
    <img
      :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path"
      class="card-img-top"
      alt="poster"
    />
    <div class="card-body">
      <h5 class="card-title font-size-title">{{ movie.title }}</h5>
    </div>
    <div class="card-tail">
      <div class="container">
        <router-link
          class="nav-link font-size-menus d-inline"
          :to="{
            name: 'MovieDetail',
            params: { movie: movie, url: movie.title },
          }"
          >영화정보
        </router-link>
        <router-link
          v-if="login"
          class="nav-link font-size-menus d-inline"
          :to="{
            name: 'ReviewCreate',
            params: { movie: movie, url: movie.title },
          }"
          >리뷰쓰기
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCard",
  props: {
    movie: Object,
  },
  data: function () {
    return {
      login: false,
    };
  },
  created: function () {
    const token = localStorage.getItem("jwt");

    if (token) {
      this.login = true;
    }
  },
};
</script>

<style scoped>
#MovieCard {
  background-color: black;
}
.nav-link {
  color: red;
}
.nav-link:hover {
  color: white;
}
.font-size-title {
  font-size: 15px;
}
.font-size-menus {
  font-size: 11px;
}
</style>
