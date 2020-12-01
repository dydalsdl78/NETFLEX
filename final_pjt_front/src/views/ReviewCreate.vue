<template>
  <div class="container">
    <div class="row">
      <div
        class="col-12 col-lg-4 d-flex align-items-center justify-content-center"
      >
        <img
          :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path"
          class="img-thumbnail ml-5"
          style="width: 300px; height: 480px"
          alt="poster"
        />
      </div>
      <div class="col-12 col-lg-8">
        <form>
          <div class="form-group">
            <label for="title"> {{ movie.title }}의 리뷰 </label>
            <input
              v-model="reviewItem.title"
              type="text"
              class="form-control"
              id="title"
              placeholder="리뷰 제목 달아주시고요"
            />
          </div>

          <div class="form-group">
            <label for="score">평점</label>
            <star-rating
              :star-size="30"
              :show-rating="false"
              v-model="reviewItem.score"
              class="justify-content-center"
            >
            </star-rating>
          </div>

          <div class="form-group">
            <label for="content">리뷰 내용</label>
            <textarea
              v-model="reviewItem.content"
              class="form-control"
              id="content"
              rows="12"
              placeholder="리뷰 내용도 달아주세요"
            ></textarea>
          </div>
        </form>
      </div>
    </div>

    <div class="form-check">
      <input type="checkbox" class="form-check-input" id="exampleCheck1" />
      <label class="form-check-label" for="exampleCheck1">
        넷플렉스 이용약관을 확인하였으며, 이에 동의합니다
      </label>
    </div>
    <small id="emailHelp" class="form-text text-muted">
      당신의 개인정보는 소중합니다
    </small>

    <button
      v-if="update"
      @click="updateReview"
      class="btn btn-success mt-3 mb-3"
    >
      수정
    </button>
    <button v-else @click="createReview" class="btn btn-danger mt-3 mb-3">
      등록
    </button>
  </div>
</template>

<script>
import axios from "axios";
import StarRating from "vue-star-rating";

export default {
  name: "CreateReview",
  components: {
    StarRating,
  },
  props: {
    movie: Object,
    review: Object,
  },
  data: function () {
    return {
      reviewItem: {
        title: "",
        movie: this.movie,
        score: "",
        content: "",
        id: "",
      },
      update: false,
    };
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("jwt");
      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },
    createReview: function () {
      const config = this.setToken();
      axios
        .post(
          "http://127.0.0.1:8000/movies/review_create_list/",
          this.reviewItem,
          config
        )
        .then(() => {
          this.$router.push({ name: "Community" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updateReview: function () {
      const config = this.setToken();
      axios
        .put(
          "http://127.0.0.1:8000/movies/review_create_list/",
          this.reviewItem,
          config
        )
        .then(() => {
          this.$router.push({ name: "Community" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updateCreateReview: function () {
      if (this.review) {
        this.reviewItem.title = this.review.title;
        this.reviewItem.score = this.review.score;
        this.reviewItem.content = this.review.content;
        this.reviewItem.id = this.review.id;
        this.update = true;
      }
    },
  },
  created: function () {
    this.updateCreateReview();
    console.log("updatereview");
  },
};
</script>










<style>
</style>