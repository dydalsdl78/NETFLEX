<template>
  <div class="d-flex justify-content-end mt-5">
    <!-- <input @keydown="searchMovie" v-model="search" type="text" /> -->
    <button>
      <i><font-awesome-icon :icon="faSearch" size="1x" /></i>
    </button>
    <span class="ml-2 d-flex justify-content-center">
      <Dropdown
        :options="searchJson"
        v-on:selected="searchSelected"
        :disabled="false"
        :maxItem="20"
        placeholder="영화 제목을 입력하세요"
      >
      </Dropdown>
      <button @click='yeah'></button>
    </span>
  </div>
</template>

<script type="text/javascript" src="node_modules/vuejs/dist/vue.min.js"></script>
<script type="text/javascript" src="node_modules/vue-simple-search-dropdown/dist/vue-simple-search-dropdown.min.js"></script>


<script>
import axios from "axios";
import { faSearch } from "@fortawesome/free-solid-svg-icons";
import Dropdown from "vue-simple-search-dropdown";
import searchJson from "../assets/search.json";

export default {
  name: "Search",
  components: {
    Dropdown,
  },
  props: {
    // movies: Array,
  },
  data: function () {
    return {
      search: "",
      faSearch,
      suggests: [],
      searchJson: searchJson,
    };
  },
  methods: {
    searchSelected: function (event) {
      console.log(event.id)
    },
    // searchMovie: function () {
    //   console.log("?");
    //   for (const idx in this.movies) {
    //     this.suggests.push({ id: idx, name: this.movies[idx].title });
    //   }
    //   const API_KEY = "d7a0f6399832ff632e1b02fc2afb5d21";
    //   axios
    //     .get(
    //       `https://api.themoviedb.org/3/search/movie?api_key=${API_KEY}&language=kr-KR&query=${this.search}`
    //     )
    //     .then((res) => {
    //       console.log(res.data["results"]);
    //       for (const idx in res.data["results"]) {
    //         this.suggests.push({
    //           id: idx,
    //           name: res.data["results"][idx].title,
    //         });
    //         console.log(this.suggests);
    //       }
    //       // this.suggests = res.data["results"];
    //     })
    //     .catch((err) => {
    //       console.log(err, "일치하는 영화가 없습니다.");
    //     });
    // },
  },
  // created: function () {
  //   for (const idx in this.movies) {
  //     this.suggests.push(movies[idx].title);
  //     console.log(this.suggests);
  //   }
  // },
};
</script>

<style>
</style>