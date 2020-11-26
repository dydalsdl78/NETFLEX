<template>
  <div id="ReviewList" class="container">
    <div class="card mb-3" style="background-color: black">
      <div class="card-header">
        <div class="row">
          <div class="col">Movie</div>
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
          <div class="mr-5 col text-center">
            <router-link
              :to="{
                name: 'MovieDetail',
                params: {
                  movie: review.movie,
                  url: review.movie.title,
                },
              }"
              ><img
                :src="
                  'https://image.tmdb.org/t/p/w300' + review.movie.poster_path
                "
                class="img-thumbnail ml-3"
                alt="poster"
                style="width: 100px"
              />
            </router-link>
          </div>
          <div class="mt-4 col">
            <router-link
              class="nav-link pl-0 pd-4 d-flex justify-content-start"
              :to="{
                name: 'ReviewDetail',
                params: { review: review, url: review.title },
              }"
              >{{ review.title }}
            </router-link>
            <div class="small d-flex justify-content-starts">
              {{ review.movie.title }}에 {{ review.user.username }}님이 작성하신
              리뷰 입니다.
            </div>
          </div>

          <div class="d-none d-md-block col-4">
            <div class="row">
              <div class="mt-5 col">
                {{ review.created_at | slice }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

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
      axios
        .get("http://127.0.0.1:8000/movies/review_create_list/")
        .then((res) => {
          this.reviews = res.data;
        });
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