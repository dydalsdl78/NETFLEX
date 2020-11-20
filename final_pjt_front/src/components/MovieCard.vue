<template>
<<<<<<< HEAD
<div class="card" style="width: 18rem;">   
           
    <img :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" class="card-img-top" alt="poster">
    <div class="card-body">
    <h5 class="card-title">{{movie.title}}</h5>
    </div>
    <div>
        <router-link class="nav-link" :to="{ name: 'ReviewCreate' }">리뷰쓰기 </router-link>

    </div>

</div>
</template>

<script>
import axios from 'axios'
export default {
    name:'MovieCard',
    props: {
        movie:Object,
    },
    methods :{
        createReview:function(){
            const movieItem = {
                movie: this.movie
            }
        

        axios.post('http://127.0.0.1:8000/movies/reviews', movieItem)
        .then((res) => {
            console.log(res)
        })
        .catch((err) =>{
            console.log(err)
        })
    }}


}
=======
  <div class="card" style="width: 18rem">
    <img
      :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path"
      class="card-img-top"
      alt="poster"
    />
    <div class="card-body">
      <h5 class="card-title">{{ movie.title }}</h5>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCard",
  props: {
    movie: Object,
  },
};
>>>>>>> a3e190f9e98f3b6ebbbb27c341909d9c6724d037
</script>

<style>
</style>
