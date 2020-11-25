<template>
  <div>
    <h2 class="m-5">{{ username }}님 반갑습니다.</h2>
    <i
      ><font-awesome-icon
        :icon="faUserCircle"
        :style="{ color: '#42b983' }"
        size="10x"
        aria-hidden="true"
    /></i>
    <div class="d-flex justify-content-around mt-5">
      <div class="follow-font-size">팔로워</div>
      <div class="follow-font-size">팔로잉</div>
    </div>
    <div class="d-flex justify-content-around">
      <div class="follow-count-size">135</div>
      <div class="follow-count-size">245</div>
    </div>
    <hr class="mb-5 mt-5 bg-light" style="width: 1200px" />
    <h2>평점 매긴 영화</h2>
    <div class="container row d-flex">
      <div v-for="(movieRating, idx) in movieRatings" :key="idx">
        <img
          :src="
            'https://image.tmdb.org/t/p/w300' + movieRating.movie.poster_path
          "
          class="card-img-top"
          alt="poster"
          style="width: 150px; height: 220px"
        />
        <div class="container" style="width: 180px">
          <div>
            {{ movieRating.movie.title }}
          </div>
          <div>
            {{ movieRating.rating }}
          </div>
        </div>
      </div>
    </div>
    <h2 @click="getUserReview">리뷰 작성한 영화</h2>
    <div class="container row d-flex">
      <div v-for="(review, idx) in reviews" :key="'movie' + idx">
        <img
          :src="'https://image.tmdb.org/t/p/w300' + review.movie.poster_path"
          class="card-img-top"
          alt="poster"
          style="width: 150px; height: 220px"
        />
        <div class="container" style="width: 180px">
          <div>
            {{ review.movie.title }}
          </div>
          <div>
            {{ review.movie.vote_average }}
          </div>
        </div>
      </div>
    </div>
    <h2 @click="getUserReview">작성한 리뷰 리스트</h2>
    <span class="container row d-flex justify-content-around">
      <h4>포스터</h4>
      <h4>영화 제목</h4>
      <h4>리뷰 제목</h4>
      <h4>리뷰 내용</h4>
      <h4>매긴 평점</h4>
    </span>
    <div v-for="(review, idx) in reviews" :key="'review' + idx">
      <span
        class="container row d-flex justify-content-around align-items-center"
      >
        <img
          :src="'https://image.tmdb.org/t/p/w300' + review.movie.poster_path"
          class="card-img-top"
          alt="poster"
          style="width: 100px; height: 160px"
        />
        <div>{{ review.movie.title }}</div>
        <div>{{ review.title }}</div>
        <div>{{ review.content }}</div>
        <div>{{ review.score }}</div>
      </span>
      <br />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faUserCircle } from "@fortawesome/free-solid-svg-icons";

export default {
  name: "Mypage",
  components: {
    FontAwesomeIcon,
  },
  data: function () {
    return {
      movieRatings: [],
      reviews: [],
      username: "",
      faUserCircle,
    };
  },
  methods: {
    ratingMovie: function () {
      this.movieRatings = this.$store.state.movieRating;
    },
    setToken: function () {
      const token = localStorage.getItem("jwt");
      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },
    getUserReview: function () {
      const config = this.setToken();
      axios
        .get("http://127.0.0.1:8000/accounts/userReview/", config)
        .then((res) => {
          console.log(res.data);
          this.reviews = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getUsername: function () {
      const config = this.setToken();
      axios
        .get("http://127.0.0.1:8000/accounts/username/", config)
        .then((res) => {
          console.log(res.data);
          this.username = res.data.username;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.getUsername();
    this.getUserReview();
    this.ratingMovie();
  },
};
</script>

<style>
.follow-font-size {
  font-size: 40px;
}

.follow-count-size {
  font-size: 20px;
}
</style>