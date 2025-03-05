import { ref } from "vue";
import { defineStore } from "pinia";

export const departSettings = defineStore(
  "departSettings",
  () => {
    // Liste des parametres d'une route*
    const nom = ref("");
    const type = ref("Voiture");
    const densite = ref(0)
    const etat = ref(true);
    const cycle = ref("");

    const clear = () => {
      nom.value = "";
      type.value = "Voiture";
      densite.value = 0;
      etat.value = true;
      cycle.value = "";
    }

    return {
      type,
      cycle,
      nom,
      densite,
      etat,
      clear
    };
  },
  {
    persist: true,
  }
);
