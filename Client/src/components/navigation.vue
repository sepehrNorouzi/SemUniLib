<template>
    <div>
        <nav class="navbar navbar-light bg-light">
            <form class="container-fluid justify-content-start">
                <router-link to="/" tag="button" class="btn btn-outline-info me-2" active-class="btn-info" exact type="button">Home</router-link>
                <template v-if="!isUserLogedin">
                    <router-link to="/login" tag="button" class="btn btn-outline-success me-2" active-class="btn-success" type="button">Login</router-link>
                    <router-link to="/signup" tag="button" class="btn btn-outline-primary" active-class="btn-primary" type="button">Sign up</router-link>
                </template>
                <template v-else>
                    <router-link to="/favorites" tag="button" class="btn btn-outline-danger me-2" active-class="btn-danger" exact type="button">Favorites</router-link>
                    <router-link to="/toreads" tag="button" class="btn btn-outline-success me-2" active-class="btn-success" exact type="button">To Read</router-link>
                    <p>Welcome {{ user.data.username }}<button class="btn btn-outline-dark" @click="logoutuser">Logout</button></p>    
                </template>
            </form>
        </nav>
    </div>
</template>

<script>

import { mapState } from 'vuex'

export default {
    

    computed: {
        ...mapState(['isUserLogedin', 'user'])
    },


    methods: {
        logoutuser() {
            this.$store.dispatch("cleanStore");
            this.$router.push('/');
        }
    },
}
</script>

<style scoped>
    .btn-danger, .btn-success, .btn-primary {
        color: white;
    }
</style>