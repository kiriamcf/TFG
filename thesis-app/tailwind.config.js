const defaultTheme = require('tailwindcss/defaultTheme');

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './resources/**/*.blade.php',
    './resources/**/*.js',
    './resources/**/*.vue',
  ],
  theme: {
    extend: {
      colors: {
        'main-gray': '#2A2E35',
        'main-gray-soft': '#BAC5D7',
        'main-orange': '#BB871E',
        'main-white': '#F1F1E6',
        'main-blue-dark': '#21687F',
        'main-blue-light': '#12B0B4',
        'main-blue-light-opacity': 'rgba(18, 176, 180, .8)',
        'main-green': '#76FAC7',
        'main-black': '#0E0E12',
        'secondary-black': '#17171A',
        'main-pink': '#6333FF',
      },
      fontFamily: {
        sans: ['Sora', ...defaultTheme.fontFamily.sans],
      },
      boxShadow: {
        'custom-button-blue': 'inset 0 0 0 3px #21687F',
        'custom-button-white': 'inset 0 0 0 3px #fff',
      },
    },
  },
  plugins: [],
};
