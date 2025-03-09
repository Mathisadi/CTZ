import { ref } from "vue";
import { defineStore } from "pinia";

export const pietonSettings = defineStore(
  "pietonSettings",
  () => {
    // Liste des parametres d'une route*
    const nom = ref("");
    const sens_route = ref("");
    const len = ref(1);

    const clear = () => {
      nom.value = "";
      sens_route.value = "";
    };

    const getPietonSettings = () => {
      return {
        "type": "Pieton",
        "nom": nom.value,
        "sens": sens_route.value,
        "len": len.value
      };
    };

    return {
      sens_route,
      nom,
      clear,
      getPietonSettings
    };
  },
  {
    persist: true,
  }
);
