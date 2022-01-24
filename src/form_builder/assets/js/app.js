import { createApp } from "vue"


import CrafterConfig from './core/Crafter.js'

// TODO: In vue 3 ?
// Vue.config.silent = false;
// Vue.config.devtools = true;
// Vue.config.productionTip = false

// window._ = require('underscore');

// require('./bootstrap/globals');
// require('./bootstrap/mixins');
// require('./bootstrap/components');
// require('./bootstrap/fieldtypes');

// import axios from 'axios'
// import PortalVue from "portal-vue";
// import VModal from "vue-js-modal";
// Vue.use(PortalVue)
// Vue.use(VModal, { componentName: 'vue-modal' })

// Crafter.booting(Crafter => {
//   console.log("booting")
//   // add default stuff when booting
// });

const vueApp = createApp(CrafterConfig)
// import base UI components used in field types

// import all field types
import TextFieldtype from "@/components/fieldtypes/TextFieldtype.vue"
vueApp.component("text-fieldtype", TextFieldtype)
vueApp.mount("#crafter")

window.Crafter = vueApp
