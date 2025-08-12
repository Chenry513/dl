<template>
    <div class="container mt-5">
      <h1>Welcome to DL Tools</h1>
      <p class="lead">Your go-to platform for managing and understanding AI models.</p>
      <router-link to="/dashboard" class="btn btn-primary">Go to Dashboard</router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Home',
  };
  </script>
  
  <style>
  .container {
    text-align: center;
    padding-top: 50px;
  }
  
  .btn-primary {
    background-color: #007bff;
    border-color: #007bff;
  }
  </style>