<template>
    <div class="col">
        <div class="card" style="width: 18rem;">
            <img :src="book.imageUrl" class="card-img-top" alt="Book">
            <div class="card-body">
                <h5 class="card-title">Name: {{ book.title }}</h5>
            </div>
            <ul class="list-group list-group-flush">
                <li class="list-group-item">Publish date: {{ book.published_date }}</li>
                <li class="list-group-item">Authors: {{ book.author }}</li>
                <li class="list-group-item">Rating: {{ book.rating }}</li>
                <li class="list-group-item">ISBN13: {{ book.isbn13 }}</li>
            </ul>
            <div class="card-body">
                <a href="#" class="card-link">Add to favorite</a>
                <a href="#" class="card-link">Add to read</a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['book'],
}
</script>

<style scoped>

</style>