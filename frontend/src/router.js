import Vue from 'vue'
import Router from 'vue-router'

import MainMenu from './views/MainMenu.vue'
import SingleGame from './views/SingleGame.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'menu',
            component: MainMenu
        },
        
        {
            path: '/single',
            name: 'single',
            component: SingleGame
        },        
    ]
});
