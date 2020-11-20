import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'
import Signup from '@/views/Signup'
import Login from '@/views/Login'
import ReviewCreate from '@/views/ReviewCreate'
import Community from '@/views/Community'
import Recommendation from '@/views/Recommendation'
Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/movies/reviews',
    name: 'ReviewCreate',
    component: ReviewCreate,
  },
  {
    path: '/community',
    name: 'Community',
    component: Community,
  },
  {
    path: '/recommendation',
    name: 'Recommendation',
    component: Recommendation,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
