<template>
    <div>
        <div class="container">
            <div class="row">
                <app-book  v-for="book in books" :key="book.id" :book="book"></app-book>    
            </div>
        </div>
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

</style>