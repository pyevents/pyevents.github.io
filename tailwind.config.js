module.exports = {
  content: [
    './content/**/*.{html,md}',
    './output/**/*.html',
    './themes/pyevents/templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
  ],
}
