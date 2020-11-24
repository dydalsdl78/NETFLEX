<template>
  <div>
      Username : {{username}}
      <hr>
      <button @click="getUsername">getUsername</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'Username',
    data: function(){
        return{
            username:''
        }
    },
    methods:{
        setToken: function(){
            const token = localStorage.getItem('jwt')
            const config = {
                headers:{
                    Authorization: `JWT ${token}`
                }
            }
            return config
        },
        getUsername: function(){
            const config = this.setToken()
            console.log('here')
            console.log(config)
            axios.get('http://127.0.0.1:8000/accounts/username/', config)
            .then((res) =>{
                console.log('here2')
                console.log(res.data)
                this.username=res.data.username
            })
            .catch((err) =>{
                console.log(err)
            })


        }
    },
    Created(){
        this.getUsername()
    },

}
</script>

<style>

</style>