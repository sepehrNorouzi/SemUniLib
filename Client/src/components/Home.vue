<template>
  <div class="container homeContainer">
    <div class="leftSide">
      <div class="myCarousel"></div>
      <div class="recentBooks"></div>
      <div class="booksGrid">
        <app-book-grid :books="books"></app-book-grid>
      </div>
      <div class="myPagination">
        <nav aria-label="Page navigation example">
          <ul class="pagination">
            <li class="page-item">
              <a class="page-link" href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
              </a>
            </li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item">
              <a class="page-link" href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </div>

    <div class="rightSide"></div>
  </div>
</template>

<script>
import BookGridVue from "./BookGrid.vue";
import api from "../service/api";
import { mapState } from 'vuex'

export default {
  data() {
    return {
      error: null
    };
  },
  computed: {
      ...mapState(['books'])
  },
  created() {
    if(!this.books) {
    Promise.resolve(api.getBooks())
      .then(res => {
        this.$store.dispatch('setBooks', res.data);
      })
      .catch(err => {
        this.error = err;
      });
    }
  },
  components: {
    appBookGrid: BookGridVue
  }
};
</script>

<style scoped></style>
