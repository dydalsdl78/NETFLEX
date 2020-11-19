<template>
    <div class="container-fluid">
      <div class="row justify-content-center">
        <MovieCard v-for="(movie, idx) in movies" :key="idx" :movie="movie" />
      </div>
    </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
export default {
    name:"MovieList",
    components:{
        MovieCard,
    }

}
</script>

<style>

</style>