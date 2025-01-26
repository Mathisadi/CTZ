<script>
import { ref } from "vue";
import { mouvement } from "@/stores/mouvement";

export default{
  name: "Quadrillage",
  setup() {
    // Constante de la grille
    const rows = ref(101);
    const nums = ref(Array.from({ length: rows.value }, (_, index) => index))
    const grid = ref(Array.from({ length: rows.value*2 }))
    
    // Drag value
    const dragStore = mouvement();
    const offset= dragStore.offset;

    return {
      rows,
      nums,
      offset,
      grid
    };
  },
}
</script>

<template>
  <div
    class="ruler_left"
    :style="{
      transform: `translate(0px, ${offset.y}px)`, // On ajoute 2 pour que se soit centrer sur le quadrillage
      '--cols': 2,
      '--rows': rows,
    }"
  >
    <div
      v-for="(_, index) in grid"
      :key="index"
      class="intervale"
    >{{ nums[index] }}</div>
  </div>
</template>

<style scoped>
.ruler_left {
  display: grid;
  grid-template-columns: repeat(var(--cols), 100px);
  grid-template-rows: repeat(var(--rows), 100px);
  grid-auto-flow: dense;
}

.ruler_left > :nth-child(3n + 1) { /* 2n + 1 cible les éléments de la première colonne */
  grid-row: span 2; /* Chaque élément occupe deux lignes */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: blue;
}

.ruler_left > div {
  background-color: red; /* Autres cases */
}

.intervale {
  border: 0.5px dashed var(--color-line);
  aspect-ratio: 1/1;
  color: var(--color-text);
  font-size: 8px;
  transform: rotate(-90deg);
}
</style>

  

  