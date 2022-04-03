<template>
  <div id="app">
      <div>　　
        <router-link to="/list/wyj">WYJ</router-link>
        <router-link to="/list/hrt">HRT</router-link>
      </div>
      <router-view></router-view>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
// import Login from './components/Login.vue'
// import Index from './components/Index.vue'
export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

}
</style>
