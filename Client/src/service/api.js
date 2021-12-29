import axios from 'axios'

export default {
    getBooks() {
        return axios.get('/books/');
    },
    getMe() {
        return axios.get('/auth/users/me/');
    }
}