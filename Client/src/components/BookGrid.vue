<template>
    <div class="container">
        <app-book  v-for="book in books" :key="book.id" :book="book"></app-book>    
    </div>
</template>

<script>
import BookVue from './Book.vue'

export default {
    props: ['books'],
    components: {
        appBook: BookVue,
    }
}
</script>

<style scoped>
    .container {
        padding: 1rem;
    }
</style>