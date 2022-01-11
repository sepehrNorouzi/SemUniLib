<template>
    <div class="col">
        <div class="card mb-3 mx-auto" style="max-width: 540px;">
            <div class="row g-0 bahiCard">
                <div class="col-md-4 bahiImage">
                    <img :src="book.imageUrl" class="myImage rounded" alt="book">
                </div>
                <div class="col-md-4 bahiText">
                    <div class="card-body">
                        <h5 class="card-title">Name: {{ book.title }}</h5>
                        <p class="card-text">Publish date: {{ book.published_date }}</p>
                        <p class="card-text">Authors: {{ book.author }}</p>
                        <p class="card-text">Rating: {{ book.rating }}</p>
                        <p class="card-text">ISBN13: {{ book.isbn13 }}</p>
                        <template v-if="isUserLogedin">
                            <button class="myHeartButton" :class="{'redHeart': isInFavorites(book.id)}" @click="addToFavorites">♥</button>
                            <button class="card-link btn btn-success readButton" :class="{'inToReads': isInToReads(book.id)}" @click="addToToReads">
                                {{isInToReads(book.id) ? "Remove From To Reads" : "Add To To Reads"}}
                            </button>
                        </template>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '../service/api'

export default {

    props: ['book',],

    computed: {
        ...mapState(['isUserLogedin', 'favorites', 'toReads'])
    },


    methods: {
        addToFavorites() {
            Promise.resolve(api.addToFavorites(this.book.id)).then(response => {
                let fav = this.$store.state.favorites;
                fav.push(response.data)
                this.$store.dispatch('setFavorites', fav);
            }).catch(err => {
                (err)
            })
        },

        addToToReads() {
            Promise.resolve(api.addToToReads(this.book.id)).then(response => {
                let tr = this.$store.state.toReads;
                tr.push(response.data)
                this.$store.dispatch('setToReads', tr);
            }).catch(err => {
                console.log(err)
            })
        },


        isInFavorites(id) {
            for(let i = 0; i < this.favorites.length; i++) {
                if(this.favorites[i].book == id) {
                    
                    return true;
                }
            }
            return false;
        },

        isInToReads(id) {
            for(let i = 0; i < this.toReads.length; i++) {
                console.log(this.toReads[i].book, id)
                if(this.toReads[i].book == id) {
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

.inToReads {
    background: red;
}

</style>