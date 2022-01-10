import axios from "axios";

export default {
  getBooks() {
    return axios.get("/books/", {
      transformRequest: (data, headers) => {
        delete headers.common["Authorization"];
        return data;
      }
    });
  },

  getRecentBooks() {
    return axios.get("/books/recents/", {
      transformRequest: (data, headers) => {
        delete headers.common["Authorization"];
        return data;
      }
    });
  },
  getMe() {
    return axios.get("/auth/users/me/");
  },
  signup(userData) {
    return axios.post("/auth/users/", userData);
  },
  login(userData) {
    return axios.post("/auth/token/login/", userData);
  },

  addToFavorites(id) {
    return axios.post('/books/favorites/', {book: id});
  },

  getFavorites() {
    return axios.get('/books/favorites/');
  }

};
