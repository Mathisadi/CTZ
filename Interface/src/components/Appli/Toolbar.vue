<script>
import { defineComponent, ref } from "vue";
import IconRoute from "../Icons/Route.vue";
import IconIntersection from "../Icons/Intersection.vue";
import IconFeu from "../Icons/Feu.vue";
import IconPriorite from "../Icons/Priorite.vue";
import IconPieton from "../Icons/Pieton.vue";
import IconDepart from "../Icons/Depart.vue";
import IconFin from "../Icons/Fin.vue";
import IconSelection from "../Icons/Selection.vue";
import IconParametre from "../Icons/Parametre.vue";
import { useToogleChoixStore } from "@/stores/toolbarInteraction.ts";

export default defineComponent({
  name: "Toolbar",
  components: {
    IconRoute,
    IconIntersection,
    IconFeu,
    IconPriorite,
    IconPieton,
    IconDepart,
    IconFin,
    IconSelection,
    IconParametre,
  },
  setup() {
    const toolbarStore = useToogleChoixStore();

    return {
      toolbarStore,
    };
  },
});
</script>

<template>
  <button
    class="icon"
    @click="toolbarStore.changeColor_route()"
    :style="{ backgroundColor: toolbarStore.bgColor_route }"
  >
    <IconRoute />Route
  </button>
  <button
    class="icon"
    @click="toolbarStore.changeColor_intersection()"
    :style="{ backgroundColor: toolbarStore.bgColor_intersection }"
  >
    <IconIntersection />Intersect°
  </button>
  <button
    class="icon"
    @click="toolbarStore.changeColor_feu()"
    :style="{ backgroundColor: toolbarStore.bgColor_feu }"
  >
    <IconFeu />Feu
  </button>
  <button
    class="icon"
    @click="toolbarStore.changeColor_priorite()"
    :style="{ backgroundColor: toolbarStore.bgColor_priorite }"
  >
    <IconPriorite />Priorité
  </button>
  <button
    class="icon"
    @click="toolbarStore.changeColor_pieton()"
    :style="{ backgroundColor: toolbarStore.bgColor_pieton }"
  >
    <IconPieton />Pieton
  </button>
  <button
    class="icon"
    @click="toolbarStore.changeColor_depart()"
    :style="{ backgroundColor: toolbarStore.bgColor_depart }"
  >
    <IconDepart />Depart
  </button>
  <button
    class="icon"
    @click="toolbarStore.changeColor_fin()"
    :style="{ backgroundColor: toolbarStore.bgColor_fin }"
  >
    <IconFin />Fin
  </button>
  <button
    class="icon"
    @click="toolbarStore.changeColor_selection()"
    :style="{ backgroundColor: toolbarStore.bgColor_selection }"
  >
    <IconSelection />Selection
  </button>
  <button
    class="icon_bas"
    @click="toolbarStore.changeColor_parametres()"
    :style="{ backgroundColor: toolbarStore.bgColor_parametres }"
  >
    <IconParametre />Paramètres
  </button>
</template>

<style >
.icon {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  aspect-ratio: 10/9;
  color: var(--color-text);
  border: none;
  cursor: pointer;
  gap: 10px;
  font-size: 10px;
  font-weight: 400;
}

.icon_bas {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  aspect-ratio: 1/1;
  color: var(--color-text);
  border: none;
  cursor: pointer;
  font-size: 10px;
  font-weight: 400;
  margin-top: auto; /* Pousse ce bouton vers le bas */
}


</style>
