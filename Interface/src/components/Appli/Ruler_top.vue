<script>
import { ref } from "vue";
import { mouvement } from "@/stores/mouvement.js";

export default {
  name: "Ruler_top",
  setup() {
    // Constante de la grille
    const cols = ref(101);
    const nums = ref(Array.from({ length: cols.value }, (_, index) => index));
    const grid = ref(Array.from({ length: cols.value }));

    // Drag value
    const dragStore = mouvement();
    const offset = dragStore.offset;

    return {
      cols,
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
      transform: `translate(${offset.x + 17.5 - 6.75}px, 0px)`, // la grid était décalée de 2 ?
      '--cols': cols,
      '--rows': 1,
    }"
  >
    <div v-for="(_, index) in grid" :key="index" class="chiffre">
      <p>{{ nums[index] - 51 }}</p>
    </div>
  </div>

  <div
    class="intervalle_container"
    :style="{
      transform: `translate(${offset.x + 17.5}px, 0px)`, // la grid était décalée de 2 ?
      '--cols': cols,
      '--rows': 1,
    }"
  >
    <div v-for="(_, index) in grid" :key="index" class="intervalle"></div>
  </div>
</template>

<style scoped>
.chiffre_container {
  display: grid;
  grid-template-columns: repeat(var(--cols), 100px);
  grid-template-rows: 14px;
}

.chiffre {
  display: flex;
  justify-content: center;
  align-items: center;
  color: var(--color-text);
  font-size: 8px;
  aspect-ratio: 1/1;
  height: 14px;
}

.intervalle_container {
  display: grid;
  grid-template-columns: repeat(var(--cols), 100px);
  grid-template-rows: 6px;
}

.intervalle {
  border-left: var(--color-line) 1px solid;
}

</style>
