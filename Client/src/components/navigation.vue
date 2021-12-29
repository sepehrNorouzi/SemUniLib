<template>
    <div>
        <nav class="navbar navbar-light bg-light">
            <form class="container-fluid justify-content-start">
                <router-link to="/" tag="button" class="btn btn-outline-danger me-2" active-class="btn-danger" exact type="button">Home</router-link>
                <router-link to="/login" tag="button" class="btn btn-outline-success me-2" active-class="btn-success" type="button">Login</router-link>
                <router-link to="/signup" tag="button" class="btn btn-outline-primary" active-class="btn-primary" type="button">Sign up</router-link>
            </form>
        </nav>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
    .btn-danger, .btn-success, .btn-primary {
        color: white;
    }
</style>