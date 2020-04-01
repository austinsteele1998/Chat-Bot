import Vue from 'vue';
import Router from 'vue-router';
import Ping from './Ping.vue';
import Chat from './components/Chat';

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/ping',
            name: 'Ping',
            component: Ping,
        },
        {
            path: '/chat',
            name: 'Chat',
            component: Chat,
        },
        /*
        {
            path: '/ai_chat',
            name: 'AIChat',
            component: Chat,
        }*/
    ],
});
