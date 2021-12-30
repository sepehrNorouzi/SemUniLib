<template>
    <div class="col">
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
                        <template v-if="isUserLogedin">
                            <button class="myHeartButton" :class="{'redHeart': isInFavorites(book.id)}" @click="addToFavorites">♥</button>
                            <button class="card-link btn btn-success readButton">Add to read</button>
                        </template>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import { mapState } from 'vuex'
import api from '../service/api'

export default {

    props: ['book',],

    computed: {
        ...mapState(['isUserLogedin', 'favorites'])
    },


    methods: {
        addToFavorites() {
            Promise.resolve(api.addToFavorites(this.book.id)).then(response => {
                let fav = this.$store.state.favorites;
                fav.push(response.data)
                this.$store.dispatch('setFavorites', this.favorites);
                window.location.reload();
            }).catch(err => {
                console.log(err)
            })
        },

        isInFavorites(id) {
            console.log(id, this.favorites);
            for(let i = 0; i < this.favorites.length; i++) {
                if(this.favorites[i].book == id) {
                    console.log("here");
                    return true;
                }
            }
            return false;
        }
    },
}
</script>

<style scoped>

.redHeart {
    color: red;
}

</style>