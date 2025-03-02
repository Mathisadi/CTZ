<script>
import { routeSettigns } from "@/stores/routeSettings";
import { intersectionSettings } from "@/stores/intersectionSettings";
import { feuSettings } from "@/stores/feuSettings"; 

import { computed } from "vue";

export default {
  props: ["type", "param"],
  setup(props) {
    // Store route setting
    const storeRoute = routeSettigns();

    // Store intersection setting
    const storeIntersection = intersectionSettings();

    // Store feu setting
    const storeFeu = feuSettings();

    // Fonction qui renvoie le bon élément en fonction des props
    const selectedValue = computed({
      get() {
        if (props.type === "route") {
          if (props.param === "len") {
            return storeRoute.longeur;
          } else if (props.param === "nom") {
            return storeRoute.nom;
          } else if (props.param === "proba-gauche") {
            return storeRoute.proba_gauche;
          } else if (props.param === "proba-droite") {
            return storeRoute.proba_droite;
          } else if (props.param === "proba-bas") {
            return storeRoute.proba_bas;
          } else if (props.param === "proba-haut") {
            return storeRoute.proba_haut;
          }
        } else if (props.type === "intersection") {
          if (props.param === "nom") {
            return storeIntersection.nom;
          }
        } else if (props.type === "feu") {
          if (props.param === "cycle") {
            return storeFeu.cycle;
          }
        }
        return 0;
      },
      set(newValue) {
        if (props.type === "route") {
          if (props.param === "len") {
            storeRoute.longeur = newValue;
          } else if (props.param === "nom") {
            storeRoute.nom = newValue;
          } else if (props.param === "proba-gauche") {
            storeRoute.proba_gauche = newValue;
          } else if (props.param === "proba-droite") {
            storeRoute.proba_droite = newValue;
          } else if (props.param === "proba-bas") {
            storeRoute.proba_bas = newValue;
          } else if (props.param === "proba-haut") {
            storeRoute.proba_haut = newValue;
          }
        } else if (props.type === "intersection") {
          if (props.param === "nom") {
            storeIntersection.nom = newValue;
          }
        } else if (props.type === "feu") {
          if (props.param === "cycle") {
            storeFeu.cycle = newValue;
          }
        }
      }
    });

    return {
      selectedValue,
    };
  },
};
</script>

<template>
  <input
    class="input-container"
    v-model="selectedValue"
    type="text"
    placeholder="None"
  />
</template>

<style scoped>
.input-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 120px;
  padding-left: 10px;
  padding-right: 10px;
  padding-bottom: 4px;
  background-color: transparent;
  color: var(--color-text);
  font-size: 12px;
  font-weight: 400;
  border: none;
  border-bottom: var(--color-underline) solid 1px;
  cursor: pointer;
}

.input-container::placeholder {
  color: var(--color-text);
  font-size: 12px;
  font-weight: 400;
}

.input-container:focus {
  outline: none;
}
</style>
