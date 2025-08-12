import axios from 'axios';
import Cookies from 'js-cookie'; // Import the js-cookie library


const api = axios.create({
  baseURL: 'http://localhost:8000/',
  withCredentials: true, // Ensure cookies are sent with requests
});

api.defaults.xsrfHeaderName = "X-CSRFToken";
api.defaults.xsrfCookieName = "csrftoken";

// Fetch CSRF token
const fetchCSRFToken = async () => {
  try {
    await api.get('/set-csrf/');
    console.log('CSRF token set');
  } catch (error) {
    console.error('Error setting CSRF token:', error);
  }
};

// Fetch CSRF token when the module is loaded
fetchCSRFToken();

// Add a request interceptor to include CSRF token in headers
api.interceptors.request.use((config) => {
  const csrfToken = Cookies.get('csrftoken');
  if (csrfToken) {
    config.headers['X-CSRFToken'] = csrfToken;
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

export default api;