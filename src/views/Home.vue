<template>
  <div class="home">
    <HomePage msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HomePage from '@/components/Home.vue'

export default {
  name: 'Home',
  components: {
    HomePage
  }
}
</script>
