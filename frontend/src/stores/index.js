import { defineStore } from 'pinia';
import { ref } from 'vue';
import api from '../services/axiosInstance';

export const useMainStore = defineStore('main', () => {
  const models = ref([]);
  const userProfile = ref(null);

  async function fetchModels() {
    try {
      const response = await api.get('/api/models/');
      models.value = response.data;
    } catch (error) {
      console.error('Failed to fetch models:', error);
    }
  }

  async function fetchUserProfile() {
    try {
      const response = await api.get('/api/profile/');
      userProfile.value = response.data;
    } catch (error) {
      console.error('Failed to fetch user profile:', error);
    }
  }

  return {
    models,
    userProfile,
    fetchModels,
    fetchUserProfile,
  };
});