<template>
  <div class="container">
    <div>
      <img
        :src="'https://image.tmdb.org/t/p/w300' + movie.backdrop_path"
        alt="backdrop"
        style="width: 80%"
      />
    </div>
    <div class="row p-5 d-flex">
      <div class="col-12 col-lg">
        <img
          :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path"
          class="img-thumbnail ml-5"
          alt="poster"
        />
      </div>
      <div class="col-12 col-lg">
        <h2 class="d-flex mb-4 justify-content-center">
          {{ movie.title }} ({{ movie.original_title }})
        </h2>
        <div class="d-flex mb-4 justify-content-center">
          <h5>{{ movie.release_date }} |</h5>
          <h5 v-for="(genre_id, idx) in movie.genre_ids" :key="idx">
            <button type="button" class="btn btn-secondary btn-sm ml-1">
              {{ genre_id.name }}
            </button>
          </h5>
        </div>
        <div class="d-flex mb-4 justify-content-center">
          <div class="pr-3">
            <h4 class="d-flex justify-content-center">성인</h4>
            <i v-if="movie.adult"
              ><font-awesome-icon :icon="faCheck" size="2x"
            /></i>
            <i v-else><font-awesome-icon :icon="faTimesCircle" size="2x" /></i>
          </div>
          <div>
            <h4 class="d-flex justify-content-center">예고편</h4>
            <i v-if="movie.video"
              ><font-awesome-icon :icon="faCheck" size="2x"
            /></i>
            <i v-else><font-awesome-icon :icon="faTimesCircle" size="2x" /></i>
          </div>
        </div>
        <h5 class="mt-3">
          {{ movie.overview }}
        </h5>
        <div>
          <router-link
            v-if="login"
            class="nav-link font-size-menus d-inline d-flex justify-content-end"
            :to="{
              name: 'ReviewCreate',
              params: { movie: movie, url: movie.title },
            }"
            >리뷰쓰러 가기
          </router-link>
        </div>
      </div>
    </div>
    <hr />
    <div class="mb-5 d-flex justify-content-around">
      <div>
        <i
          ><font-awesome-icon
            :icon="faHeart"
            size="6x"
            :style="{ color: 'red' }"
        /></i>
        <h2 class="mt-3 mb-4 d-flex justify-content-center">좋아요</h2>
        <h2 class="mt-3 d-flex justify-content-center">
          {{ movie.vote_count }}
        </h2>
      </div>
      <div>
        <i
          ><font-awesome-icon
            :icon="faFire"
            size="6x"
            :style="{ color: 'orange' }"
        /></i>
        <h2 class="mt-3 mb-4 d-flex justify-content-center">인기도</h2>
        <h2 class="mt-3 d-flex justify-content-center">
          {{ movie.popularity }}
        </h2>
      </div>
      <div>
        <i
          ><font-awesome-icon
            :icon="faStar"
            size="6x"
            :style="{ color: 'yellow' }"
        /></i>
        <h2 class="mt-3 mb-4 d-flex justify-content-center">평점</h2>
        <h2 class="mt-3 d-flex justify-content-center">
          {{ movie.vote_average }}
        </h2>
      </div>
    </div>

    <hr />
    <div class="row d-flex justify-content-around">
      <div class="col-12 col-lg">
        <h3 class="m-4">이 영화와 유사한 장르</h3>
        <div class="container-fluid">
          <div class="row justify-content-center mt-5 mb-5">
            <MovieRecommendGenre
              v-for="(recommend_movie, idx) in recommend_Genre"
              :key="idx"
              :recommend_movie="recommend_movie"
            />
          </div>
        </div>
      </div>
      <div class="col-12 col-lg">
        <h3 class="m-4">이 영화와 유사한 줄거리</h3>
        <div class="container-fluid">
          <div class="row justify-content-center mt-5 mb-5">
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
import { faHeart } from "@fortawesome/free-solid-svg-icons";
import { faCheck } from "@fortawesome/free-solid-svg-icons";
import { faFire } from "@fortawesome/free-solid-svg-icons";
import { faStar } from "@fortawesome/free-solid-svg-icons";
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
      faFire,
      faCheck,
      faStar,
      faTimesCircle,
      recommend_Genre: [],
      recommend_Overview: [],
      genreName: [],
      login: false,
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
      axios
        .post("http://127.0.0.1:8000/movies/overview/", {
          movie_title: this.movie.title,
        })
        .then((res) => {
          console.log(res.data);
          this.recommend_Overview = res.data;
        });
    },
  },
  created() {
    this.getRecommendedGenre();
    this.getRecommendedOverwiew();
    const token = localStorage.getItem("jwt");
    if (token) {
      this.login = true;
    }
  },
  watch: {
    movie: function () {
      this.getRecommendedGenre();
      this.getRecommendedOverwiew();
    },
  },
};
</script>

<style>
</style>