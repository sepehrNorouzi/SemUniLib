<template>
    <div class="container homeContainer">
       
        <div class="leftSide">
            <div class="myCarousel"></div>
            <div class="recentBooks"></div>
            <div class="booksGrid">
                <app-book-grid :books="books"></app-book-grid>
            </div>
            <div class="myPagination"></div>
        </div>

         <div class="rightSide">

        </div>

    </div>
</template>

<script>
import BookGridVue from './BookGrid.vue'
import api from '../service/api'

export default {
    data() {
        return {
            books: null,
            error: null
        };
    },
    created() {
        Promise.resolve(api.getBooks()).then(res => {
            this.books = res.data;
        }).catch(err => {
            this.error = err;
        });
    },
    components: {
        appBookGrid: BookGridVue,
    },
}
</script>

<style scoped>

</style>