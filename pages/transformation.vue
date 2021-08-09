<template>
  <div>
    <a-row type="flex" justify="space-around">
      <a-col :span="10">
        <a-divider orientation="left">Input</a-divider>
        <a-select
          v-model="inputProjection"
          show-search
          type="flex"
          style="width: 100%; margin-bottom: 0.5rem;"
        >
          <a-select-option
            v-for="(data, index) in references"
            :key="index"
            :value="data.ref"
            >{{ data.name }}</a-select-option
          >
        </a-select>
        <a-textarea
          v-model="inputCoordinates"
          placeholder="Input Coordinate in format: x,y or longitude, latitude"
          :rows="11"
      /></a-col>
      <a-col :span="10">
        <a-divider orientation="left">Output</a-divider>
        <a-select
          v-model="outputProjection"
          show-search
          type="flex"
          style="width: 100%; margin-bottom: 0.5rem;"
          :default-value="references[6].ref"
        >
          <a-select-option
            v-for="(data, index) in references"
            :key="index"
            :value="data.ref"
            >{{ data.name }}</a-select-option
          >
        </a-select>
        <a-textarea
          v-model="outputCoordinates"
          placeholder="Output Coordinate"
          :rows="11"
      /></a-col>
    </a-row>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import Proj4 from 'proj4'
import * as RefData from '~/proj4_def.json'

interface IReferences {
  ref: string
  name: string
}

@Component
export default class TransformationPage extends Vue {
  references: Array<IReferences> = RefData.itrf.concat(
    RefData.tm3.concat(RefData.utm)
  )

  inputCoordinates: string = ''

  inputProjection: string = this.references[1].ref
  outputProjection: string = this.references[6].ref

  transform(coordinate: Array<number>): number[] {
    return Proj4(this.inputProjection, this.outputProjection, coordinate)
  }

  searchProjection(projectionName: string): Array<IReferences> {
    return this.references.filter((r) => {
      return r.name.search(projectionName)
    })
  }

  get outputCoordinates(): string {
    const rows: Array<string> = this.inputCoordinates.split('\n')

    const transformed: Array<number[]> = []
    rows.forEach((row) => {
      if (/[,]/.test(row)) {
        const coordinates: Array<string> = row.split(',')
        const xyz: Array<number> = []
        coordinates.forEach((c) => {
          const parsed = parseFloat(c)
          const coordinate = isNaN(parsed) ? 0 : parsed
          xyz.push(coordinate)
        })
        if (!isNaN(xyz[0])) {
          transformed.push(this.transform(xyz))
        }
      }
    })
    return transformed.join('\n')
  }

  // async mounted(){
  //   fetch("/proj4_def.json")
  // }
}
</script>
<style></style>
