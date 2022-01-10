<template>
  <div class="container homeContainer">
    <div class="leftSide">
      <div class="myCarousel">
        <template v-if="!$route.params.page">
          <app-carousel :books="books.slice(16, 19)" />
        </template>
      </div>
      <template v-if="!$route.params.page">
        <div class="recentBooks">
          <recent-books-grid :books="recentBooks" />
        </div>
      </template>
      <div class="booksGrid">
        <app-book-grid :books="pagesBooks()"> </app-book-grid>
      </div>
      <div class="myPagination">
        <nav aria-label="Page navigation example">
          <ul class="pagination">
            <li class="page-item">
              <a class="page-link" href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
              </a>
            </li>
            <li
              class="page-item"
              v-for="index in parseInt(bookLen / 7)"
              :key="index"
            >
              <router-link
                class="page-link"
                :to="paginationTo(index)"
                exact
                active-class="active"
                >{{ index }}</router-link
              >
            </li>
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
import { mapState } from "vuex";
import CarouselVue from "./Carousel.vue";
import RecentBooksGrid from "./RecentBooksGrid.vue";

export default {
  data() {
    return {
      error: null
    };
  },
  computed: {
    ...mapState(["books", "bookLen", "recentBooks"])
  },
  created() {
    if (!this.books) {
      Promise.resolve(api.getBooks())
        .then(res => {
          this.$store.dispatch("setBooks", res.data);
        })
        .catch(err => {
          this.error = err;
        });
    }

    if (!this.recentBooks) {
      Promise.resolve(api.getRecentBooks())
        .then(res => {
          this.$store.dispatch("setRecentBooks", res.data);
        })
        .catch(err => {
          this.error = err;
        });
    }
  },
  methods: {
    pagesBooks() {
      if (this.$route.params.page) {
        return this.books.slice(
          (this.$route.params.page - 1) * 7,
          this.$route.params.page * 7
        );
      } else {
        return this.books.slice(0, 7);
      }
    },
    paginationTo(index) {
      return `/${index}`;
    }
  },
  components: {
    appBookGrid: BookGridVue,
    appCarousel: CarouselVue,
    RecentBooksGrid
  }
};
</script>

<style scoped>
.active {
  background-color: rgb(155, 191, 245);
}
</style>
