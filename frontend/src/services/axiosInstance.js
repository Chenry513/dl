import axios from 'axios';
import Cookies from 'js-cookie';

const api = axios.create({
  baseURL: import.meta.env.PROD ? 'https://dl-tools.onrender.com' : 'http://localhost:8000/',
  withCredentials: true,
});

api.defaults.xsrfHeaderName = "X-CSRFToken";
api.defaults.xsrfCookieName = "csrftoken";

const fetchCSRFToken = async () => {
  try {
    await api.get('/set-csrf/');
    console.log('CSRF token set');
  } catch (error) {
    console.error('Error setting CSRF token:', error);
  }
};

fetchCSRFToken();

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
