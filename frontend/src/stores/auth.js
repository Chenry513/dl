import { defineStore } from 'pinia';
import axios from '../services/axiosInstance'; // Ensure this path is correct

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isLoggedIn: false,
  }),
  actions: {
    async checkAuth() {
      try {
        const response = await axios.get('/auth-check/');
        this.isLoggedIn = response.status === 200 && response.data.authenticated;
      } catch (error) {
        this.isLoggedIn = false;
      }
    },
    async login(credentials) {
      try {
        await axios.post('/login/', new URLSearchParams(credentials));
        this.isLoggedIn = true;
        window.location.href = '/'; // Redirect to dashboard after successful login
      } catch (error) {
        this.isLoggedIn = false;
        throw error;
      }
    },
    async logout() {
      try {
        await axios.post('/logout/');
        this.isLoggedIn = false;
        window.location.href = '/'; // Redirect to home after logout
      } catch (error) {
        console.error('Logout failed', error);
      }
    },
  },
});