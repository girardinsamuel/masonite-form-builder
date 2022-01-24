const mix = require('laravel-mix')
const path = require("path")
const src = 'src/form_builder/assets'
const dest = 'tests/integrations/storage/compiled'

// mix.setPublicPath('./tests/integrations/storage/compiled')

mix.postCss(`${src}/formbuilder.css`, `${dest}/css`, [
  require("tailwindcss")
])
mix.setPublicPath(".")
mix.js(`${src}/js/app.js`, `${dest}/js`)
mix.vue({"extractStyles": true})
mix.extract([
    'vue'
])
mix.alias({
  "@": path.resolve("src/form_builder/assets/js/"),
})
mix.sourceMaps()
