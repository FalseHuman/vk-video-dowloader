import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import browserDetect from 'vue-browser-detect-plugin'

Vue.config.productionTip = false
Vue.use(browserDetect)

axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://localhost:8000/' // the FastAPI backend

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
