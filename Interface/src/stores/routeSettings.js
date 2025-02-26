import { ref } from "vue";
import { defineStore } from "pinia";

export const routeSettigns = defineStore(
  "routeSettings",
  () => {
    // Liste des parametres d'une route
    const sens_route = ref([]);
    const direction_possible = ref([]);
    const longeur = ref(0);

    return {
      sens_route,
      direction_possible,
      longeur,
    };
  },
  {
    persist: true,
  }
);
