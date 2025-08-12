import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Dashboard from '../views/Dashboard.vue';
import ModelDetails from '../views/ModelDetails.vue';
import Search from '../views/Search.vue';
import Profile from '../views/Profile.vue';
import SignUp from '../views/Signup.vue';
import Login from '../views/Login.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/model/:id', name: 'ModelDetails', component: ModelDetails },
  { path: '/search', name: 'Search', component: Search },
  { path: '/profile', name: 'Profile', component: Profile },
  // { path: '/signup', name: 'SignUp', component: SignUp },
  //{ path: '/login', name: 'Login', component: Login },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;