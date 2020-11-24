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
            <router-link class="nav-link" :to="{name: 'MovieDetail', params: { movie: review.movie, url: review.movie.title },}"> {{review.movie.title}} </router-link>에 대한 
          
         {{review.user.username}}님의 리뷰입니다.
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
        <div v-if="user">
        <router-link class="btn btn-primary mr-3" :to="{name: 'ReviewCreate', params: { movie: review.movie, url: review.movie.title, review:review},}">Update </router-link>
        <router-link class="btn btn-primary mr-3" :to="{name: 'ReviewCreate', params: { movie: review.movie, url: review.movie.title, review:review},}">Delete </router-link>
        <button class='btn btn-primary' @click="deleteReview">Delete</button>
        <hr>
        </div>
      



        <!-- Single Comment -->
        <div class="media mb-4">
          <img class="d-flex mr-3 rounded-circle" src="http://placehold.it/50x50" alt="">
          <div class="media-body">
            <h5 class="mt-0">Commenter Name</h5>
            Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
          </div>
        </div>

        <!-- Comments Form -->
        <div class="card my-4">
          <h5 class="card-header">Leave a Comment:</h5>
          <div class="card-body">
            <form>
              <div class="form-group">
                <textarea class="form-control" rows="3"></textarea>
              </div>
              <button type="submit" class="btn btn-primary">Submit</button>
            </form>
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
          }
        })
        .catch((err)=>{console.log(err)})
        

      },
      deleteReview: function(){
        const config = this.setToken()
        console.log(this.review.id)
        axios.delete("http://127.0.0.1:8000/movies/review_create_list/", config, this.review.id)
        .then((res)=>{
          console.log(res)
          console.log('deleted')
        })

      }
    },
    created: function(){
      this.userId()
    }

}
</script>

<style>

</style>