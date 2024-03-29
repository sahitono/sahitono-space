module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
  },
  extends: [
    '@nuxtjs/eslint-config-typescript',
    'prettier',
    'prettier/vue',
    'plugin:prettier/recommended',
    'plugin:nuxt/recommended',
    'plugin:vue/essential',
  ],
  plugins: ['prettier'],
  // add your custom rules here
  rules: {
    'vue/component-definition-name-casing': ['error', 'PascalCase'],
  },
}
