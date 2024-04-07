<template>
  <div class="card" style="width: 18rem;">
    <div class="image-container">
      <img :src="movie.poster" class="card-img-top" alt="Movie Poster">
    </div>
    <div class="card-body">
      <h5 class="card-title">{{ movie.title }}</h5>
      <p class="card-text">{{ movie.description }}</p>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  movie: {
    type: Object,
    required: true,
  },
});
</script>

<style scoped>
.image-container .card-img-top {
  width: 100%; 
  height: 200px; 
  object-fit: cover; 
}
.card {
margin: 20px;
}

</style>