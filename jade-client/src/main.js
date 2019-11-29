// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Jade from './Jade'
import Vuex from 'vuex'
import BootstrapVue from 'bootstrap-vue'

import router from './router'
import axios from 'axios';

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

require('../static/css/variables.css')
require('../static/css/jade.css')

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(Vuex)

const store = new Vuex.Store({

  state: {
    page: [],
    pages: [],
    main_menu: [],
    errors: [],
    current_name: '',
    current_path: '',
  },

  getters: {
    get_page: state => {
      return state.page
    },
    get_pages: state => {
      return state.pages
    },
    get_main_menu: state => {
      return state.main_menu
    },
    get_errors: state => {
      return state.errors
    },
    get_current_name: state => {
      return state.current_name
    },
    get_current_path: state => {
      return state.current_path
    },
  
    get_valign: state => {
      if (state.page == undefined) { return 'middle' }
      else { return state.page.valign }
    }
  },
  
  mutations: {
    set_pages (state, pages) {
      state.pages = pages
    },

    set_main_menu (state, menu) {
      state.main_menu = menu
    },

    set_current_page(state, {page, name, path}) {
      state.page = page
      state.current_name = name
      state.current_path = path
    },
    
    set_errors(state, e) {
      state.errors.push(e)
    }

  },

  actions: {

    fetch_pages (context) {
      axios.get('http://localhost:4000/api/v1/pages')
      .then(response => {
        var page
        for (page of response.data) {
      
        }
        context.commit('set_pages', response.data)
      })
      .catch(e => {
        context.commit('set_errors', e)
      })
    },

    fetch_main_menu (context) {
      axios.get('http://localhost:4000/api/v1/main-menu')
      .then(response => {
        // JSON responses are automatically parsed.
        context.commit('set_main_menu', response.data)
      })
      .catch(e => {
        context.commit('set_errors', e)
      })
    },

    fetch_current_page (context, {name, path}) {
      axios.get('http://localhost:4000/api/v1/pages/' + name)
      .then(response => {
        // JSON responses are automatically parsed.
        context.commit('set_current_page', {page: response.data[0], name: name, path: path}) 
      })
      .catch(e => {
        context.commit('set_errors', e)
      })
    }
  },
})

/* eslint-disable no-new */
new Vue({
  el: '#jade',
  router,
  store,
  components: { Jade },
  template: '<Jade/>'
})

export default {
  computed: {
    get_pages: function () {
      return this.$store.getters.get_pages
    },
    get_current_path: function () {
      return this.$store.getters.get_current_path
    }
  }
}