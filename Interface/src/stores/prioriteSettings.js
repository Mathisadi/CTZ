import { ref } from "vue";
import { defineStore } from "pinia";

export const prioriteSettings = defineStore(
  "prioriteSettings",
  () => {
    // Liste des parametres d'une route*
    const nom = ref("");
    const sens_route = ref(0);
    const proba_gauche = ref(0);
    const proba_droite = ref(0);
    const proba_bas = ref(0);
    const proba_haut = ref(0);
    const len = ref(1);

    const clear = () => {
      nom.value = "";
      sens_route.value = 0;
      proba_gauche.value = 0;
      proba_droite.value = 0;
      proba_bas.value = 0;
      proba_haut.value = 0;
    };

    return {
      sens_route,
      nom,
      proba_gauche,
      proba_droite,
      proba_bas,
      proba_haut,
      clear
    };
  },
  {
    persist: true,
  }
);
