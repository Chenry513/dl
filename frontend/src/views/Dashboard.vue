<template>
  <div class="container mt-5">
    <h1 class="mb-4">AIMDC (AI Models Data Control) Dashboard</h1>
    <input
      type="text"
      class="form-control mb-4"
      v-model="query"
      placeholder="Search for models..."
    />
    <div v-if="loading" class="text-center">
      <p>Loading models...</p>
    </div>
    <div v-else>
      <div v-if="isLoggedIn">
        <!-- Logged In Version -->
        <div class="row">
          <div class="col-md-4 mb-4" v-for="model in filteredModels" :key="model.name">
            <div class="card h-100" @click="viewModelDetails(model.id)" style="cursor: pointer;">
              <div class="card-body">
                <h5 class="card-title">{{ model.name }}</h5>
                <p class="card-text"><strong>Organization:</strong> {{ model.organization }}</p>
                <p class="card-text"><strong>Use Cases:</strong> {{ model.use_cases }}</p>
                <p class="card-text"><strong>Practices:</strong> {{ model.practices }}</p>
                <div class="card-text data-info">
                  <strong>Data Info:</strong> {{ model.data_info }}
                </div>
                <div class="card-text concerning-practices" style="margin-bottom: 10px;">
                  <strong>Concerning Practices:</strong>
                  <!-- Render concerning practices here -->
                  <span>{{ model.concerning_practices }}</span>
                </div>
                <div class="card-text concerning-practices-links" style="margin-top: 10px;">
                  <strong>Concerning Practices Links:</strong>
                  <!-- Render concerning practices URLs here -->
                  <div v-if="model.concerning_practices_urls">
                    <div v-for="url in model.concerning_practices_urls.split(',')" :key="url.trim()">
                      <a :href="url.trim()" target="_blank" style="color: blue;">
                        {{ url.trim() }}
                      </a>
                    </div>
                  </div>
                  <div v-else>No concerning practices links provided</div>
                </div>
                <p class="card-text">
                  <strong>Severity:</strong>
                  <span :style="{ color: getColor(model.severity) }">{{ model.severity }}</span>
                </p>
                <button
                  class="btn btn-preference"
                  :class="hasPreference(model) ? 'btn-secondary' : 'btn-primary'"
                  @click.stop="openPreferenceModal(model)"
                >
                  {{ hasPreference(model) ? 'Edit Preference' : 'Save Preference' }}
                </button>
                <div v-if="hasPreference(model)" class="mt-2">
                  <strong>Saved Preference:</strong> {{ getPreference(model).preference }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        <!-- No Login Required Version -->
        <div class="row">
          <div class="col-md-4 mb-4" v-for="model in filteredModels" :key="model.name">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title">{{ model.name }}</h5>
                <p class="card-text"><strong>Organization:</strong> {{ model.organization }}</p>
                <p class="card-text"><strong>Use Cases:</strong> {{ model.use_cases }}</p>
                <p class="card-text"><strong>Practices:</strong> {{ model.practices }}</p>
                <div class="card-text data-info">
                  <strong>Data Info:</strong> {{ model.data_info }}
                </div>
                <div class="card-text concerning-practices" style="margin-bottom: 10px;">
                  <strong>Concerning Practices:</strong>
                  <span>{{ model.concerning_practices }}</span>
                </div>
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
                <p class="card-text">
                  <strong>Severity:</strong>
                  <span :style="{ color: getColor(model.severity) }">{{ model.severity }}</span>
                </p>
              </div>
            </div>
          </div>
        </div>
        <p class="text-center mt-4">Log in to save your preferences.</p>
      </div>
    </div>
    <PreferenceModal v-if="selectedModel" :model="selectedModel" :preference="selectedPreference" :isVisible="isModalVisible" @close="closeModal" @preferenceSaved="handlePreferenceSaved" />
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import { useMainStore } from '../stores';
import PreferenceModal from '../components/PreferenceModal.vue';

export default {
  components: {
    PreferenceModal,
  },
  setup() {
    const authStore = useAuthStore();
    const store = useMainStore();
    const router = useRouter();
    const loading = ref(true);
    const query = ref('');
    const selectedModel = ref(null);
    const selectedPreference = ref(null);
    const isModalVisible = ref(false);

    const openPreferenceModal = (model) => {
      selectedModel.value = model;
      selectedPreference.value = getPreference(model);
      isModalVisible.value = true;
    };

    const closeModal = () => {
      isModalVisible.value = false;
      selectedModel.value = null;
      selectedPreference.value = null;
    };

    const handlePreferenceSaved = (preference) => {
      console.log('Preference saved:', preference);
      closeModal();
      fetchPreferences();
    };

    const fetchPreferences = async () => {
      await store.fetchUserProfile();
    };

    const viewModelDetails = (modelId) => {
      router.push({ name: 'ModelDetails', params: { id: modelId } });
    };

    onMounted(async () => {
      await store.fetchModels();
      if (authStore.isLoggedIn) {
        await fetchPreferences();
      }
      loading.value = false;
    });

    const models = computed(() => store.models);
    const preferences = computed(() => store.userProfile?.preferences || []);
    const isLoggedIn = computed(() => authStore.isLoggedIn);

    const hasPreference = (model) => {
      return preferences.value.some(pref => pref.model.name === model.name);
    };

    const getPreference = (model) => {
      return preferences.value.find(pref => pref.model.name === model.name) || {};
    };

    const getColor = (severity) => {
      if (severity === 'low') return 'green';
      if (severity === 'medium') return 'orange';
      if (severity === 'high') return 'red';
      return 'black';
    };

    const filteredModels = computed(() => {
      if (!query.value) {
        return models.value;
      }
      return models.value.filter(model =>
        model.name.toLowerCase().includes(query.value.toLowerCase()) ||
        model.organization.toLowerCase().includes(query.value.toLowerCase()) ||
        model.use_cases.toLowerCase().includes(query.value.toLowerCase()) ||
        model.practices.toLowerCase().includes(query.value.toLowerCase())
      );
    });

    return {
      query,
      models,
      preferences,
      loading,
      selectedModel,
      selectedPreference,
      isModalVisible,
      openPreferenceModal,
      closeModal,
      handlePreferenceSaved,
      hasPreference,
      getPreference,
      viewModelDetails,
      isLoggedIn,
      filteredModels,
      getColor,
    };
  },
};
</script>

<style>
.container {
  max-width: 1200px;
  margin-bottom: 100px; /* Ensure enough space at the bottom */
}

.card {
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  cursor: pointer;
}

.card-body {
  padding: 15px;
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

.data-info {
  margin-top: 10px;
}

.concerning-practices {
  margin-bottom: 10px; /* Added bottom margin for spacing */
}

.concerning-practices-links {
  margin-top: 10px; /* Added top margin for spacing */
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



