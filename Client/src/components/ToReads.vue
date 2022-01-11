<template>
  <div class="container homeContainer">
    <div class="alert alert-danger" role="alert" v-if="err">
      {{ err }}
    </div>
    <div class="booksGrid">
      <template v-if="$store.state.user && toReads.length">
        <app-book-grid :books="toReads"></app-book-grid>
      </template>

      <template v-else-if="$store.state.user">
        <h1>No To reads yet!! Pick some from home.</h1>
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
      toReads: [],
      err: null
    };
  },

  created() {
    this.initToReads();
  },

  methods: {
    initToReads() {
      Promise.resolve(api.getToReads())
        .then(res => {
          res.data.forEach(tr => {
            Promise.resolve(api.getBook(tr.book))
              .then(bookResponse => {
                this.toReads.push(bookResponse.data);
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
