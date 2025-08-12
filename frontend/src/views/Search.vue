<template>
  <div class="container mt-5">
    <h1 class="mb-4">Advanced Search AI Models</h1>
    <form @submit.prevent="performSearch">
      <div class="mb-4">
        <input
          type="text"
          class="form-control"
          v-model="query"
          placeholder="Search for models..."
        />
      </div>
      <div class="mb-4">
        <input
          type="text"
          class="form-control"
          v-model="organization"
          placeholder="Filter by organization..."
        />
      </div>
      <div class="mb-4">
        <input
          type="text"
          class="form-control"
          v-model="useCases"
          placeholder="Filter by use cases..."
        />
      </div>
      <div class="mb-4">
        <input
          type="text"
          class="form-control"
          v-model="practices"
          placeholder="Filter by practices..."
        />
      </div>
      <button type="submit" class="btn btn-primary">Search</button>
    </form>
    <div v-if="filteredModels.length === 0" class="text-center mt-4">
      <p>No models found.</p>
    </div>
    <div v-else class="row mt-4">
      <div class="col-md-4 mb-4" v-for="model in filteredModels" :key="model.name">
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title">{{ model.name }}</h5>
            <p class="card-text"><strong>Organization:</strong> {{ model.organization }}</p>
            <p class="card-text"><strong>Use Cases:</strong> {{ model.use_cases }}</p>
            <p class="card-text"><strong>Practices:</strong> {{ model.practices }}</p>
            
            <!-- Concerning Practices -->
            <div class="card-text concerning-practices" style="margin-top: 10px;">
              <strong>Concerning Practices:</strong>
              <span>{{ model.concerning_practices }}</span>
            </div>
            
            <!-- Concerning Practices Links -->
            <div class="card-text concerning-practices-links" style="margin-top: 10px;">
              <strong>Concerning Practices Links:</strong>
              <div v-if="model.concerning_practices_urls">
                <div v-for="url in model.concerning_practices_urls.split(',')" :key="url.trim()">
                  <a :href="url.trim()" target="_blank" style="color: blue;">
                    {{ url.trim() }}
                  </a>
                </div>
              </div>
              <div v-else>No concerning practices links provided</div>
            </div>

            <!-- Severity -->
            <p class="card-text" style="margin-top: 10px;">
              <strong>Severity:</strong>
              <span :style="{ color: getColor(model.severity) }">{{ model.severity }}</span>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useMainStore } from '../stores';

export default {
  setup() {
    const store = useMainStore();
    const query = ref('');
    const organization = ref('');
    const useCases = ref('');
    const practices = ref('');

    const filteredModels = computed(() => {
      return store.models.filter(model => {
        const matchesQuery = !query.value || model.name.toLowerCase().includes(query.value.toLowerCase());
        const matchesOrganization = !organization.value || model.organization.toLowerCase().includes(organization.value.toLowerCase());
        const matchesUseCases = !useCases.value || model.use_cases.toLowerCase().includes(useCases.value.toLowerCase());
        const matchesPractices = !practices.value || model.practices.toLowerCase().includes(practices.value.toLowerCase());
        return matchesQuery && matchesOrganization && matchesUseCases && matchesPractices;
      });
    });

    const performSearch = () => {
      // This function can be used to trigger any side effects on form submission
    };

    const getColor = (severity) => {
      if (severity === 'low') return 'green';
      if (severity === 'medium') return 'orange';
      if (severity === 'high') return 'red';
      return 'black';
    };

    onMounted(() => {
      store.fetchModels();
    });

    return {
      query,
      organization,
      useCases,
      practices,
      filteredModels,
      performSearch,
      getColor,
    };
  },
};
</script>

<style>
.card {
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.card-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 10px;
  text-align: left;
}

.card-text {
  font-size: 0.9rem;
  margin-bottom: 5px;
  text-align: left;
}

.concerning-practices {
  margin-top: 10px;
}

.concerning-practices-links {
  margin-top: 10px;
}

.btn-preference {
  width: 100%;
  margin-top: 10px;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
}

.btn-secondary {
  background-color: #6c757d;
  border-color: #6c757d;
}
</style>
