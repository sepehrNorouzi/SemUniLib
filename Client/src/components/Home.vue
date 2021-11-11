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

export default {
    data() {
        return {
            books: [
                {
                    "id": 1,
                    "title": "The Hunger Games",
                    "isbn13": "9780439023480",
                    "imageUrl": "https://images.gr-assets.com/books/1447303603m/2767052.jpg",
                    "author": "Suzanne Collins",
                    "rating": 4.43,
                    "published_date": "2008-01-01"
                },
                {
                    "id": 2,
                    "title": "Harry Potter and the Philosopher's Stone",
                    "isbn13": "9780439554930",
                    "imageUrl": "https://images.gr-assets.com/books/1474154022m/3.jpg",
                    "author": "J.K. Rowling, Mary GrandPrÃ",
                    "rating": 4.44,
                    "published_date": "1997-01-01"
                },
                {
                    "id": 3,
                    "title": "Twilight",
                    "isbn13": "9780316015840",
                    "imageUrl": "https://images.gr-assets.com/books/1361039443m/41865.jpg",
                    "author": "Stephenie Meyer",
                    "rating": 3.57,
                    "published_date": "2005-01-01"
                },
                {
                    "id": 4,
                    "title": "To Kill a Mockingbird",
                    "isbn13": "9780061120080",
                    "imageUrl": "https://images.gr-assets.com/books/1361975680m/2657.jpg",
                    "author": "Harper Lee",
                    "rating": 4.25,
                    "published_date": "1960-01-01"
                },
                {
                    "id": 3,
                    "title": "Twilight",
                    "isbn13": "9780316015840",
                    "imageUrl": "https://images.gr-assets.com/books/1361039443m/41865.jpg",
                    "author": "Stephenie Meyer",
                    "rating": 3.57,
                    "published_date": "2005-01-01"
                },
                {
                    "id": 4,
                    "title": "To Kill a Mockingbird",
                    "isbn13": "9780061120080",
                    "imageUrl": "https://images.gr-assets.com/books/1361975680m/2657.jpg",
                    "author": "Harper Lee",
                    "rating": 4.25,
                    "published_date": "1960-01-01"
                }
            ]
        };
    },
    components: {
        appBookGrid: BookGridVue,
    },
}
</script>

<style scoped>

</style>