import { ref } from "vue";
import { defineStore } from "pinia";

export const finSettings = defineStore(
  "finSettings",
  () => {
    // Liste des parametres d'une route*
    const nom = ref("");
    const sens_route = ref(0);
    const len = ref(1);

    const testFilled = () => {
      return (nom.value != "");
    };

    const clear = () => {
      nom.value = "";
      sens_route.value = 0;
    };

    const getFinSettings = () => {
      return {
        "type": "Fin",
        "nom": nom.value,
        "sens": Number(sens_route.value),
        "len": len.value
      };
    };

    return {
      nom,
      sens_route,
      clear,
      getFinSettings,
      testFilled
    };
  },
  {
    persist: true,
  }
);
