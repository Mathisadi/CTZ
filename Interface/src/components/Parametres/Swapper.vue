<script>
import Depart from "./Depart.vue";
import Feu from "./Feu.vue";
import Fin from "./Fin.vue";
import Intersection from "./Intersection.vue";
import Pieton from "./Pieton.vue";
import Priorite from "./Priorite.vue";
import Route from "./Route.vue";
import Settings from "./Settings.vue";
import { toolbarInteraction } from "@/stores/toolbarInteraction.js";

export default {
  components: {
    Depart,
    Feu,
    Fin,
    Intersection,
    Pieton,
    Priorite,
    Route,
    Settings,
  },

  setup() {
    const toolbarStore = toolbarInteraction();

    const test = () => {
      console.log(toolbarStore.isDepartToogle);
      console.log(toolbarStore.isRouteToogle);
      console.log(toolbarStore.isIntersectionToogle);
      console.log(toolbarStore.isFeuToogle);
      console.log(toolbarStore.isPietonToogle);
      console.log(toolbarStore.isPrioriteToogle);
      console.log(toolbarStore.isFinToogle);
    };

    return {
      toolbarStore,
      test
    };
  },
};
</script>

<template>
  <Depart v-if="toolbarStore.isDepartToogle" @click="test" />
  <Route v-else-if="toolbarStore.isRouteToogle" />
  <Intersection v-else-if="toolbarStore.isIntersectionToogle" />
  <Feu v-else-if="toolbarStore.isFeuToogle" />
  <Pieton v-else-if="toolbarStore.isPietonToogle" />
  <Priorite v-else-if="toolbarStore.isPrioriteToogle" />
  <Fin v-else-if="toolbarStore.isFinToogle" />
  <Settings v-else-if="toolbarStore.isParametresToogle" />
</template>
