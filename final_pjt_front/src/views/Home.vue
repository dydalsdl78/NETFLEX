<template>
  <div class="container-fluid">
    <div class="row justify-content-center">
      <MovieCard v-for="(movie, idx) in movies" :key="idx" :movie="movie" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import MovieCard from "@/components/MovieCard";
export default {
  name: "Home",
  components: {
    MovieCard,
  },
  data: function () {
    return {
      movies: [],
    };
  },
  methods: {
    getMovieList: function () {
      axios.get("http://127.0.0.1:8000/movies/movielist/").then((res) => {
        // console.log(res.data[0].title)
        this.movies = res.data;
      });
    },
  },
  created() {
    this.getMovieList();
  },
};
</script>
