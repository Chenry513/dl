<template>
  <div class="modal" :class="{ 'd-block': isVisible }" tabindex="-1" aria-labelledby="preferenceModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content" v-if="model">
        <div class="modal-header">
          <h5 class="modal-title" id="preferenceModalLabel">{{ preference ? 'Edit' : 'Save' }} Preference for {{ model.name }}</h5>
          <button type="button" class="btn-close" @click="closeModal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="savePreference">
            <div class="mb-3">
              <label for="preference" class="form-label">Preference</label>
              <textarea v-model="preferenceText" class="form-control" id="preference" rows="3" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">{{ preference ? 'Update' : 'Save' }} Preference</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch, defineComponent } from 'vue';
import api from '../services/axiosInstance';

export default defineComponent({
  props: {
    model: {
      type: Object,
      required: true,
    },
    preference: {
      type: Object,
      default: null,
    },
    isVisible: {
      type: Boolean,
      required: true,
    },
  },
  setup(props, { emit }) {
    const preferenceText = ref('');

    watch(props.model, (newModel) => {
      if (newModel && props.preference) {
        preferenceText.value = props.preference.preference; // Set existing preference
      } else {
        preferenceText.value = ''; // Reset preference when a new model is selected
      }
    });

    const closeModal = () => {
      emit('close');
    };

    const savePreference = async () => {
      const payload = {
        model_id: props.model.id,
        preference: preferenceText.value,
      };
      console.log('Payload:', payload); // Log the payload

      try {
        let response;
        if (props.preference && props.preference.id) {
          response = await api.put(`/api/preferences/${props.preference.id}/`, payload);
        } else {
          response = await api.post('/api/preferences/', payload);
        }
        console.log('Preference saved successfully!');
        closeModal(); // Close the modal
        emit('preferenceSaved', response.data); // Emit an event to notify parent component
      } catch (error) {
        console.error('Failed to save preference:', error.response.data); // Log the error
        console.log('Failed to save preference. Please try again.');
      }
    };

    return {
      preferenceText,
      savePreference,
      closeModal,
    };
  },
});
</script>

<style>
.modal {
  display: none;
}
.modal.d-block {
  display: block;
  background-color: rgba(0, 0, 0, 0.5);
}
.modal-content {
  border-radius: 10px;
}
</style>