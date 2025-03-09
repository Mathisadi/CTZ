import { ref } from "vue";
import { defineStore } from "pinia";

export const pietonSettings = defineStore(
  "pietonSettings",
  () => {
    // Liste des parametres d'une route
    const nom = ref("");
    const sens_route = ref([0,2]);
    const len = ref(1);

    const testFilled = () => {
      return (
        (nom.value != "") & 
        (sens_route.value.length === 2)
      );
    };

    const clear = () => {
      nom.value = "";
      sens_route.value = [0,2];
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
      getPietonSettings,
      testFilled
    };
  },
  {
    persist: true,
  }
);
