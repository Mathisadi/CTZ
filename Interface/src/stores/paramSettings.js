import { ref } from "vue";
import { defineStore } from "pinia";

export const paramSettings = defineStore(
  "paramSettings",
  () => {
    // Liste des parametres d'une route
    const nom_projet = ref("");

    return {
      nom_projet,
    };
  },

  {
    persist: true,
  }
);
