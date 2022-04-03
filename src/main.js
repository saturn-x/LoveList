import Vue from 'vue'
import App from './App.vue'
import ant from 'ant-design-vue';
import reqwest from 'reqwest';
import infiniteScroll from 'vue-infinite-scroll';
import 'ant-design-vue/dist/antd.css';
import axios from 'axios'
import http from './js/conncet'
import router from './router.js'
Vue.prototype.$http = http //全局注册，使用方法为:this.$http
Vue.prototype.$axios = axios;
Vue.config.productionTip = false
    //使用ant ui框架
Vue.use(ant)


new Vue({
    router,
    render: h => h(App),
}).$mount('#app')