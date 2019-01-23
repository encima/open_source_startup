import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import Swagger from 'swagger-client'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'

Vue.use(VueMaterial)

Vue.config.productionTip = false

 Swagger({
   url: 'http://localhost:8081/openapi.json'
        }).then(client => {
          console.log('client reached');
        }).catch(err => {
          console.error('Endpoint likely not available');
        });

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
