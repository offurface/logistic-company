import '../sass/app.sass'
import Vue from 'vue'
import store from './store'

import './plugins'
import './components'

Vue.config.productionTip = false

new Vue({ // eslint-disable-line no-new
  el: '#app',
  store
})
