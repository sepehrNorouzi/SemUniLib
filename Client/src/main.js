import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import {routes} from './routes/routes'
import axios from 'axios'
import {sync} from 'vuex-router-sync'
import store from './store/store'

Vue.use(VueRouter)

const router = new VueRouter({
  routes: routes,
  mode: 'history',
})

sync(store, router)

axios.defaults.baseURL = 'http://localhost:8000'

new Vue({
  el: '#app',
  router: router,
  axios: axios,
  store: store,
  render: h => h(App)
})
