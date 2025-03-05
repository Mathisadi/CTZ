<script>
import { routeSettigns } from "@/stores/routeSettings";
import { feuSettings } from "@/stores/feuSettings";
import { prioriteSettings } from "@/stores/prioriteSettings";
import { pietonSettings } from "@/stores/pietonSettings";

import { ref, computed } from "vue";
import IconFleche from "../Icons/Fleche_bas.vue";

export default {
  props: ["type", "param"],
  components: {
    IconFleche,
  },
  setup(props) {
    // Liste des params des directions (affichés dans la dropbox)
    if (props.type === "route") {
      
    }
    const initiale_dir = ["G", "B", "D", "H"];
    const nom_dir = ["Gauche", "Bas", "Droite", "Haut"];
    const isOpen = ref(false);

    // Store route setting
    const storeRoute = routeSettigns();

    // Store feu setting
    const storeFeu = feuSettings();

    // Store priorite setting
    const storePriorite = prioriteSettings();

    // Store pieton setting
    const storePieton = pietonSettings();

    // Fonction qui renvoie le bon élément en fonction des props
    const selectedValue = computed({
      get() {
        if (props.type === "route") {
          if (props.param === "sens") {
            return storeRoute.sens_route;
          } else if (props.param === "direction") {
            return storeRoute.direction_possible;
          }
        } else if (props.type === "feu") {
          if (props.param === "sens") {
            return storeFeu.sens_route;
          }
        } else if (props.type === "priorite") {
          if (props.param === "sens") {
            return storePriorite.sens_route;
          }
        } else if (props.type === "pieton") {
          if (props.param === "sens") {
            return storePieton.sens_route;
          }
        }
        return [];
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
      {{ selectedValue.length != 0 ? selectedValue.join(", ") : "None" }}
      <IconFleche />
    </button>
    <!-- Si on ouvre la dropbox -->
    <ul v-if="isOpen" class="dropdown-menu">
      <li v-for="(item, index) in initiale_dir" :key="index">
        <label class="dropdown-item">
          <input type="checkbox" :value="item" v-model="selectedValue" />
          {{ nom_dir[index] }}
        </label>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.dropdown-wrapper {
  position: relative; /* clé pour positionner la liste déroulante en absolu */
  display: inline-block; /* optionnel pour s'adapter à la taille du bouton */
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
  position: absolute; /* positionnement absolu par rapport à .dropdown-wrapper */
  z-index: 10;
  top: 100%; /* juste en dessous du bouton */
  right: 0; /* aligné au même point horizontal que le bouton */
  width: 100%;
  list-style: none;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 20px;
  padding-right: 0;
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
