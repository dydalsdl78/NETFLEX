import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/Signup'
import Home from '@/views/Home'
import Login from '@/views/Login'
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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
