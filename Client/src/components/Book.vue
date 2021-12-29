<template>
    <div class="col">
        <!-- <div class="card" style="width: 18rem;">
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
        </div> -->

        <div class="card mb-3 mx-auto" style="max-width: 540px;">
            <div class="row g-0 bahiCard">
                <div class="col-md-4 bahiImage">
                    <img :src="book.imageUrl" class="myImage rounded" alt="book">
                </div>
                <div class="col=md-8 bahiText">
                    <div class="card-body">
                        <h5 class="card-title">Name: {{ book.title }}</h5>
                        <p class="card-text">Publish date: {{ book.published_date }}</p>
                        <p class="card-text">Authors: {{ book.author }}</p>
                        <p class="card-text">Rating: {{ book.rating }}</p>
                        <p class="card-text">ISBN13: {{ book.isbn13 }}</p>
                        <button class="myHeartButton">♥</button>
                        <button class="card-link btn btn-success readButton">Add to read</button>
                    </div>
                </div>
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