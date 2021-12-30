import Home from "../components/Home.vue";
import Login from "../components/Login.vue";
import Signup from "../components/Signup.vue";

export const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
  { path: "/signup", component: Signup },
  { path: "/:page", component: Home },
];
