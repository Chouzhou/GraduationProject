import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/home'
import Learn from '@/views/learn'
import personalInfo from '@/views/personalInfo'
import homework from '@/views/homework'
import detailCouser from '@/views/student/detailCouser'
import home from '../components/index'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: home
    },{
      path: '/',
      name: 'Index',
      component: home,
      children: [
        {
          path: '/student/home',
          name: 'Home',
          component: Home
        },{
          path: '/student/learn',
          name: 'Learn',
          component: Learn
        },{
          path: '/student/personalInfo',
          name: 'PersonalInfo',
          component: personalInfo
        },{
          path: '/student/homework',
          name: 'Homework',
          component: homework
        },{
          path: '/student/detailCouser',
          name: 'detailCouser',
          component: detailCouser
        }
      ]
    }
  ]
})
