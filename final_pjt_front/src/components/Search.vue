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
      <button></button>
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
  data: function () {
    return {
      search: "",
      faSearch,
      suggests: [],
      searchJson: searchJson,
      movie: [],
    };
  },
  methods: {
    searchSelected: function (event) {
      const movie_name = event.name;
      axios
        .post('http://127.0.0.1:8000/movies/get_movie/', { name: movie_name })
        .then((res) => {
          console.log("changed");
          const received_movie = res.data;
          this.$router.push({
            name: "MovieDetail",
            params: { url: movie_name, movie: received_movie },
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
</style>