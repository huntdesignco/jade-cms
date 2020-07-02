<template>
  <div v-html="html">
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: 'HTMLRenderer',
  computed: mapState({
    html: state => state.page_content,
  })
}
</script>