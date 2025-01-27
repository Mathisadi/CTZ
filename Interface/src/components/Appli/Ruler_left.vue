<script>
import { ref } from "vue";
import { mouvement } from "@/stores/mouvement";

export default {
  name: "Quadrillage",
  setup() {
    // Constante de la grille
    const rows = ref(101);
    const nums = ref(Array.from({ length: rows.value }, (_, index) => index - 51));
    const grid = ref(Array.from({ length: rows.value }));

    // Drag value
    const dragStore = mouvement();
    const offset = dragStore.offset;

    return {
      rows,
      nums,
      offset,
      grid,
    };
  },
};
</script>

<template>
  <div
    class="chiffre_container"
    :style="{
      transform: `translate(0px, ${offset.y - 2.5 - 6.25}px)`, // la grid était décalée de 2 ?
      '--cols': 2,
      '--rows': rows,
    }"
  >
    <div v-for="(_, index) in grid" :key="index" class="chiffre">
      <p>{{ nums[index] }}</p>
    </div>
  </div>

  <div
    class="intervalle_container"
    :style="{
      transform: `translate(0px, ${offset.y - 2.5}px)`, // la grid était décalée de 2 ?
      '--cols': 2,
      '--rows': rows,
    }"
  >
    <div v-for="(_, index) in grid" :key="index" class="intervalle"></div>
  </div>
</template>

<style scoped>
.chiffre_container {
  display: grid;
  grid-template-columns: 14px;
  grid-template-rows: repeat(var(--rows), 100px);
}

.chiffre {
  /* 2n + 1 cible les éléments de la première colonne */
  display: flex;
  justify-content: center;
  align-items: center;
  color: var(--color-text);
  font-size: 8px;
  align-self: auto;
  transform: rotate(-90deg);
  aspect-ratio: 1/1;
  height: 14px;
  width: 14px;
}

.intervalle_container {
  display: grid;
  grid-template-columns: 6px;
  grid-template-rows: repeat(var(--rows), 100px);
}

.intervalle {
  /* 2n + 1 cible les éléments de la première colonne */
  border-top: var(--color-line) 1px solid;
}
</style>
