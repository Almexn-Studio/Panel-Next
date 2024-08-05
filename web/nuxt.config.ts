// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: false },
  modules: [
    '@ant-design-vue/nuxt',
    '@nuxtjs/tailwindcss',
    'nuxt-quasar-ui',
  ],
  css: ['~/assets/css/tailwind.css','~/assets/css/main.css'],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  quasar: {
    plugins: [
      'Loading'
     ]
  }
})
