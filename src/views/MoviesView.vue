<template>
  <main class="container py-5">
    <h1 class="display-1 mb-3">Movies</h1>
    <div v-if="loading" class="d-flex justify-content-center">
      <div class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
    <div v-if="error.length > 0" class="alert alert-danger">{{ error }}</div>
    <div class="row row-cols-1 row-cols-md-4 g-4" v-if="!loading">
      <MovieCard :movie="movie" v-for="movie in movies" :key="movie.id" />
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import MovieCard from '@/components/MovieCard.vue';

let movies = ref([]);
let loading = ref(false);
let error = ref('');

const fetchMovies = () => {
  loading.value = true;
  fetch("/api/v1/movies")
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to fetch');
      }
      return response.json();
    })
    .then(data => {
      movies.value = data.movies; 
      loading.value = false;
    })
};

onMounted(fetchMovies);
</script>
