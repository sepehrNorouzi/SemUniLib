import axios from 'axios'

export default {
    getBooks() {
        return axios.get('/books/');
    },
    getMe() {
        return axios.get('/auth/users/me/');
    },
    signup(userData) {
        return axios.post('/auth/users/', userData);
    },
    login(userData) {
        return axios.post('/auth/token/login/', userData);
    }
}