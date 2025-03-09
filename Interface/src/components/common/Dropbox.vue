<script>
import { routeSettigns } from "@/stores/routeSettings";
import { feuSettings } from "@/stores/feuSettings";
import { prioriteSettings } from "@/stores/prioriteSettings";
import { pietonSettings } from "@/stores/pietonSettings";
import { departSettings } from "@/stores/departSettings";
import { finSettings } from "@/stores/finSettings";

import { ref, computed } from "vue";
import IconFleche from "../Icons/Fleche_bas.vue";

export default {
  props: ["type", "param"],
  components: {
    IconFleche,
  },
  setup(props) {
    const isOpen = ref(false);
    // Définition des listes initiales
    const initiale_dir = computed(() => {
      if (props.type === "depart" && props.param === "type") {
        return ["Voiture", "Piéton"];
      } else if (props.type === "pieton" && props.param === "sens") {
        return [
          [0, 2],
          [1, 3],
        ];
      } else if (props.type === "depart" && props.param === "etat") {
        return [true, false];
      } else if (props.type === "feu" && props.param === "etat") {
        return [true, false];
      } else {
        return [0, 1, 2, 3];
      }
    });

    const nom_dir = computed(() => {
      if (props.type === "depart" && props.param === "type") {
        return ["Voiture", "Piéton"];
      } else if (props.type === "pieton" && props.param === "sens") {
        return ["Horizontale", "Verticale"]
      } else if (props.type === "depart" && props.param === "etat") {
        return ["Actif", "Inactif"];
      } else if (props.type === "feu" && props.param === "etat") {
        return ["Actif", "Inactif"];
      } else {
        return ["Gauche", "Bas", "Droite", "Haut"];
      }
    });

    // Récupération des stores
    const storeRoute = routeSettigns();
    const storeFeu = feuSettings();
    const storePriorite = prioriteSettings();
    const storePieton = pietonSettings();
    const storeDepart = departSettings();
    const storeFin = finSettings();

    // Computed property pour gérer la valeur sélectionnée
    const selectedValue = computed({
      get() {
        let result;
        if (props.type === "route") {
          if (props.param === "sens") {
            result = storeRoute.sens_route;
          } else if (props.param === "direction") {
            result = storeRoute.direction_possible;
          }
        } else if (props.type === "feu") {
          if (props.param === "sens") {
            result = storeFeu.sens_route;
          } else if (props.param === "etat") {
            result = storeFeu.etat;
          }
        } else if (props.type === "priorite") {
          if (props.param === "sens") {
            result = storePriorite.sens_route;
          }
        } else if (props.type === "pieton") {
          if (props.param === "sens") {
            result = storePieton.sens_route;
          }
        } else if (props.type === "depart") {
          if (props.param === "type") {
            result = storeDepart.type_depart;
          } else if (props.param === "sens") {
            result = storeDepart.sens_route;
          } else if (props.param === "etat") {
            result = storeDepart.etat;
          }
        } else if (props.type === "fin") {
          if (props.param === "sens") {
            result = storeFin.sens_route;
          }
        }
        // Si aucune valeur n'est définie, renvoyer la valeur par défaut
        if (result === undefined || result === null) {
          result = isUniqueSelection.value ? "" : [];
        }

        return result;
      },
      set(newValue) {
        if (props.type === "route") {
          if (props.param === "sens") {
            storeRoute.sens_route = newValue;
          } else if (props.param === "direction") {
            storeRoute.direction_possible = newValue;
          }
        } else if (props.type === "feu") {
          if (props.param === "sens") {
            storeFeu.sens_route = newValue;
          } else if (props.param === "etat") {
            storeFeu.etat = newValue;
          }
        } else if (props.type === "priorite") {
          if (props.param === "sens") {
            storePriorite.sens_route = newValue;
          }
        } else if (props.type === "pieton") {
          if (props.param === "sens") {
            storePieton.sens_route = newValue;
          }
        } else if (props.type === "depart") {
          if (props.param === "type") {
            storeDepart.type_depart = newValue;
          } else if (props.param === "sens") {
            storeDepart.sens_route = newValue;
          } else if (props.param === "etat") {
            storeDepart.etat = newValue;
          }
        } else if (props.type === "fin") {
          if (props.param === "sens") {
            storeFin.sens_route = newValue;
          }
        }
      },
    });

    const toggleDropdown = () => {
      isOpen.value = !isOpen.value;
    };

    return {
      initiale_dir,
      nom_dir,
      isOpen,
      toggleDropdown,
      selectedValue,
    };
  },
};
</script>

<template>
  <div class="dropdown-wrapper">
    <button @click="toggleDropdown" class="dropdown">
      <!-- Affichage : si sélection non vide, on affiche directement pour unique, sinon on joint le tableau -->
      {{
        (selectedValue !== "" ? selectedValue : "None")
      }}
      <IconFleche />
    </button>
    <!-- Dropdown -->
    <ul v-if="isOpen" class="dropdown-menu">
      <li v-for="(item, index) in initiale_dir" :key="index">
        <label class="dropdown-item">
          <input
            :type="'radio'"
            :value="item"
            v-model="selectedValue"
            :name="''"
          />
          {{ nom_dir[index] }}
        </label>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.dropdown-wrapper {
  position: relative;
  display: inline-block;
}
.dropdown {
  flex: initial;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding-left: 10px;
  width: 120px;
  padding-bottom: 2px;
  background-color: transparent;
  color: white;
  font-size: 12px;
  font-weight: 400;
  border: none;
  border-bottom: var(--color-underline) solid 1px;
  cursor: pointer;
}
.dropdown-menu {
  position: absolute;
  z-index: 10;
  top: 100%;
  right: 0;
  width: 100%;
  list-style: none;
  padding: 8px 0 8px 20px;
  border-radius: 2px;
  margin-top: 2px;
  background-color: var(--color-underline);
  gap: 10px;
}
.dropdown-menu li {
  margin-bottom: 10px;
}
.dropdown-menu li:last-child {
  margin-bottom: 0;
}
.dropdown-item {
  display: flex;
  align-items: center;
  cursor: pointer;
  justify-content: left;
  font-size: 12px;
  gap: 20px;
}
</style>
