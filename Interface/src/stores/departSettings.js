import { ref } from "vue";
import { defineStore } from "pinia";

export const departSettings = defineStore(
  "departSettings",
  () => {
    // Liste des parametres d'une route
    const nom = ref("");
    const sens_route = ref(0);
    const type_depart = ref("Voiture");
    const densite = ref(0)
    const etat = ref(true);
    const cycle = ref("");
    const proba_gauche = ref(0);
    const proba_droite = ref(0);
    const proba_bas = ref(0);
    const proba_haut = ref(0);
    const len = ref(1);

    const clear = () => {
      nom.value = "";
      sens_route.value = 0;
      type_depart.value = "Voiture";
      densite.value = 0;
      etat.value = true;
      cycle.value = "";
      proba_gauche.value = 0;
      proba_droite.value = 0;
      proba_bas.value = 0;
      proba_haut.value = 0;
    }
    
    const getDepartSettings = () => {
      if (type_depart.value == "Voiture") {
        return {
          "type": "Depart",
          "nom": nom.value,
          "sens": sens_route.value,
          "densite": densite.value,
          "proba_g": proba_gauche.value,
          "proba_d": proba_droite.value,
          "proba_b": proba_bas.value,
          "proba_h": proba_haut.value,
        };
      } else {
        return {
          "type": "Depart_pieton",
          "nom": nom.value,
          "sens": sens_route.value,
          "densite": densite.value,
          "etat": etat.value,
          "cycle": cycle.value
        };
      }
      
    };

    return {
      type_depart,
      cycle,
      proba_gauche,
      proba_droite,
      proba_bas,
      proba_haut,
      nom,
      sens_route,
      densite,
      etat,
      clear,
      getDepartSettings
    };
  },
  {
    persist: true,
  }
);
