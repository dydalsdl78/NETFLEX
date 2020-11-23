<template>
  <div>
    <h2>장르 유사도 및 가중평점이 가장 높은 추천</h2>
    <br />
    <input
      @keypress.enter="getRecommendedMovies"
      v-model="movie_title"
      type="text"
    />
    <button @click="getRecommendedMovies">get</button>
    <br />
    <!-- <ul v-for="(recommend_movie, idx) in recommend_movies" :key="idx"> -->
    <!-- <p>{{ recommend_movie.title }}</p> -->
    <br />
    <div class="container-fluid">
      <div class="row justify-content-center">
        <MovieRecommend
          v-for="(recommend_movie, idx) in recommend_movies"
          :key="idx"
          :recommend_movie="recommend_movie"
        />
      </div>
    </div>
    <!-- </ul> -->
  </div>
</template>

<script>
import axios from "axios";
import MovieRecommend from "@/components/MovieRecommend";

export default {
  name: "Recommendation",
  components: {
    MovieRecommend,
  },
  data: function () {
    return {
      movie_title: "",
      recommend_movies: [],
    };
  },
  methods: {
    getRecommendedMovies: function () {
      const movie_title = {
        movie_title: this.movie_title,
      };

      axios
        .post("http://127.0.0.1:8000/movies/recommend/", movie_title)
        .then((res) => {
          console.log(res.data);
          this.recommend_movies = res.data;
        });
    },
  },
};
</script>

<style>
</style>