<script>
import { routeSettigns } from "@/stores/routeSettings";
import { intersectionSettings } from "@/stores/intersectionSettings";
import { feuSettings } from "@/stores/feuSettings";
import { prioriteSettings } from "@/stores/prioriteSettings";
import { pietonSettings } from "@/stores/pietonSettings";
import { departSettings } from "@/stores/departSettings";
import { finSettings } from "@/stores/finSettings";


import IconFleche from "../Icons/Fleche_bas.vue";

export default {
  props: ["type"],
  components: {
    IconFleche,
  },
  setup(props) {
    // Stores
    const storeRoute = routeSettigns();
    const storeIntersection = intersectionSettings();
    const storeFeu = feuSettings();
    const storePriorite = prioriteSettings();
    const storePieton = pietonSettings();
    const storeDepart = departSettings();
    const storeFin = finSettings();

    const clear = () => {
      if (props.type === "route") {
        storeRoute.clear();
      } else if (props.type === "intersection") {
        storeIntersection.clear();
      } else if (props.type === "feu") {
        storeFeu.clear();
      } else if (props.type === "priorite") {
        storePriorite.clear();
      } else if (props.type === "pieton") {
        storePieton.clear();
      } else if (props.type === "depart") {
        storeDepart.clear();
      } else if (props.type === "fin") {
        storeFin.clear();
      }
    }

    return {
      clear
    };
  },
};
</script>

<template>
  <button class="button-clear" @click="clear"> Clear </button>
</template>

<style scoped>
.button-clear {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  height: 30px;
  background-color: var(--color-title);
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
