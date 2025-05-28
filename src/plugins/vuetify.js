// src/plugins/vuetify.js

// 1. Import Vuetify core
import { createVuetify } from 'vuetify'
// 2. Bring in all Vuetify components & directives
import * as components from 'vuetify/components'
import * as directives  from 'vuetify/directives'
// 3. Import Material Design Icons + Vuetify’s base styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// 4. Export a Vuetify instance with your theme & icon settings
export default createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
  },
  theme: {
    defaultTheme: 'light',
    themes: {
      light: {
        colors: {
          primary:   '#1976D2',
          secondary: '#424242',
          accent:    '#82B1FF',
          background:'#F5F7FA',
        }
      }
    }
  }
})
