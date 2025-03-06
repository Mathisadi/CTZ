import { ref } from "vue";
import { defineStore } from "pinia";

export const finSettings = defineStore(
  "finSettings",
  () => {
    // Liste des parametres d'une route*
    const nom = ref("");
    const len = ref(1);

    const clear = () => {
      nom.value = "";
    };

    return {
      nom,
      clear
    };
  },
  {
    persist: true,
  }
);
