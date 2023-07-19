/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
    "./app.vue",
    "./node_modules/flowbite.{js,ts}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: [
          "Outfit",
          "ui-sans-serif",
          "system-ui",
          "-apple-system",
          "BlinkMacSystemFont",
          "Segoe UI",
          "Roboto",
          "Helvetica Neue",
          "Arial",
          "Noto Sans",
          "sans-serif",
          "Apple Color Emoji",
          "Segoe UI Emoji",
          "Segoe UI Symbol",
          "Noto Color Emoji",
        ],
      },
      tabSize: {
        4: "4",
      },
      colors: {
        primary: {
          light: "#4c4c4c",
          DEFAULT: "#222222",
          dark: "#1f1f1f",
        },
        secondary: {
          light: "#f6f6f6",
          DEFAULT: "#f0f0f0",
          dark: "#e1e1e1",
        },
        accent: {
          light: "#feb2b2",
          DEFAULT: "#fc8181",
          dark: "#c53e3e",
        },
      },
    },
    variants: {
      display: ["responsive", "group-hover", "group-focus"],
    },
    fontFamily: {
      // Diğer font-family sınıfları...
      outfit: [
        "Outfit",
        "ui-sans-serif",
        "system-ui",
        "-apple-system",
        "BlinkMacSystemFont",
        "Segoe UI",
        "Roboto",
        "Helvetica Neue",
        "Arial",
        "Noto Sans",
        "sans-serif",
        "Apple Color Emoji",
        "Segoe UI Emoji",
        "Segoe UI Symbol",
        "Noto Color Emoji",
      ],
    },
    extend: {},
    container: {
      center: true,
    },
  },
  css: ["~/assets/css/main.css"],
  plugins: [
    require("flowbite/plugin"),
    // require("tailwindcss-dark-mode")(),
    require("@tailwindcss/typography"),
  ],
};
