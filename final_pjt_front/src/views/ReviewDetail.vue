<template>

  <!-- Page Content -->
  <div class="container">

    <div class="row">

      <!-- Post Content Column -->
      <div class="col">

        <!-- Title -->
        <h2 class="mt-4">{{review.title}} </h2>

        <!-- Author -->
        <p class="lead">
            <router-link class="nav-link d-inline" :to="{name: 'MovieDetail', params: { movie: review.movie, url: review.movie.title },}">{{review.movie.title}}</router-link>에 대한 {{review.user.username}}님의 리뷰입니다.
        </p>

        <hr>

        <!-- Date/Time -->
        <p>Posted on {{review.created_at}}</p>

        <hr>

        <!-- Preview Image -->
        <img class="img-fluid rounded" :src="'https://image.tmdb.org/t/p/w300' + review.movie.poster_path" alt="poster" style="height:200px">

        <hr>

        <!-- Post Content -->
        <p class="lead"> {{review.content}}</p>

        <hr>
        <div class="text-right" v-if="user">
        <router-link class="btn btn-success mr-3" :to="{name: 'ReviewCreate', params: { movie: review.movie, url: review.movie.title, review:review},}">Update </router-link>
        <button class='btn btn-danger' @click="deleteReview">Delete</button>
        <hr>
        </div>
      



        <!-- Single Comment -->
        <div class="media mb-4" v-for="(comment, idx) in comments" :key="idx">
          <img class="d-flex mr-3 rounded-circle" src="http://placehold.it/50x50" alt="">
          <div class="media-body text-left">
            <h5 class="mt-0">{{comment.user.username}}님의 답글</h5>
            {{comment.content}}
          
          </div>
        </div>

        <!-- Comments Form -->
        <div class="card my-4" style="background-color:black">
          <h5 class="card-header text-left" style="background-color:black">Leave a Comment:</h5>
          <div class="card-body">
            <form>
              <div class="form-group">
                <textarea v-model="commentItem.content" class="form-control" rows="3"></textarea>
              </div>

            </form>
                <div class="text-right">
              <button @click="createComment" class="btn btn-primary">Submit</button>
              </div>
          </div>
        </div>



      </div>

      <!-- Sidebar Widgets Column -->
      
    </div>
    <!-- /.row -->

  </div>
  <!-- /.container -->



  
</template>

<script>
import axios from 'axios'

export default {
    name:"ReviewDetail",
    props:{
        review:Object,
    },
    data: function(){
      return{
        user:false,
        comments:[],
        commentItem:{
          content: "",
          review: this.review,
          user:"",
        },
      }
    },
    methods:{
      setToken: function(){
        const token = localStorage.getItem('jwt')
        const config = {
          headers : {
            Authorization : `JWT ${token}`
          }
        }
        return config

      },
      userId:function(){
        const config = this.setToken()
        axios.get('http://127.0.0.1:8000/accounts/username/', config)
        .then((res)=> {
          if(res.data.username === this.review.user.username){
            console.log('match')
            this.user = true
            this.commentItem.user = res.data
          }
        })
        .catch((err)=>{console.log(err)})
      },
      readComment:function(){

        console.log(this.commentItem)
        axios.get('http://127.0.0.1:8000/movies/comment_crud/', {data:{review:this.review}})
        .then((res)=>{
          console.log(res.data)
          this.comments=res.data;
        })
        .catch((err) => {console.log(err)})
      },
      createComment:function(){
        const config = this.setToken()
        console.log(this.commentItem)
        axios.post('http://127.0.0.1:8000/movies/comment_crud/', this.commentItem, config)
        .then((res)=>{
          console.log(res.data)
          this.comments.push(res.data)
        })
        .catch((err)=>{
          console.log(err)
        })
      },
      deleteReview: function(){
        if (confirm('삭제하시겠습니까?')) {
          // Save it!
        console.log(this.review)
        axios.delete("http://127.0.0.1:8000/movies/review_create_list/", {data:this.review})
        .then((res)=>{
          console.log(res)
          console.log('deleted')
          this.$router.push({ name: "Community" });
        })
          
        } else {
          // Do nothing!
          console.log('Thing was not saved to the database.');
        }


      }
    },
    created: function(){
      this.userId()
      this.readComment()
    }

}
</script>

<style>

</style>