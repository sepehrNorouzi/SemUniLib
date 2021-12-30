<template>
  <div class="login">
    <div class="card">
      <div class="card-header">Login</div>
      <div class="card-body">
        <div class="alert alert-danger" role="alert" v-if="err">
          {{ err }}
        </div>
        <form>
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input
              type="text"
              class="form-control"
              id="username"
              placeholder="John Doe"
              v-model="userData.username"
            />
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input
              type="password"
              class="form-control"
              id="password"
              v-model="userData.password"
            />
          </div>
          <button class="btn btn-success" @click.prevent="loginUser">
            Login
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import api from "../service/api";
import axios from "axios";
import { mapState } from 'vuex'


export default {
  data() {
    return {
      userData: {
        username: "",
        password: ""
      },
      err: null
    };
  },

  methods: {
    loginUser() {
      Promise.resolve(api.login(this.userData))
        .then(response => {
          this.$store.dispatch("setToken", response.data.auth_token);
          const token = this.$store.state.token;
          if (token) {
            axios.defaults.headers.common["Authorization"] = "Token " + token;
            Promise.resolve(api.getMe())
              .then(user => {
                if (user) {
                  this.$store.dispatch("setUser", user);
                  this.$router.push("/");
                }
              })
              .catch(err => {
                delete axios.defaults.headers.common["Authorization"];
              });
          }
        })
        .catch(err => {
          if (err) {
            this.err = err.response.data.non_field_errors[0];
          }
        });
    }
  },

  computed: {
      ...mapState(['isUserLogedin']),
  }
};
</script>

<style scoped>
.login {
  height: 100vh;
}
</style>
