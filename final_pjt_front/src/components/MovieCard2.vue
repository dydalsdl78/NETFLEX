<template>
  <div class="card" style="width: 15rem">
    <img
      :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path"
      class="card-img-top"
      alt="poster"
    />
    <div class="card-body">
      <h5 class="card-title">{{ movie.title }}</h5>
    </div>
    <div>
      <router-link
        v-if="login"
        class="nav-link"
        :to="{
          name: 'ReviewCreate',
          params: { movie: movie, url: movie.title },
        }"
        >리뷰쓰기
      </router-link>
      <router-link
        class="nav-link"
        :to="{
          name: 'MovieDetail',
          params: { movie: movie, url: movie.title },
        }"
        >영화정보
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
</style>
