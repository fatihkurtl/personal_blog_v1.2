// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  buildModules: [
    "@nuxtjs/tailwindcss",
    "@nuxt-color-mode",
    "@nuxtjs/google-fonts",
    "@vueuse/nuxt",
    "@nuxtjs/dotenv",
    "@nuxt/content",
    "highlight.js",
    "@nuxtjs/markdownit",
  ],
  app: {
    pageTransition: { name: "page", mode: "out-in" },
  },
  markdownit: {
    runtime: true,
    preset: "default",
    linkify: true,
    breaks: true,
    injected: true,
    use: [["markdown-it-highlightjs"]],
  },
  content: {
    markdown: {
      prism: {
        theme: "prism-themes/themes/prism-material-oceanic.css",
      },
    },
  },
  ssr: true, // remove the mode option
  vite: {
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: '@import "@/assets/scss/variables.scss";',
        },
      },
    },
    server: {
      middlewareMode: true,
      middlewares: [
        (req, res, next) => {
          res.setHeader(
            "Set-Cookie",
            `myCookie=value; SameSite=${process.env.COOKIE_SAMESITE}; Secure`
          );

          next();
        },
      ],
    },
  },
  colorMode: {
    preference: "system",
    fallback: "light",
    hid: "nuxt-color-mode-script",
    globalName: "__NUXT_COLOR_MODE__",
    componentName: "ColorScheme",
    classPrefix: "",
    classSuffix: "-mode",
    storageKey: "nuxt-color-mode",
  },
  resolve: {
    // remove the alias option and add the resolve option
    alias: {
      assets: "/<rootDir>/assets",
    },
  },
  head: {
    script: [
      {
        src: "https://kit.fontawesome.com/7f90a92925.js",
        crossorigin: "anonymous",
      },
      {
        src: "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.2.1/highlight.min.js",
      },
      {
        type: "text/javascript",
        src: "https://cdnjs.cloudflare.com/ajax/libs/markdown-it/11.0.1/markdown-it.min.js ",
      },
    ],
    link: [
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/icon?family=Material+Icons+Outlined",
      },
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css?family=Inter",
      },
      {
        rel: "stylesheet",
        href: "cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css",
      },
    ],
  },
  css: ["~/assets/css/main.css"],
  modules: [
    "@pinia/nuxt",
    '@pinia-plugin-persistedstate/nuxt',
    '@nuxtjs/tailwindcss',
    "@nuxtjs/google-fonts",
    '@nuxtjs/color-mode',
  ],
  googleFonts: {
    families: { "Material+Icons": true },
  },
  build: {
    // remove the postcss option and add the build.postcss option
    postcss: { plugins: { tailwindcss: {}, autoprefixer: {} } },
  },
  router: {
    // remove the routeRules option and add the router.extendRoutes option
    extendRoutes(routes, resolve) {
      // modify the routes array as you wish
    },
  },
})
