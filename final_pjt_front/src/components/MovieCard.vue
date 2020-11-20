<template>
<div class="card" style="width: 18rem;">   
           
    <img :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" class="card-img-top" alt="poster">
    <div class="card-body">
    <h5 class="card-title">{{movie.title}}</h5>
    </div>
    <div>
    <router-link class="nav-link" :to="{ name: 'ReviewCreate', params:{movie:movie, url:movie.title} }">리뷰쓰기 </router-link>

    </div>

</div>
</template>

<script>

export default {
    name:'MovieCard',
    props: {
        movie:Object,
    },



}
</script>

<style>
</style>
