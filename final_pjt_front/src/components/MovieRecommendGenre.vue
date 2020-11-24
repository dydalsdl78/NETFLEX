<template>
  <div class="card" style="width: 150px; height: 330px">
    <!-- <div class="card" style="width: 15rem"> -->
    <img
      :src="'https://image.tmdb.org/t/p/w300' + recommend_movie.poster_path"
      class="card-img-top"
      alt="poster"
    />
    <div class="card-body">
      <h5 class="card-title">{{ recommend_movie.title }}</h5>
    </div>
    <div>
      <router-link
        v-if="login"
        class="nav-link"
        :to="{
          name: '',
          params: {
            recommend_movie: recommend_movie,
            url: recommend_movie.title,
          },
        }"
        >영화 정보 보기
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieRecommendGenre",
  props: {
    recommend_movie: Object,
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