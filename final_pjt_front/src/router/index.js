import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'
import Signup from '@/views/Signup'
import Login from '@/views/Login'
import ReviewCreate from '@/views/ReviewCreate'
import Community from '@/views/Community'
import Mypage from '@/views/Mypage'
import MovieDetail from '@/views/MovieDetail'
import ReviewDetail from '@/views/ReviewDetail'
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
    path: '/movies/reviews/:url',
    name: 'ReviewCreate',
    component: ReviewCreate,
    props: true
  },
  {
    path: '/community',
    name: 'Community',
    component: Community,
  },
  {
    path: '/mypage',
    name: 'Mypage',
    component: Mypage,
  },
  {
    path: '/movieDetail/:url',
    name: 'MovieDetail',
    component: MovieDetail,
    props: true
  },
  {
    path: '/reviewDetail',
    name: 'ReviewDetail',
    component: ReviewDetail,
    props: true
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior () {
  return { x: 0, y: 0 };
}
})

export default router
