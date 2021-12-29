<template>
    <div class="signup">
        <div class="card">
            <div class="card-header">Signup</div>
            <div class="card-body">
                <form>
                    <div class="mb-3">
                        <label for="username" class="form-label">Username</label>
                        <input type="text" class="form-control" id="username" placeholder="John Doe" v-model="userData.username">
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">Password</label>
                        <input type="password" class="form-control" id="password" v-model="userData.password">
                    </div>
                    <button class="btn btn-primary">Signup</button>
                </form>
            </div>
        </div>
    </div>    
</template>

<script>
export default {
    data() {
        return {
            userData: {
                username: '',
                password: '',
            },
            err: null,
        };
    },
}
</script>

<style scoped>
    .signup {
        height: 100vh;
    }
</style>