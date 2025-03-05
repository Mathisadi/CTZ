import { ref } from "vue";
import { defineStore } from "pinia";

export const pietonSettings = defineStore(
  "pietonSettings",
  () => {
    // Liste des parametres d'une route*
    const nom = ref("");
    const sens_route = ref("");

    const clear = () => {
      nom.value = "";
      sens_route.value = "";
    };

    return {
      sens_route,
      nom,
      clear
    };
  },
  {
    persist: true,
  }
);
