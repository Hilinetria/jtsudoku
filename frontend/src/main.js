import Vue from 'vue';
import App from './App.vue';

// Routes
import router from './router';

// Styles
// Customs css
import './assets/css/style.css';

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
