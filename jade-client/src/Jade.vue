<template>
  <div id="jade">
    <div id="wrapper" class="d-flex flex-column">
      <Navigation />
        <main class="container-fluid flex-fill" v-bind:class="{ 'valign-middle' : (this.$store.getters.get_valign == 'middle') }">
          <router-view/>
        </main>
      <Footer />
    </div>
  </div>
</template>

<script>

import axios from 'axios';
import Navigation from './components/Navigation.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'Jade',
  components: {
    Navigation,
    Footer
  },
  
  // Fetches page names
  created() {    
    this.$store.dispatch('fetch_pages')
    this.$store.dispatch('fetch_main_menu')
    this.$store.dispatch('fetch_current_page', {name: this.$route.name, path: this.$route.path})
  },

  watch: {
    $route () {
      this.$store.dispatch('fetch_current_page', {name: this.$route.name, path: this.$route.path})
    }
  }
}
</script>
