<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">TQDB</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name:'Home'}"> Home </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'Login' }">Log in </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'Signup' }">Sign up</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/">Community</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/">Recommendation</router-link>
          </li>
        </ul>


      </div>
    </nav>
    <router-view/>


  </div>
</template>

<script>

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
