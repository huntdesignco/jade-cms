<template>
  <b-navbar toggleable="lg" type="light" variant="light" class="border-bottom">
    <b-navbar-brand href="#">Jade CMS</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav v-if="get_pages && get_pages.length" v-bind:class="{'ml-auto mr-auto': true }">
        <b-nav-item v-for="page in get_pages" v-bind:key="page.pid" v-bind:class="{ 'active' : (get_current_path == page.slug) }" :to="{ path: page.slug }">
          {{ page.name }}
        </b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: 'Navigation',
  computed: {
    get_pages: function () {
      return this.$store.getters.get_pages
    },
    get_current_path: function () {
      return this.$store.getters.get_current_path
    }
  }
}
</script>