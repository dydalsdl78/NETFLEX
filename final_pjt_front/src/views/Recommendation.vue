<template>
  <div>
    <h1>Recommendation</h1>
    <input
      @keypress.enter="getRecommendedMovies"
      v-model="movie_title"
      type="text"
    />
    <button @click="getRecommendedMovies">get</button>
    <ul v-for="(recommend_movie, idx) in recommend_movies" :key="idx">
      <p>{{ recommend_movie.title }}</p>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Recommendation",
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