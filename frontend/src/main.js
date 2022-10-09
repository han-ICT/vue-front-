import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'


Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
/*
import axios from "axios";

let url = "http://localhost:8000/location/"
axios.get(url)
.then(function(response){
  console.log(response);
})
.catch(function(response){
  console.log(response);
})
*/

