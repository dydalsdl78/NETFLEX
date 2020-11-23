<template>
  <div>
    <!-- <div class="row justify-content-center"> -->
    <h2 class="mt-5">현재 상영 영화</h2>
    <div class="container">
      <carousel
        :navigationEnabled="true"
        :perPage="5"
        :scrollPerPage="true"
        :paginationEnabled="false"
      >
        <slide
          v-for="(movie, idx) in movies"
          :key="idx"
          @slideclick="handleSlideClick"
        >
          <MovieCard :movie="movie" />
        </slide>
      </carousel>
    </div>

    <h2 class="mt-5">개봉 예정 영화</h2>
    <div class="container">
      <carousel
        :navigationEnabled="true"
        :perPage="5"
        :scrollPerPage="true"
        :paginationEnabled="false"
      >
        <slide
          v-for="(movie, idx) in movies"
          :key="idx"
          @slideclick="handleSlideClick"
        >
          <MovieCard2 :movie="movie" />
        </slide>
      </carousel>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import MovieCard from "@/components/MovieCard";
import MovieCard2 from "@/components/MovieCard2";
import { Carousel, Slide } from "vue-carousel";

export default {
  name: "Home",
  components: {
    MovieCard,
    MovieCard2,
    Carousel,
    Slide,
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
    handleSlideClick: function () {
      console.log("슬라이드 클릭 굿");
    },
  },
  created() {
    this.getMovieList();
  },
};
</script>
