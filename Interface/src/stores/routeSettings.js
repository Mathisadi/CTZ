import { ref } from "vue";
import { defineStore } from "pinia";

export const routeSettigns = defineStore(
  "routeSettings",
  () => {
    // Liste des parametres d'une route*
    const nom = ref("");
    const sens_route = ref(0);
    const longeur = ref(0);

    const clear = () => {
      nom.value = "";
      sens_route.value = 0;
      longeur.value = 0;
    };

    const getRouteSettings = () => {
      return {
        "nom": nom.value,
        "sens": sens_route.value,
        "len": longeur.value,
      };
    };

    return {
      sens_route,
      longeur,
      nom,
      clear,
      getRouteSettings
    };
  },
  {
    persist: true,
  }
);
