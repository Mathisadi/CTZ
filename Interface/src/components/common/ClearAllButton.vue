<script>
import { grid } from "@/stores/gridProps.js";
import { routeSettigns } from "@/stores/routeSettings";
import { intersectionSettings } from "@/stores/intersectionSettings";
import { feuSettings } from "@/stores/feuSettings";
import { prioriteSettings } from "@/stores/prioriteSettings";
import { pietonSettings } from "@/stores/pietonSettings";
import { departSettings } from "@/stores/departSettings";
import { finSettings } from "@/stores/finSettings";

export default {
  setup() {
    // Stores
    const storeGrid = grid();
    const storeRoute = routeSettigns();
    const storeIntersection = intersectionSettings();
    const storeFeu = feuSettings();
    const storePriorite = prioriteSettings();
    const storePieton = pietonSettings();
    const storeDepart = departSettings();
    const storeFin = finSettings();

    const clear = () => {
      storeGrid.clear();
      storeRoute.clear();
      storeIntersection.clear();
      storeFeu.clear();
      storePriorite.clear();
      storePieton.clear();
      storeDepart.clear();
      storeFin.clear();
    }

    return {
      clear
    };
  },
};
</script>

<template>
  <button class="button-clear" @click="clear"> Clear All</button>
</template>

<style scoped>
.button-clear {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  height: 30px;
  background-color: #AE7676;
  color: var(--color-text);
  font-size: 12px;
  font-weight: 400;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.button-clear:hover {
  color: white;
}
</style>
