<template>
  <div class="container mt-5">
    <h1 class="mb-4">Profile</h1>
    <div v-if="loading" class="text-center">
      <p>Loading profile...</p>
    </div>
    <div v-else>
      <h2>User Information</h2>
      <p><strong>Username:</strong> {{ userProfile.username }}</p>
      <p><strong>Email:</strong> {{ userProfile.email }}</p>
      
      <h2>Preferences</h2>
      <div v-if="!preferences.length" class="text-center">
        <p>No preferences found.</p>
      </div>
      <div v-else class="row">
        <div class="col-md-4 mb-4" v-for="pref in preferences" :key="pref.model.name">
          <div class="card h-100">
            <div class="card-body">
              <h5 class="card-title">{{ pref.model.name }}</h5>
              <p class="card-text"><strong>Organization:</strong> {{ pref.model.organization }}</p>
              <p class="card-text"><strong>Use Cases:</strong> {{ pref.model.use_cases }}</p>
              <p class="card-text"><strong>Practices:</strong> {{ pref.model.practices }}</p>
              <p class="card-text"><strong>Preference:</strong> {{ pref.preference }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import api from '../services/axiosInstance';

export default {
  setup() {
    const userProfile = ref(null);
    const preferences = ref([]);
    const loading = ref(true);

    const fetchUserProfile = async () => {
      try {
        const response = await api.get('/api/profile/');
        userProfile.value = response.data;
      } catch (error) {
        console.error('Failed to fetch user profile:', error);
      }
    };

    const fetchPreferences = async () => {
      try {
        const response = await api.get('/api/preferences/list/');
        preferences.value = response.data;
      } catch (error) {
        console.error('Failed to fetch preferences:', error);
      }
    };

    onMounted(async () => {
      await fetchUserProfile();
      await fetchPreferences();
      loading.value = false;
    });

    return {
      userProfile,
      preferences,
      loading,
    };
  },
};
</script>

<style>
.container {
  max-width: 800px;
  margin-bottom: 50px; /* Ensure enough space at the bottom */
}

.card {
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.card-title {
  font-size: 1.25rem;
  font-weight: 600;
}

.card-text {
  font-size: 0.9rem;
}
</style>