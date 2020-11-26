<template>
  <div id="ReviewList" class="container">
    <div class="card mb-3" style="background-color: black">
      <div class="card-header">
        <div class="row">
          <div class="col">Topics</div>
          <div class="col-4">
            <div class="row">
              <div class="col">작성일</div>
            </div>
          </div>
        </div>
      </div>
      <div class="card-body py-3" v-for="(review, idx) in reviews" :key="idx">
        <div class="row">
          <div class="col text-left">
            <router-link
              class="nav-link"
              :to="{
                name: 'ReviewDetail',
                params: { review: review, url: review.title },
              }"
              >{{ review.title }}
            </router-link>
            <div class="small">
              {{ review.movie.title }}를 보고 {{ review.user.username }}님이
              쓰신 리뷰
            </div>
          </div>
          <div class="d-none d-md-block col-4">
            <div class="row">
              <div class="col">{{ review.created_at | slice }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "ReviewList",
  data: function () {
    return {
      reviews: [],
      movie_titles: [],
      review: [],
    };
  },
  methods: {
    getList: function () {
<<<<<<< HEAD
      axios
        .get("http://127.0.0.1:8000/movies/review_create_list/")
        .then((res) => {
          this.reviews = res.data;
          console.log("getlist 테스트", this.reviews);
        });
=======
      axios.get(`${SERVER_URL}/movies/review_create_list/`).then((res) => {
        this.reviews = res.data;
        console.log("getlist 테스트", this.reviews);
        const reviewComment = {
          reviewComment: this.reviews,
        };
        axios
          .post(`${SERVER_URL}/movies/commentcount/`, reviewComment)
          .then((res) => {
            this.commentCounts = res.data;
            console.log("comment 테스트", this.commentCounts);
          });
      });
>>>>>>> 54f6ea90e7429c75ba5af1fcdba541ac812aaf7d
    },
  },
  created: function () {
    this.getList();
  },
  filters: {
    slice: function (origin) {
      return origin.slice(0, 10);
    },
  },
};
</script>

<style scoped>
#ReviewList {
  background-color: black;
}
.nav-link {
  color: red;
}
.nav-link:hover {
  color: white;
}
</style>