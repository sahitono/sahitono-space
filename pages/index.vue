<template>
  <div>
    <h1 style="text-align: center;">Hi, my name is Sahit</h1>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

interface IReferences {
  ref: string
  name: string
}

@Component
export default class IndexPage extends Vue {}
</script>
<style></style>
