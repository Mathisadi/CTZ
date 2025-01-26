<script>
import { defineComponent, ref } from "vue";
import { useToogleChoixStore } from "@/stores/toolbarInteraction.ts";

export default defineComponent({
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

    // Constante du zoom et drag
    const offset = ref({ x: -5100, y: -5100 });
    const startPosition = ref({ x: 0, y: 0 });
    const isDraging = ref(false);

    // Drag
    const startDrag = (event) => {
      isDraging.value = true;
      startPosition.value = { x: event.clientX, y: event.clientY };
    };

    const onDrag = (event) => {
      if (isDraging.value) {
        const dx = event.clientX - startPosition.value.x;
        const dy = event.clientY - startPosition.value.y;
        offset.value.x += dx;
        offset.value.y += dy;
        startPosition.value = { x: event.clientX, y: event.clientY };
      }
    };

    const endDrag = () => {
      isDraging.value = false;
    };

    // Constante couleur
    const color_route = "#76ABAE";
    const color_intersection = "#AE7676";
    const color_priorite = "#AEA176";
    const color_feu = "#A176AE";
    const color_depart = "#76ABAE";
    const color_fin = "#AE7676";
    const color_pieton = "#AE7676";

    // Etats des boutons
    const toolbarStore = useToogleChoixStore();

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
      console.log(grid.value[index])
    }


    return {
      grid,
      cols,
      rows,
      offset,
      startPosition,
      isDraging,
      startDrag,
      onDrag,
      endDrag,
      change_color
    };
  },
});
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
.quadrillage-container {
  position: absolute;
  top: 5vh;
  left: 5vw;
  height: 95vh;
  width: 95vw;
  overflow: hidden;
}


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
