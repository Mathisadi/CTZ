import { ref } from "vue";
import { defineStore } from "pinia";

export const feuSettings = defineStore(
  "feuSettings",
  () => {
    // Liste des parametres d'une route*
    const nom = ref("");
    const sens_route = ref([]);
    const proba_gauche = ref(0);
    const proba_droite = ref(0);
    const proba_bas = ref(0);
    const proba_haut = ref(0);
    const cycle = ref("");

    return {
      sens_route,
      cycle,
      nom,
      proba_gauche,
      proba_droite,
      proba_bas,
      proba_haut,
    };
  },
  {
    persist: true,
  }
);
