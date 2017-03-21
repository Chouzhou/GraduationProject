import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/home'
import Learn from '@/views/learn'
import personalInfo from '@/views/personalInfo'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },{
      path: '/learn',
      name: 'Learn',
      component: Learn
    }
  ]
})
