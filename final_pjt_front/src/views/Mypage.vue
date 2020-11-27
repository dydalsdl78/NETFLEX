<template>
  <div class="container">
    <h2 class="m-5">{{ username }}님 반갑습니다.</h2>
    <i
      ><font-awesome-icon
        :icon="faUserCircle"
        :style="{ color: '#808080' }"
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

    <h2 class="mb-5">작성한 리뷰 리스트</h2>
    <div
      class="media mb-4"
      v-for="(review, idx) in reviews"
      :key="'review' + idx"
    >
      <div class="justify-content-center">
        <router-link
          :to="{
            name: 'MovieDetail',
            params: {
              movie: review.movie,
              url: review.movie.title,
            },
          }"
          ><img
            class="d-flex mr-3"
            :src="'https://image.tmdb.org/t/p/w300' + review.movie.poster_path"
            alt=""
            style="width: 100px; height: 160px"
          />
        </router-link>

        <star-rating
          :increment="0.5"
          :star-size="15"
          :show-rating="false"
          v-model="review.score"
          :read-only="true"
          class="justify-content-center"
        >
        </star-rating>
      </div>
      <div class="ml-5 media-body text-left">
        <h2 class="mt-0 mb-5">{{ review.title }}</h2>
        {{ review.content }}
        <p class="mt-5 text-right info-font-size">
          {{ review.movie.title }}을 보고 {{ review.created_at | slice }}에 남긴
          리뷰
        </p>
      </div>
      <div class="mt-5 toreivew-font-size">
        <router-link
          class="nav-link"
          :to="{
            name: 'ReviewDetail',
            params: { review: review, url: review.title },
          }"
          >보러 가기
        </router-link>
      </div>
    </div>
    <hr class="mb-5 mt-5 bg-light" style="width: 1200px" />

    <h2 class="mb-5">평점 매긴 영화</h2>
    <div class="row d-flex mb-3">
      <div v-for="(movieRating, idx) in movieRatings" :key="idx">
        <router-link
          :to="{
            name: 'MovieDetail',
            params: {
              movie: movieRating.movie,
              url: movieRating.movie.title,
            },
          }"
          ><img
            :src="
              'https://image.tmdb.org/t/p/w300' + movieRating.movie.poster_path
            "
            class="card-img-top"
            alt="poster"
            style="width: 150px; height: 220px"
          />
        </router-link>

        <div class="container" style="width: 180px">
          <div class="mt-2">
            {{ movieRating.movie.title }}
          </div>
          <div>
            <star-rating
              :increment="0.5"
              :star-size="15"
              :show-rating="false"
              :read-only="true"
              v-model="movieRating.rating"
              class="justify-content-center"
            >
            </star-rating>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faUserCircle } from "@fortawesome/free-solid-svg-icons";
import StarRating from "vue-star-rating";

export default {
  name: "Mypage",
  components: {
    FontAwesomeIcon,
    StarRating,
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
  filters: {
    slice: function (origin) {
      return origin.slice(0, 10);
    },
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

.info-font-size {
  font-size: 10px;
}

.toreivew-font-size {
  font-size: 20px;
}
</style>