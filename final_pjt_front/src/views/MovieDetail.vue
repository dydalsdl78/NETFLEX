<template>
  <div>
    <h2>영화 정보</h2>
    <div class="p-5 d-flex">
      <div class="float-left">
        <img
          :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path"
          class="img-thumbnail ml-5"
          alt="poster"
        />
      </div>
      <div class="container">
        <h2 class="d-flex mb-4">
          {{ movie.title }} ({{ movie.original_title }})
        </h2>
        <div class="d-flex mb-4">
          <h5>{{ movie.release_date }} |</h5>
          <!-- <h5 v-for="(name, idx) in genreName" :key="idx">{{ name.name }}</h5> -->
          <h5 v-for="(genre_id, idx) in movie.genre_ids" :key="idx">
            <span> {{ genre_id.name }}, </span>
          </h5>
        </div>
        <div class="d-flex mb-4">
          <div class="pr-3">
            <span class="d-flex justify-content-center">성인</span>
            <i v-if="movie.adult"
              ><font-awesome-icon :icon="faCheck" size="3x"
            /></i>
            <i v-else><font-awesome-icon :icon="faTimesCircle" size="3x" /></i>
          </div>
          <div>
            <span class="d-flex justify-content-center">예고편</span>
            <i v-if="movie.video"
              ><font-awesome-icon :icon="faCheck" size="3x"
            /></i>
            <i v-else><font-awesome-icon :icon="faTimesCircle" size="3x" /></i>
          </div>
        </div>
        <h5 class="mt-3">
          {{ movie.overview }}
        </h5>
      </div>
    </div>
    <hr />
    <div class="d-flex justify-content-around">
      <div>
        <h2 class="mb-5 d-flex justify-content-center">
          좋아요 {{ movie.vote_count }}
        </h2>
        <i><font-awesome-icon :icon="faHeart" size="6x" /></i>
      </div>
      <div>
        <h2 class="mb-5 d-flex justify-content-center">
          인기도 {{ movie.popularity }}
        </h2>
        <i><font-awesome-icon :icon="faHeart" size="6x" /></i>
      </div>
      <div>
        <h2 class="mb-5 d-flex justify-content-center">
          평점 {{ movie.vote_average }}
        </h2>
        <i><font-awesome-icon :icon="faHeart" size="6x" /></i>
      </div>
    </div>
    <hr />
    <div class="d-flex justify-content-around">
      <div>
        <h3 class="m-4">유사한 장르</h3>
        <div class="container-fluid">
          <div class="row justify-content-center mb-5">
            <MovieRecommendGenre
              v-for="(recommend_movie, idx) in recommend_Genre"
              :key="idx"
              :recommend_movie="recommend_movie"
            />
          </div>
        </div>
      </div>
      <div>
        <h3 class="m-4">유사한 줄거리</h3>
        <div class="container-fluid">
          <div class="row justify-content-center mb-5">
            <MovieRecommendOverview
              v-for="(recommend_movie, idx) in recommend_Overview"
              :key="idx"
              :recommend_movie="recommend_movie"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faHeart } from "@fortawesome/free-regular-svg-icons";
import { faCheck } from "@fortawesome/free-solid-svg-icons";
import { faTimesCircle } from "@fortawesome/free-solid-svg-icons";
import MovieRecommendGenre from "@/components/MovieRecommendGenre";
import MovieRecommendOverview from "@/components/MovieRecommendOverview";
import axios from "axios";

export default {
  name: "MovieDetail",
  components: {
    MovieRecommendGenre,
    MovieRecommendOverview,
    FontAwesomeIcon,
  },
  props: {
    movie: Object,
  },
  data: function () {
    return {
      faHeart,
      faCheck,
      faTimesCircle,
      recommend_Genre: [],
      recommend_Overview: [],
      genreName: [],
    };
  },
  methods: {
    getRecommendedGenre: function () {
      const movie_title = {
        movie_title: this.movie.title,
      };

      axios
        .post("http://127.0.0.1:8000/movies/genre/", movie_title)
        .then((res) => {
          console.log(res.data);
          this.recommend_Genre = res.data;
        });
    },
    getRecommendedOverwiew: function () {
      const movie_title = {
        movie_title: this.movie.title,
      };

      axios
        .post("http://127.0.0.1:8000/movies/overview/", movie_title)
        .then((res) => {
          console.log(res.data);
          this.recommend_Overview = res.data;
        });
    },
    //   getGenre: function () {
    //     const genres = {
    //       genres: this.movie.genre_ids,
    //     };

    //     axios
    //       .post("http://127.0.0.1:8000/movies/getgenre/", genres)
    //       .then((res) => {
    //         this.genreName = res.data;
    //       });
    //   },
  },
  created() {
    this.getRecommendedGenre();
    this.getRecommendedOverwiew();
    // this.getGenre();
  },
};
</script>

<style>
</style>