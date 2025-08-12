<template>
    <div class="container mt-5">
      <div v-if="loading" class="text-center">
        <p>Loading model details...</p>
      </div>
      <div v-else>
        <h1 class="mb-4">{{ model.name }}</h1>
        <p><strong>Organization:</strong> {{ model.organization }}</p>
        <p><strong>Use Cases:</strong> {{ model.use_cases }}</p>
        <p><strong>Practices:</strong> {{ model.practices }}</p>
        <p><strong>Data Info:</strong> {{ model.data_info }}</p>
        <p><strong>Concerning Practices:</strong> {{ model.concerning_practices }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  import api from '../services/axiosInstance';
  
  export default {
    setup() {
      const route = useRoute();
      const model = ref(null);
      const loading = ref(true);
  
      const fetchModelDetails = async (id) => {
        try {
          const response = await api.get(`/api/models/${id}/`);
          model.value = response.data;
        } catch (error) {
          console.error('Failed to fetch model details:', error);
        } finally {
          loading.value = false;
        }
      };
  
      onMounted(() => {
        fetchModelDetails(route.params.id);
      });
  
      return {
        model,
        loading,
      };
    },
  };
  </script>
  
  <style>
  .container {
    max-width: 800px;
  }
  </style>