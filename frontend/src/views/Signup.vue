<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card shadow-sm">
          <div class="card-body">
            <h1 class="mb-4 text-center">Sign Up</h1>
            <form @submit.prevent="signup">
              <div class="mb-3">
                <label for="username" class="form-label">Username</label>
                <input type="text" class="form-control" id="username" v-model="username" required>
              </div>
              <div class="mb-3">
                <label for="email" class="form-label">Email</label>
                <input type="email" class="form-control" id="email" v-model="email" required>
              </div>
              <div class="mb-3">
                <label for="password" class="form-label">Password</label>
                <input type="password" class="form-control" id="password" v-model="password" required>
              </div>
              <button type="submit" class="btn btn-primary w-100">Sign Up</button>
              <p v-if="error" class="text-danger mt-3">{{ error }}</p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from '../services/axiosInstance';

export default {
  setup() {
    const username = ref('');
    const email = ref('');
    const password = ref('');
    const error = ref('');

    const signup = async () => {
      try {
        const response = await axios.post('/register/', {
          username: username.value,
          email: email.value,
          password: password.value,
        });
        if (response.status === 200) {
          window.location.href = '/login'; // Redirect to login page after successful signup
        } else {
          error.value = 'Signup failed';
        }
      } catch (err) {
        error.value = err.response.data.errors || 'An error occurred';
      }
    };

    return {
      username,
      email,
      password,
      error,
      signup,
    };
  },
};
</script>

<style>
.container {
  max-width: 600px;
  margin-top: 100px;
}

.card {
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.card-body {
  padding: 30px;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #0056b3;
  border-color: #004085;
}

.text-center {
  text-align: center;
}
</style>