import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import 'swiper/css/swiper.css'
import VueAwesomeSwiper from 'vue-awesome-swiper';

Vue.use(VueAwesomeSwiper)
Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
