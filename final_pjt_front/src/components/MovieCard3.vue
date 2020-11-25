<template>
  <div class="card" style="width: 12rem; background-color: black">
    <img
      :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path"
      class="card-img-top"
      alt="poster"
    />
    <div class="card-body">
      <h5 class="mb-0 card-title font-size-title">{{ movie.title }}</h5>
    </div>
    <div>
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

<style>
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
