<template>
  <div id="app">
    <p>List</p>
    <button @click="getMovieList">getlist</button>
    <ul>
      <p v-for="(movie, idx) in movies" :key="idx"> {{ movie.title }} </p>
    </ul>
  </div>
</template>

<script>
<<<<<<< HEAD
export default {
  
=======
import axios from 'axios'

export default {
  name: 'App',
  data: function () {
    return {
      movies: [],
    }
  },
  methods: {
    getMovieList: function () {
      axios.get("http://127.0.0.1:8000/movies/movielist/")
        .then((res) => {
          // console.log(res.data[0].title)
          this.movies = res.data
        })
    }
  }
>>>>>>> 5b2a61fd84255d1eac405f8fc3e4674094e9ccee
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
