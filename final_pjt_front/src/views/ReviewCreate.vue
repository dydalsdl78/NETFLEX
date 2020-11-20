<template>

<div class='container'>
<form>
  <div class="form-group">
    <label for="title"> {{movie.title}}의 리뷰 </label>
    <input v-model="movieItem.title" type="text" class="form-control" id="title" placeholder="글 제목">
  </div>

  <div class="form-group">
    <label for="content">리뷰 내용</label>
    <textarea  v-model="movieItem.content" class="form-control" id="content" rows="3"></textarea>
  </div>

  <div class="form-group">
    <label for="score">평점</label>
    <input v-model="movieItem.score" class="form-control" type="number" id="score" min="1" max="10">

  </div>

  <div class="form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">사용자 약관에 동의합니다.</label>
  </div>
  <button @click="createReview" type="submit" class="btn btn-primary">제출</button>
  <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone elsedd.</small>
</form>

<button @click="createReview">sdasd</button>

</div>
  
</template>

<script>
import axios from 'axios'
export default {
  name:'CreateReview',
  props:{
    movie:Object
  },
  data:function(){
    return {
      movieItem :{
        title: "",
        movie: this.movie,
        score: "",
        content: "",
      },
    };
  },
  methods :{
      createReview:function(){
      console.log(this.movieItem)

      axios.post('http://127.0.0.1:8000/movies/reviews/', this.movieItem)
      .then((res) => {
          console.log(res)
      })
      .catch((err) =>{
          console.log(err)
      })
  }} 

}
</script>










<style>

</style>