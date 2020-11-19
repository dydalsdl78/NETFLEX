<template>
<div class="card" style="width: 18rem;">


      
           

<img :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" class="card-img-top" alt="poster">
<div class="card-body">
<h5 class="card-title">{{movie.title}}</h5>
</div>



</div>
</template>

<script>

export default {
    name:'MovieCard',
    props: {
        movie:Object,
    }


}
</script>

<style>

</style>
