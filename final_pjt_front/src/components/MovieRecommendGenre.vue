<template>
  <div id="MovieCard" class="card" style="width: 150px; height: 330px">
    <!-- <div class="card" style="width: 15rem"> -->
    <img
      :src="'https://image.tmdb.org/t/p/w300' + recommend_movie.poster_path"
      class="card-img-top"
      alt="poster"
    />
    <div class="pt-2 card-body">
      <h5 class="card-title font-size-title">
        {{ recommend_movie.title }}
      </h5>
    </div>
    <div class="card-tail">
      <div @click="test" class="container">
        <router-link
          class="nav-link font-size-menus"
          :to="{
            name: '',
            params: {
              movie: recommend_movie,
            },
          }"
          >영화정보
        </router-link>
      </div>
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
  methods: {
    test: function () {
      console.log(this.recommend_movie);
      // this.$router.go(this.$router.currentRoute);
      this.$router.replace({
        name: "",
        params: { movie: this.recommend_movie },
      });
      // .catch((err) => {
      //   console.log(err);
      // });
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
  font-size: 12px;
}
.font-size-menus {
  font-size: 10px;
}
</style>