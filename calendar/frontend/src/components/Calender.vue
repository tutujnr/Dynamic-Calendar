<template>
  <div>
    <button @click="view = 'day'">Day View</button>
    <button @click="view = 'week'">Week View</button>
    <button @click="view = 'month'">Month View</button>
    <component :is="viewComponent" />
  </div>
</template>

<script lang="ts">
import { ref, defineComponent } from 'vue'
import DayView from '../views/DayView.vue'
import WeekView from '../views/WeekView.vue'
import MonthView from '../views/MonthView.vue'

export default defineComponent({
  components: {
    DayView,
    WeekView,
    MonthView
  },
  setup() {
    const view = ref('day')
    const viewComponent = computed(() => {
      return {
        day: DayView,
        week: WeekView,
        month: MonthView
      }[view.value]
    })

    return { view, viewComponent }
  }
})
</script>

<style>
/* Component styles */
</style>
