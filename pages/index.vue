<template>
  <div>
    <h1 style="text-align: center;">Hi, my name is Sahit</h1>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import Proj4 from 'proj4'
import * as RefData from '../proj4_def.json'

interface IReferences {
  ref: string
  name: string
}

@Component
export default class IndexPage extends Vue {
  references: Array<IReferences> = RefData.tm3.concat(RefData.utm)
  inputCoordinates: string = ''

  inputProjection: string = this.references[0].ref
  outputProjection: string = this.references[6].ref

  transform(coordinate: Array<number>): number[] {
    return Proj4(this.inputProjection, this.outputProjection, coordinate)
  }

  get outputCoordinates(): string {
    const rows = this.inputCoordinates.split('\n')
    if (rows.length <= 1) {
      return ''
    }
    const transformed: Array<number[]> = []
    rows.forEach((row) => {
      const coordinates: Array<string> = row.split(',')
      const xyz: Array<number> = []
      coordinates.forEach((c) => {
        xyz.push(parseFloat(c))
      })

      if (
        xyz.every((e) => {
          return !isNaN(e)
        }) &&
        xyz.length >= 2
      ) {
        if (!isNaN(xyz[1])) {
          transformed.push(this.transform(xyz.slice(0, 2)))
        }
      }
    })
    return transformed.join('\n')
  }
}
</script>
<style></style>
