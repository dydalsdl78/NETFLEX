<template>
  <div>
    <h2>mypage</h2>
    <h4>id</h4>
    <h2 @click="test">평점 매긴 영화</h2>
    <p v-for="(movieRating, idx) in movieRatings" :key="idx">
      {{ movieRating.movie.title }}
      {{ movieRating.rating }}
    </p>
    <h2>리뷰 작성한 영화</h2>
    <h2>작성한 리뷰 리스트</h2>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: "Mypage",
  components: {},
  data: function () {
    return {
      movieRatings: [],
    };
  },
  methods: {
    test: function () {
      this.movieRatings = this.$store.state.movieRating;
    },
  },
  created() {
    this.test();
  },
};
</script>

<style>
</style>