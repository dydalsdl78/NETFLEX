<template>
  <div id="MovieCard" class="card" style="width: 12rem; backgroud-color: black">
    <button class="content">
      <img
        :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path"
        class="card-img-top"
        alt="poster"
      />

      <div
        class="pb-4 align-items-end content-overlay content-details fadeIn-bottom"
      >
        <h5 class="mt-5">{{ movie.title }}</h5>
        <p>{{ movie.release_date }}</p>
        <div class="average-font-size">{{ movie.vote_average }}</div>
        <star-rating
          :increment="0.5"
          :star-size="30"
          :show-rating="false"
          v-model="rating"
          @rating-selected="setRating"
          class="justify-content-center"
        ></star-rating>
      </div>
    </button>
    <div class="card-body" style="height: 70px">
      <h5 class="card-title font-size-title">{{ movie.title }}</h5>
    </div>
    <div class="card-tail">
      <div class="container">
        <router-link
          class="nav-link font-size-menus d-inline"
          :to="{
            name: 'MovieDetail',
            params: { movie: movie, url: movie.title },
          }"
          >영화정보
        </router-link>
        <router-link
          v-if="login"
          class="nav-link font-size-menus d-inline"
          :to="{
            name: 'ReviewCreate',
            params: { movie: movie, url: movie.title },
          }"
          >리뷰쓰기
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from "vue-star-rating";
export default {
  name: "MovieCard",
  components: {
    StarRating,
  },
  props: {
    movie: Object,
  },
  data: function () {
    return {
      login: false,
      rating: 0,
    };
  },
  methods: {
    setRating: function (rating) {
      this.rating = rating;

      const movieRating = {
        movie: this.movie,
        rating: rating,
      };

      this.$store.dispatch("transferRating", movieRating);
    },
  },
  created: function () {
    const token = localStorage.getItem("jwt");

    if (token) {
      this.login = true;
    }
  },
};
</script>

<style scoped>
#MovieCard {
  background-color: black;
}
.nav-link {
  color: red;
}
.nav-link:hover {
  color: white;
}
.font-size-title {
  font-size: 15px;
}
.font-size-menus {
  font-size: 12px;
}

.content {
  position: relative;
  width: 90%;
  max-width: 400px;
  margin: auto;
  overflow: hidden;
}

.content-overlay {
  background: rgba(0, 0, 0, 0.7);
  position: relative;
  height: 100%;
  width: 100%;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
  opacity: 1;
  -webkit-transition: all 0.4s ease-in-out 0s;
  -moz-transition: all 0.4s ease-in-out 0s;
  transition: all 0.4s ease-in-out 0s;
}

.content-overlay:hover {
  opacity: 0.6;
}

.content-details {
  position: absolute;
  text-align: center;
  padding-left: 1em;
  padding-right: 1em;
  width: 100%;
  top: 50%;
  left: 50%;
  opacity: 0;
  -webkit-transform: translate(-50%, -50%);
  -moz-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  -webkit-transition: all 0.3s ease-in-out 0s;
  -moz-transition: all 0.3s ease-in-out 0s;
  transition: all 0.3s ease-in-out 0s;
}

.content:hover .content-details {
  top: 50%;
  left: 50%;
  opacity: 1;
}

.content-details h3 {
  color: #fff;
  font-weight: 500;
  letter-spacing: 0.15em;
  margin-bottom: 0.5em;
  text-transform: uppercase;
}

.content-details p {
  color: #fff;
  font-size: 0.7em;
}

.fadeIn-bottom {
  top: 70%;
}

.average-font-size {
  font-size: 20px;
}
</style>
