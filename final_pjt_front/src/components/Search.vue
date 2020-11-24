<template>
  <div>
    <h2>검색</h2>
    <!-- <input @keydown="searchMovie" v-model="search" type="text" /> -->
    <div class="d-flex justify-content-center">
      <i><font-awesome-icon :icon="faSearch" size="1x" /></i>
      <p class="d-flex justify-content-center"></p>

      <vue-autosuggest
        :suggestions="[
          {
            data: suggests,
          },
        ]"
        :input-props="{
          id: 'autosuggest__input',
          placeholder: 'Do you feel lucky, punk?',
        }"
        @input="onInputChange"
        @selected="selectHandler"
        @click="clickHandler"
      >
        <template slot-scope="{ suggestion }">
          <span class="my-suggestion-item">{{ suggestion.item }}</span>
        </template>
      </vue-autosuggest>

      <button @click="searchMovie">search</button>
    </div>
  </div>
</template>

<script type="text/javascript" src="node_modules/vuejs/dist/vue.min.js"></script>
<script type="text/javascript" src="node_modules/vue-simple-search-dropdown/dist/vue-simple-search-dropdown.min.js"></script>
<script>
import axios from "axios";
import { faSearch } from "@fortawesome/free-solid-svg-icons";
import { VueAutosuggest } from "vue-autosuggest";

export default {
  name: "Search",
  components: {
    VueAutosuggest,
  },
  props: {
    movies: Array,
  },
  data: function () {
    return {
      search: "",
      faSearch,
      suggests: [],
      selectedAddress: null,
    };
  },
  methods: {
    searchMovie: function () {
      console.log("???");
      for (const idx in this.movies) {
        this.suggests.push({ id: idx, name: this.movies[idx].title });
      }
      // const API_KEY = "d7a0f6399832ff632e1b02fc2afb5d21";
      // axios
      //   .get(
      //     `https://api.themoviedb.org/3/search/movie?api_key=${API_KEY}&language=kr-KR&query=${this.search}`
      //   )
      //   .then((res) => {
      //     console.log(res.data["results"]);
      //     for (const idx in res.data["results"]) {
      //       this.suggests.push({
      //         id: idx,
      //         name: res.data["results"][idx].title,
      //       });
      //       console.log(this.suggests);
      //     }
      //     // this.suggests = res.data["results"];
      //   })
      //   .catch((err) => {
      //     console.log(err, "일치하는 영화가 없습니다.");
      //   });
    },
  },
  // created: function () {
  //   for (const idx in this.movies) {
  //     this.suggests.push({ id: idx, name: this.movies[idx].title });
  //   }
  // },
  // watch: {
  //   movieSearch: function (movie) {
  //     this.searchMovie(movie);
  //   },
  // },
};
</script>

<style>
</style>