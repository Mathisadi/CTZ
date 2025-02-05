<script>
import { ref } from "vue";
import { toolbarInteraction } from "@/stores/toolbarInteraction.js";
import { mouvement } from "@/stores/mouvement.js";
import { grid } from "@/stores/grid.js";

export default {
  name: "Quadrillage",
  setup() {
    // Constante de la grille
    const storeGrid = grid();
    const cols = storeGrid.cols;
    const rows = storeGrid.rows;
    const couleurs = ref(
      Array.from({ length: rows * cols }, () => ({ color: "#222831" }))
    );

    // Drag
    const dragStore = mouvement();
    const startDrag = dragStore.startDrag;
    const onDrag = dragStore.onDrag;
    const endDrag = dragStore.endDrag;
    const offset = dragStore.offset;

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
        couleurs.value[index].color = color_route;
      }

      if (toolbarStore.isIntersectionToogle) {
        couleurs.value[index].color = color_intersection;
      }

      if (toolbarStore.isFeuToogle) {
        couleurs.value[index].color = color_feu;
      }

      if (toolbarStore.isPrioriteToogle) {
        couleurs.value[index].color = color_priorite;
      }

      if (toolbarStore.isDepartToogle) {
        couleurs.value[index].color = color_depart;
      }

      if (toolbarStore.isFinToogle) {
        couleurs.value[index].color = color_fin;
      }

      if (toolbarStore.isPietonToogle) {
        couleurs.value[index].color = color_pieton;
      }
    };

    return {
      couleurs,
      cols,
      rows,
      offset,
      startDrag,
      onDrag,
      endDrag,
      change_color,
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
      v-for="(cell, index) in couleurs"
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
