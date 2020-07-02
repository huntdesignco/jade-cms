// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuex from 'vuex'
import BootstrapVue from 'bootstrap-vue'
import axios from 'axios';

import Jade from './Jade'
import HTMLRenderer from '@/components/HTMLRenderer.vue'
import PageNotFound from '@/components/PageNotFound.vue'

import router from './router'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

require('../static/css/variables.css')
require('../static/css/jade.css')

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(Vuex)

axios.defaults.baseURL = process.env.API_URL;

const store = new Vuex.Store({

  state: {
    page: [],
    pages: [],
    main_menu: [],
    errors: [],
    current_name: null,
    current_path: null,
    page_routes: [],
    page_content: null
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
    },
    get_routes: state => {
      return state.routes
    },
    get_page_content: state => {
      return state.page_content
    },
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
    },
    set_routes(state, routes) {
      state.routes = routes
    },
    set_page_content(state, content) {
      state.page_content = content
    }

  },

  actions: {
    fetch_pages (context) {
      axios.get('/api/v1/pages')
      .then(response => {
        var page, route, routes = []
        for (page of response.data) {
          if (page.component == 'HTMLRenderer') { 
            route = {'name': page.name, 'path': page.slug, 'component': HTMLRenderer}
          }
          routes.push(route)
        }
        route = { path: "*", component: PageNotFound }
        routes.push(route)

        router.addRoutes(routes)

        context.commit('set_routes', routes)
        context.commit('set_pages', response.data)
      })
      .catch(e => {
        context.commit('set_errors', e)
      })
    },

    fetch_main_menu (context) {
      axios.get('/api/v1/main-menu')
      .then(response => {
        // JSON responses are automatically parsed.
        context.commit('set_main_menu', response.data)
      })
      .catch(e => {
        context.commit('set_errors', e)
      })
    },

    fetch_current_page (context, {name, path}) {
      if (path == '/') { name = 'index' }

      axios.get('/api/v1/pages' + path)
      .then(response => {
        var page
        page = response.data[0]
        // JSON responses are automatically parsed.

        context.commit('set_current_page', {page: page, name: name, path: path}) 
        context.dispatch('fetch_page_content', {page: page, path: path})

      })
      .catch(e => {
        context.commit('set_errors', e)
      })
    },

    fetch_page_content( context, {page, path} ) {
      if (page.component == 'HTMLRenderer') {
        if (path == '/') { path = '/index' }

        axios.get('/api/v1/pages' + path + '/content', { responseType: 'text' })
        .then(response => {
          context.commit('set_page_content', response.data)
        })
        .catch(e => {
          context.commit('set_errors', e)
        })
      }
    }

  }
  
})

/* eslint-disable no-new */
new Vue({
  el: '#jade',
  router,
  store,
  components: { Jade },
  template: '<Jade/>'
})