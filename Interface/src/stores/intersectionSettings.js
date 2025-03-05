import { ref } from "vue";
import { defineStore } from "pinia";

export const intersectionSettings = defineStore(
  "intersectionSettings",
  () => {
    // Liste des parametres d'une route*
    let nom = ref("");
    
    return {
      nom
    };
  },
  {
    persist: true,
  }
);
