<script>

import { updateColorCell } from "@/stores/updateColorGrid";
import { errorMessages } from "@/stores/ErrorMessages";
import { mouvement } from "@/stores/mouvement.js";
import { grid } from "@/stores/grid.js";

export default {
  name: "Quadrillage",
  setup() {
    // Stores
    const storeGrid = grid();
    const storeColor = updateColorCell();
    const storeError = errorMessages();

    // Constante grille
    const cols = storeGrid.cols;
    const rows = storeGrid.rows;

    // Drag
    const dragStore = mouvement();
    const startDrag = dragStore.startDrag;
    const onDrag = dragStore.onDrag;
    const endDrag = dragStore.endDrag;
    const offset = dragStore.offset;
    
    return {
      cols,
      rows,
      offset,
      startDrag,
      onDrag,
      endDrag,
      storeColor,
      storeError
    };
  },
};
</script>

<template>
  <div
    class="quadrillage"
    @mousedown="startDrag"
    @mousemove="onDrag"
    @mouseup="endDrag"
    @mouseleave="endDrag"
    :style="{
      transform: `translate(${offset.x}px, ${offset.y}px)`,
      '--cols': cols,
      '--rows': rows,
    }"
  >
    <div
      v-for="(cell, index) in storeColor.couleurs"
      :key="index"
      @click="storeColor.changeColor(cell)"
      :style="{ backgroundColor: cell.color }"
      class="cases"
    ></div>
  </div>
</template>

<style scoped>
.quadrillage {
  display: grid;
  grid-template-columns: repeat(var(--cols), 100px);
  grid-template-rows: repeat(var(--rows), 100px);
}

.cases {
  border: 0.5px dashed var(--color-line);
  aspect-ratio: 1/1;
}
</style>
