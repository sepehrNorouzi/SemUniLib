<template>
  <div class="container homeContainer">
    <div class="booksGrid">
      <app-book-grid :books="favorites"></app-book-grid>
    </div>
  </div>
</template>

<script>
export default {
    props: ['favorites'],
};
</script>

<style></style>
