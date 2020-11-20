import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/Signup'
import Home from '@/views/Home'
import Login from '@/views/Login'
import ReviewCreate from '@/views/ReviewCreate'
Vue.use(VueRouter)

const routes = [
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
