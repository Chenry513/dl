<template>
  <div id="app">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/">DL Tools</router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <router-link class="nav-link" to="/dashboard">Dashboard</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/search">Search</router-link>
            </li>
            <li class="nav-item" v-if="isLoggedIn">
              <router-link class="nav-link" to="/profile">Profile</router-link>
            </li>
            <!-- <li class="nav-item" v-else>
              <router-link class="nav-link" to="/login">Log In</router-link>
            </li> -->
            <li class="nav-item" v-if="isLoggedIn">
              <a class="nav-link" @click="logout">Log Out</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    
    <!-- Main Content -->
    <div class="main-content">
      <router-view />
    </div>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script>
import { onMounted, computed } from 'vue';
import Footer from './components/Footer.vue';
import { useAuthStore } from './stores/auth';

export default {
  name: 'App',
  components: {
    Footer,
  },
  setup() {
    const authStore = useAuthStore();

    const logout = async () => {
      await authStore.logout();
    };

    onMounted(() => {
      authStore.checkAuth();
    });

    return {
      isLoggedIn: computed(() => authStore.isLoggedIn),
      logout,
    };
  },
};
</script>

<style>
html, body, #app {
  height: 100%;
  margin: 0;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  padding: 20px;
  box-sizing: border-box;
}

.navbar-brand {
  font-size: 1.5rem;
  font-weight: 600;
}

.nav-link {
  font-size: 1.1rem;
}

footer {
  flex-shrink: 0;
}
</style>