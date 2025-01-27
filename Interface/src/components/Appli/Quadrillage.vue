<script>
import { ref } from "vue";
import { toolbarInteraction } from "@/stores/toolbarInteraction.js";
import { mouvement } from "@/stores/mouvement.js";

export default{
  name: "Quadrillage",
  setup() {
    // Constante de la grille
    const cols = ref(101);
    const rows = ref(101);
    const grid = ref(
      Array.from({ length: rows.value * cols.value }, () => ({
        color: "#222831",
      }))
    );
    
    // Drag
    const dragStore = mouvement();
    const startDrag = dragStore.startDrag;
    const onDrag = dragStore.onDrag;
    const endDrag = dragStore.endDrag;
    const offset= dragStore.offset;

    // Constante couleur
    const color_route = "#76ABAE";
    const color_intersection = "#AE7676";
    const color_priorite = "#AEA176";
    const color_feu = "#A176AE";
    const color_depart = "#76ABAE";
    const color_fin = "#AE7676";
    const color_pieton = "#AE7676";

    // Etats des boutons
    const toolbarStore = toolbarInteraction();

    const change_color = (index) => {
      if (toolbarStore.isRouteToogle) {
        grid.value[index].color = color_route;
      }

      if (toolbarStore.isIntersectionToogle) {
        grid.value[index].color = color_intersection;
      }

      if (toolbarStore.isFeuToogle) {
        grid.value[index].color = color_feu;
      }

      if (toolbarStore.isPrioriteToogle) {    
        grid.value[index].color = color_priorite;
      }

      if (toolbarStore.isDepartToogle) {
        grid.value[index].color = color_depart;
      }

      if (toolbarStore.isFinToogle) {
        grid.value[index].color = color_fin;
      }

      if (toolbarStore.isPietonToogle) {
        grid.value[index].color = color_pieton;
      }
    }


    return {
      grid,
      cols,
      rows,
      offset,
      startDrag,
      onDrag,
      endDrag,
      change_color
    };
  },
}
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
      v-for="(cell, index) in grid"
      :key="index"
      @click="change_color(index)"
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
