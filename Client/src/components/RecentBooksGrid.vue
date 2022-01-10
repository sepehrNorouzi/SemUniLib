<template>
  <div id="recentGrid">
    <h1>Popular recent books</h1>
    <div class="parent">
      <div v-for="book in books" :key="book.id">
        <recent-book :book="book" />
      </div>
    </div>
  </div>
</template>

<script>
import RecentBook from "./RecentBook.vue";

export default {
  props: ["books"],

  components: { RecentBook }
};
</script>

<style>
.parent {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(2, 1fr);
  grid-column-gap: 20px;
  grid-row-gap: 20px;
}
</style>
