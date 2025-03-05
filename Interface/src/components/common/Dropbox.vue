<script>
import { routeSettigns } from "@/stores/routeSettings";
import { feuSettings } from "@/stores/feuSettings";
import { prioriteSettings } from "@/stores/prioriteSettings";
import { pietonSettings } from "@/stores/pietonSettings";
import { departSettings } from "@/stores/departSettings";

import { ref, computed } from "vue";
import IconFleche from "../Icons/Fleche_bas.vue";

export default {
  props: ["type", "param"],
  components: {
    IconFleche,
  },
  setup(props) {
    // Variable réactive pour l'ouverture du dropdown
    const isOpen = ref(false);

    // Définition des listes initiale en fonction des props
    const initiale_dir = computed(() => {
      if (props.type === "depart" && props.param === "type") {
        return ["Voiture", "Piéton"];
      } else {
        return ["G", "B", "D", "H"];
      }
    });

    const nom_dir = computed(() => {
      if (props.type === "depart" && props.param === "type") {
        return ["Voiture", "Piéton"];
      } else {
        return ["Gauche", "Bas", "Droite", "Haut"];
      }
    });

    // Stores
    const storeRoute = routeSettigns();
    const storeFeu = feuSettings();
    const storePriorite = prioriteSettings();
    const storePieton = pietonSettings();
    const storeDepart = departSettings();

    // Propriété calculée pour gérer la valeur sélectionnée en tant que chaîne
    const selectedValue = computed({
      get() {
        if (props.type === "route") {
          if (props.param === "sens") {
            return storeRoute.sens_route || "";
          } else if (props.param === "direction") {
            return storeRoute.direction_possible || "";
          }
        } else if (props.type === "feu") {
          if (props.param === "sens") {
            return storeFeu.sens_route || "";
          }
        } else if (props.type === "priorite") {
          if (props.param === "sens") {
            return storePriorite.sens_route || "";
          }
        } else if (props.type === "pieton") {
          if (props.param === "sens") {
            return storePieton.sens_route || "";
          }
        } else if (props.type === "depart") {
          if (props.param === "type") {
            return storeDepart.type || "";
          } else if (props.param === "sens") {
            return storeDepart.sens_route || "";
          }
        }
        return "";
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
            storeDepart.type = newValue;
          } else if (props.param === "sens") {
            storeDepart.sens_route = newValue;
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
      {{ selectedValue !== "" ? selectedValue : "None" }}
      <IconFleche />
    </button>
    <!-- Affichage du dropdown -->
    <ul v-if="isOpen" class="dropdown-menu">
      <li v-for="(item, index) in initiale_dir" :key="index">
        <label class="dropdown-item">
          <!-- Utilisation d'un champ radio pour une sélection unique -->
          <input
            type="radio"
            :value="item"
            v-model="selectedValue"
            name="selection"
            @change="toggleDropdown"
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
