<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "Quadrillage",
  setup() {
    const cols = ref(100);
    const rows = ref(100);

    const grid = ref(
      Array.from({ length: rows.value * cols.value }, () => ({ color: '#ffffff' }))
    );

    console.log(1)
    console.log(grid.value);
    console.log(grid.value[0].color)

    return {
      grid,
      cols,
      rows
    };
  },
})
</script>

<template>
  <div class="quadrillage" :style="{ '--cols': cols, '--rows': rows }">
    <div
      v-for="(cell, index) in grid"
      :key="index"
      :style="{ backgroundColor: cell.color }"
      class="line"
    ></div>
  </div>
</template>

<style scoped>
.quadrillage {
  position: absolute;
  display: grid;
  grid-template-columns: repeat(var(--cols), 1fr);
  grid-template-rows: repeat(var(--rows), 1fr);
  top: 5vh;
  left: 5vw;
  height: 95vh;
  width: 95vw;
  overflow: hidden;
}

.line {
  border: 0.5px dashed var(--color-line);
  aspect-ratio: 1/1;
}
</style>
