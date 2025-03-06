import { ref } from "vue";
import { defineStore } from "pinia";

export const finSettings = defineStore(
  "finSettings",
  () => {
    // Liste des parametres d'une route*
    const nom = ref("");
    const sens_route = ref(0);
    const len = ref(1);

    const clear = () => {
      nom.value = "";
      sens_route.value = 0;
    };

    return {
      nom,
      sens_route,
      clear
    };
  },
  {
    persist: true,
  }
);
