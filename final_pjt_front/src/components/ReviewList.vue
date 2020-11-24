<template>

  <div id="ReviewList" class="container">
      <div class="card mb-3" style="background-color:black;">
          <div class="card-header">
              <div class="row">
                  <div class="col ">Topics</div>
                  <div class="col-4">
                      <div class="row">
                        <div class="col-4">Replis</div>
                        <div class="col-8">Last</div>
                      </div>
                  </div>

              </div>
          </div>
          <div class="card-body py-3" v-for="(review, idx) in reviews" :key="idx">
              <div class="row">
                  <div class="col text-left">
                    <router-link
                        class="nav-link"
                        :to="{
                        name: 'ReviewDetail',
                        params: { review: review, url: review.title },
                        }"
                        >{{review.title}}
                    </router-link>
                      <div class="small">{{review.movie.title}}를 보고 {{review.user.username}}님이 쓰신 리뷰</div>
                  </div>
                  <div class="d-none d-md-block col-4">
                    <div class="row">
                      <div class="col-4">댓글수</div>
                      <div class="col-8">{{review.created_at}}</div>
                      </div>
                  </div>
              </div>
          </div>
      </div>


  </div>
</template>

<script>
import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
    name:"ReviewList",
    data: function(){
        return {
            reviews:[],
            movie_titles:[],
        }
    },
    methods:{
        getList:function(){
                console.log('k')
                axios.get('http://127.0.0.1:8000/movies/review_create_list/')
                .then((res)=>{
                    console.log(res.data)
                    this.reviews = res.data
                }
                )
            }
        },
    created(){
        return(this.getList())
    }
}


</script>

<style scoped>
#ReviewList {
    background-color: black;

}
.nav-link {
    color:red;
}
.nav-link:hover {
    color:white;
}

</style>