import Vue from 'vue';
import App from './App.vue';

// Routes
import router from './router';

// Styles
import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
// Customs css
import './assets/css/style.css';

Vue.config.productionTip = false;
// Enable Buefy css framework
Vue.use(Buefy);

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
