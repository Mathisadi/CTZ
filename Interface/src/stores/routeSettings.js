import { ref } from "vue";
import { defineStore } from "pinia";

export const routeSettigns = defineStore(
  "routeSettings",
  () => {
    // Liste des parametres d'une route*
    let nom = ref("None");
    let sens_route = ref([]);
    let direction_possible = ref([]);
    let longeur = ref(0);

    return {
      sens_route,
      direction_possible,
      longeur,
      nom
    };
  },
  {
    persist: true,
  }
);
