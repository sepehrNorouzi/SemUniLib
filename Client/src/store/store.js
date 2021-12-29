import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        user: null,
        token: null,
        isUserLogedin: false,
    },
    mutations: {
        setUser(state, user) {
            state.user = user;
            isUserLogedin = true;
        },
        setToken(state, token) {
            state.token = token;
            isUserLogedin = true;
        },
        initializeStore(state) {
            if(localStorage.getItem('token')) {
                state.token = localStorage.getItem('token');
            }
            else {
                state.user = null;
                state.token = null;
                state.isUserLogedin = false;            
            }
        }
    },
    actions: {
        setUser({commit}, user) {
            commit("setUser", user);
        },
        setToken({commit}, token) {
            commit("setToken", token);
        },
        initializeStore({commit}) {
            commit("initializeStore");
        }
    },
})