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
                    <button class="btn btn-primary" @click.prevent="signupUser">Signup</button>
                </form>
            </div>
        </div>

        <div class="position-fixed bottom-0 end-0 p-3" style="z-index: 11">
            <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
                <div id="toast-header" class="toast-header">
                    <strong id="toastTitle" class="me-auto"></strong>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div id="toastBody" class="toast-body"></div>
            </div>
        </div>
    </div>    
</template>

<script>
import api from '../service/api'

export default {
    data() {
        return {
            userData: {
                username: '',
                password: '',
            },
            message: null,
            err: null,
        };
    },
    methods: {
        signupUser() {
            Promise.resolve(api.signup(this.userData)).then(user => {
                this.triggerToast('successful!', 'user has been created successfully, please login.', 'message');
            }).catch(err => {
                this.triggerToast('unsuccessful!', err.response.data, 'err');
                console.log(err.response.data)
            });
        },
        triggerToast(title, body, type) {
            var toastLiveExample = document.getElementById('liveToast');
            document.getElementById('toastTitle').innerHTML = title;
            document.getElementById('toastBody').innerHTML = body;
            if(type == 'err') {
                document.getElementById('toast-header').classList.add('bg-danger');
            }
            else {
                document.getElementById('toast-header').classList.add('bg-success');
            }
            var toast = new bootstrap.Toast(toastLiveExample);
            toast.show()
        },
    }
}
</script>

<style scoped>
    .signup {
        height: 100vh;
    }
    #toastTitle {
        color: white;
    }
</style>