<template>
  <form id="movieForm" @submit.prevent="saveMovie">
   <div v-if="successMessage" class="alert alert-success">
      {{ successMessage }}
    </div>
    <ul v-if="errorMessages.length">
      <li v-for="(error, index) in errorMessages" :key="index" class="alert alert-danger">
        {{ error }}
      </li>
    </ul>
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" class="form-control"  />
    </div>
    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea name="description" class="form-control" ></textarea>
    </div>
    <div class="form-group mb-3">
      <label for="poster" class="form-label">Poster</label>
      <input type="file" name="poster" class="form-control"  />
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</template>

<script setup>
import { ref, onMounted } from 'vue';

let csrf_token = ref("");
const successMessage = ref('');
const errorMessages = ref([]);

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      csrf_token.value = data.csrf_token;
    });
}

onMounted(() => {
  getCsrfToken();
});

function saveMovie() {
  let movieForm = document.getElementById('movieForm');
  let formData = new FormData(movieForm);
  
  fetch("/api/v1/movies", {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
  .then(response => response.json()) 
  .then(data => {
    if (data.errors) {
      errorMessages.value = data.errors; 
      successMessage.value = ''; 
    } else {
      successMessage.value = "Movie Successfully added";
      errorMessages.value = []; 
    }
  })
}

</script>

<style>
.form-group {
margin: 20px;
}
</style>