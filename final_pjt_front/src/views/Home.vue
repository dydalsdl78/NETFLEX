<template>
  <div class="container-fluid">
    <HomeCarousel />
    <h5 class="mt-5 mb-4">현재 상영 영화</h5>
    <div class="container">
      <carousel
        :navigationEnabled="true"
        :perPage="10"
        :scrollPerPage="true"
        :paginationEnabled="false"
      >
        <slide
          v-for="(movie, idx) in cur_movies"
          :key="idx"
          @slideclick="handleSlideClick"
        >
          <MovieCard :movie="movie" />
        </slide>
      </carousel>
    </div>

    <h5 class="mt-5 mb-4">인기 영화</h5>
    <div class="mb-4 container">
      <carousel
        :navigationEnabled="true"
        :perPage="10"
        :scrollPerPage="true"
        :paginationEnabled="false"
      >
        <slide
          v-for="(movie, idx) in pop_movies"
          :key="idx"
          @slideclick="handleSlideClick"
        >
          <MovieCard3 :movie="movie" />
        </slide>
      </carousel>
    </div>

    <h5 class="mt-5 mb-4">개봉 예정 영화</h5>
    <div class="container">
      <carousel
        :navigationEnabled="true"
        :perPage="10"
        :scrollPerPage="true"
        :paginationEnabled="false"
      >
        <slide
          v-for="(movie, idx) in pre_movies"
          :key="idx"
          @slideclick="handleSlideClick"
        >
          <MovieCard2 :movie="movie" />
        </slide>
      </carousel>
      <hr class="mt-3" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import _ from "lodash";
import MovieCard from "@/components/MovieCard";
import MovieCard2 from "@/components/MovieCard2";
import MovieCard3 from "@/components/MovieCard3";
import { Carousel, Slide } from "vue-carousel";
import HomeCarousel from "@/components/HomeCarousel";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "Home",
  components: {
    MovieCard,
    MovieCard2,
    MovieCard3,
    Carousel,
    Slide,
    HomeCarousel,
  },
  data: function () {
    return {
      movies: [],
      cur_movies: [],
      pre_movies: [],
      pop_movies: [],
    };
  },
  methods: {
    getMovieList: function () {
      axios.get(`${SERVER_URL}/movies/movielist/`).then((res) => {
        // console.log(res.data[0].title)
        this.movies = res.data;
        this.cur_movies = _.slice(res.data, 0, 66);
        this.pre_movies = _.slice(res.data, 67, 136);
        this.pop_movies = _.slice(res.data, 137, 200);
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

<style >
.VueCarousel .VueCarousel-navigation-button {
  color: white;
}

.example-slide {
  align-items: center;
  background-color: #666;
  color: #999;
  display: flex;
  font-size: 1.5rem;
  justify-content: center;
  min-height: 10rem;
}
</style>