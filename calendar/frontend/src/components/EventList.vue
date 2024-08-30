<template>
  <div>
    <div v-for="event in events" :key="event.id">
      <h3>{{ event.title }}</h3>
      <p>{{ event.description }}</p>
      <p>{{ event.start_time }} - {{ event.end_time }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  setup() {
    const events = ref([])

    const fetchEvents = async () => {
      const response = await axios.get('/events/')
      events.value = response.data
    }

    onMounted(() => {
      fetchEvents()
    })

    return { events }
  }
}
</script>

<style>
/* List styles */
</style>
