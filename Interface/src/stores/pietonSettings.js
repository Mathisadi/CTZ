import { ref } from "vue";
import { defineStore } from "pinia";

export const pietonSettings = defineStore(
  "pietonSettings",
  () => {
    // Liste des parametres d'une route*
    const nom = ref("");
    const sens_route = ref([]);

    return {
      sens_route,
      nom,
    };
  },
  {
    persist: true,
  }
);
