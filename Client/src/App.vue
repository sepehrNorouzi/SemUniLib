<template>
  <div class="appContainer">
    <app-navigation></app-navigation>
    <router-view></router-view>
  </div>
</template>

<script>
import axios from 'axios'
import api from './service/api';
import navigationVue from './components/navigation.vue';

export default {
  data () {
    return {
     
    }
  },

  components: {
    appNavigation: navigationVue,
  },

  beforeCreate() {
    this.$store.dispatch('initializeStore');
    const token = this.$store.state.token;
    if(token) {
        axios.defaults.headers.common['Authorization'] = 'Token ' + token;
        Promise.resolve(api.getMe()).then(user => {
          if(user) {
            this.$store.dispatch('setUser', user);
          }
        }).catch(err => {
           console.log("here");
           delete axios.defaults.headers.common['Authorization'];
        });
    }
  }
}
</script>

<style>
  
</style>
