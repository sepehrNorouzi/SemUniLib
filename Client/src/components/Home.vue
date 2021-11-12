<template>
    <div>
        <nav class="navbar navbar-light bg-light">
            <form class="container-fluid justify-content-start">
                <button class="btn btn-outline-success me-2" type="button">Login</button>
                <button class="btn btn-outline-secondary" type="button">Sign up</button>
            </form>
        </nav>

        <div>
            <app-book-grid :books="books"></app-book-grid>
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
        Promise.resolve(api().get('/books/')).then(res => {
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