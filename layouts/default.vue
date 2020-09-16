<template>
  <a-layout class="layout">
    <a-layout-header
      style="
        display: flex;
        justify-content: center;
        position: fixed;
        width: 100%;
        z-index: 99999999;
      "
    >
      <a-menu
        theme="dark"
        mode="horizontal"
        :default-selected-keys="defaultKey"
        :style="{ lineHeight: '64px' }"
        @click="changePath"
      >
        <a-menu-item key="1">
          Home
        </a-menu-item>
        <a-menu-item key="2">
          Transformation
        </a-menu-item>
        <a-menu-item key="3">
          Conversion
        </a-menu-item>
      </a-menu>
    </a-layout-header>
    <a-layout-content style="padding: 0 50px; background-color: #ffffff;">
      <div :style="{ padding: '6em 24px 24px 24px', minHeight: '100vh' }">
        <Nuxt />
      </div>
    </a-layout-content>
    <!--    <a-layout-footer style="text-align: center;">-->
    <!--      Ant Design ©2018 Created by Ant UED-->
    <!--    </a-layout-footer>-->
  </a-layout>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

interface IMenuClicked {
  key: string
  keyPath: Array<string>
  item: Vue
  domEvent: MouseEvent
}
@Component
export default class DefaultLayout extends Vue {
  routes: Array<string> = ['/', '/transformation', '/conversion']

  changePath(event: IMenuClicked) {
    const { key } = event
    const keyInt: number = parseInt(key) - 1
    this.$router.push(this.routes[keyInt])
  }

  get defaultKey(): string[] {
    return [(this.routes.indexOf(this.$route.path) + 1).toString()]
  }
}
</script>
<style>
html {
  font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, 'Helvetica Neue', Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}
</style>
