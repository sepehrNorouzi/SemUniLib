<template>
  <div class="container homeContainer">
    <div class="alert alert-danger" role="alert" v-if="err">
      {{ err }}
    </div>
    <div class="booksGrid">
      <template v-if="$store.state.user && favorites.length">
        <app-book-grid :books="favorites"></app-book-grid>  
      </template>

      <template v-else-if="$store.state.user">
        <h1>No favorites yet!! Pick some from home.</h1>
      </template>
    </div>
  </div>
</template>

<script>
import api from "../service/api";
import appBookGrid from "./BookGrid.vue";
export default {
  components: { appBookGrid },

  data() {
    return {
      favorites: [],
      err: null
    };
  },

  created() {
    this.initFavorites();
  },

  methods: {
    initFavorites() {
      Promise.resolve(api.getFavorites())
        .then(res => {
          res.data.forEach(fav => {
            Promise.resolve(api.getBook(fav.book))
              .then(bookResponse => {
                this.favorites.push(bookResponse.data);
              })
              .catch(err => {
                this.err = err.response.data;
              });
          });
        })
        .catch(err => {
          this.err = err.response.data;
        });
    }
  }
};
</script>

<style></style>
