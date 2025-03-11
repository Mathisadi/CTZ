<script>

import { grid } from "@/stores/gridProps.js";
import { updateCell } from "@/stores/updateCell";
import { mouvement } from "@/stores/mouvement.js";
import { useRoute } from "vue-router";
import { computed, toRefs } from "vue";

import Arrow_sens from "../Icons/Arrow_sens.vue";

export default {
  name: "Quadrillage",
  components: {
    Arrow_sens
  },
  setup() {
    // Stores
    const storeGrid = grid();
    const storeCell = updateCell();

    // Récupérer la route courante
    const route = useRoute();
    // Vérifier si nous sommes sur la page édition (adaptez la condition selon votre configuration de routes)
    const isEditionPage = computed(() => route.name === "Edition");

    // Constante grille
    const  { cols, rows } = toRefs(storeGrid);
    const { infoCell } = toRefs(storeGrid);

    // Drag
    const dragStore = mouvement();
    const startDrag = dragStore.startDrag;
    const onDrag = dragStore.onDrag;
    const endDrag = dragStore.endDrag;
    const offset = dragStore.offset;

    // Mise à jour des cellules
    const handleMajCell = (index) => {
      if (isEditionPage.value) {
        storeCell.majCell(index);
      }
    };

    
    return {
      cols,
      rows,
      offset,
      startDrag,
      onDrag,
      endDrag,
      storeCell,
      infoCell,
      handleMajCell
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
      v-for="(cell, index) in infoCell"
      :key="index"
      @click="handleMajCell(index)"
      :style="{ backgroundColor: cell.color }"
      class="cases"
    > {{ cell.nom }} <Arrow_sens :sens="cell.sens" /></div>
  </div>
</template>

<style scoped>
.quadrillage {
  display: grid;
  grid-template-columns: repeat(var(--cols), 100px);
  grid-template-rows: repeat(var(--rows), 100px);
}

.cases {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  color: var(--color-text);
  font-size: 10px;
  font-weight: 400;
  gap: 10px;

  border: 0.5px dashed var(--color-line);
  aspect-ratio: 1/1;
}
</style>
