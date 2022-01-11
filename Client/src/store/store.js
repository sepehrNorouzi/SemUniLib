import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        user: null,
        token: null,
        isUserLogedin: false,
        books: null,
        bookLen: 0,
        recentBooks: null,
        favorites: [],
        toReads: [],
    },
    mutations: {
        
        setBooks(state, books) {
            state.books = books;
            state.bookLen = books.length;
        },

        setRecentBooks(state, books) {
            state.recentBooks = books;
        },

        setUser(state, user) {
            state.user = user;
            state.isUserLogedin = true;
        },

        setFavorites(state, favorites) {
            state.favorites = favorites;
        },

        setToReads(state, toReads) {
            state.toReads = toReads;
        },

        setToken(state, token) {
            if(localStorage.getItem("token")) {
                localStorage.removeItem("token");
            }
            localStorage.setItem('token', token);
            state.token = token;
            state.isUserLogedin = true;
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
        },

        cleanStore(state) {
            state.token = null;
            if(localStorage.getItem("token")) {
                localStorage.removeItem("token");
            }
            state.user = null;
            state.isUserLogedin = false;
        }
    },
    actions: {
        setBooks({commit}, books) {
            commit("setBooks", books);
        },

        setRecentBooks({commit}, books) {
            commit("setRecentBooks", books);
        },

        setUser({commit}, user) {
            commit("setUser", user);
        },
        setToken({commit}, token) {
            commit("setToken", token);
        },
        initializeStore({commit}) {
            commit("initializeStore");
        },
        cleanStore({ commit }) {
            commit("cleanStore");
        },

        setFavorites({ commit }, favorites) {
            commit("setFavorites", favorites);
        },

        setToReads({ commit }, toReads) {
            commit("setToReads", toReads);
        },
    },
})