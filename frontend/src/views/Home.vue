<template>
  <div class="container mt-5">
    <h1>Welcome to DL Tools</h1>
    <p class="lead">Your go-to platform for managing and understanding AI models.</p>
    <router-link to="/dashboard" class="btn btn-primary">Go to Dashboard</router-link>
    
    <div class="contribute-section mt-5">
      <h3>Want to Contribute?</h3>
      <p>Help expand our AI model library! Here's how:</p>
      
      <div class="instructions">
        <div class="instruction-item">
          <strong>Add a New Model:</strong> Create a <code>.md</code> file in the 
          <a href="https://github.com/Chenry513/dl/tree/main/dl_tools/markdown_files" target="_blank">markdown_files folder</a>. 
          Follow the existing format with model details, parameters, and use cases.
        </div>
        
        <div class="instruction-item">
          <strong>Edit Existing Models:</strong> Update any <code>.md</code> file in the repo to fix errors or add new info. 
          Changes appear on the site within a minute after merging.
        </div>
      </div>
      
      <p class="note">All contributions are reviewed before going live. Thanks for helping out!</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
};
</script>

<style scoped>
.container {
  text-align: center;
  padding-top: 50px;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
}

.contribute-section {
  max-width: 700px;
  margin: 0 auto;
  padding: 30px;
  background-color: #f8f9fa;
  border-radius: 8px;
}

.contribute-section h3 {
  margin-bottom: 15px;
  color: #333;
}

.instructions {
  text-align: left;
  margin: 20px 0;
}

.instruction-item {
  margin-bottom: 15px;
  padding: 15px;
  background-color: white;
  border-radius: 5px;
  border-left: 4px solid #007bff;
}

.instruction-item strong {
  color: #007bff;
}

code {
  background-color: #e9ecef;
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 0.9em;
}

a {
  color: #007bff;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

.note {
  font-size: 0.9em;
  color: #666;
  margin-top: 15px;
}
</style>
