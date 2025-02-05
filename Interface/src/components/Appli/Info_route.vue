<script>
import { ref } from "vue";
import IconFleche from "../Icons/Fleche_bas.vue";

export default {
  components: {
    IconFleche,
  },

  setup() {
    const isOpenDrop1 = ref(false);
    const items = ["G", "B", "D", "H"];
    const selectedDrop_1 = ref([]);

    const toggleDropdown = () => {
      isOpenDrop1.value = !isOpenDrop1.value;
    };

    return {
      isOpenDrop1,
      items,
      selectedDrop_1,
      toggleDropdown,
    };
  },
};
</script>

<template>
  <div class="container">
    <div class="title">
      <p>Paramètres Route</p>
    </div>
    <div class="parametre-container">
      <div class="parametre">
        <!-- Sens de la route -->
        <p class="nom-parametre">Sens route</p>
        <button @click="toggleDropdown" class="dropdown">
          {{ selectedDrop_1.join(", ") || "None" }}
          <IconFleche />
        </button>
        

        <!-- Si on ouvre la dropbox -->
        <ul v-if="isOpenDrop1" class="dropdown-menu">
          <li v-for="(item, index) in items" :key="index">
            <label class="dropdown-item">
              <input type="checkbox" :value="item" v-model="selectedDrop_1" />
              {{ item }}
            </label>
          </li>
        </ul>
      </div>
    </div>


  </div>

</template>

<style>
.container {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  background-color: transparent;
  padding: 10px;
  gap: 20px;
}

.title {
  border: none;
  padding-bottom: 6px;
  padding-left: 6px;
  border-bottom: var(--color-underline) solid 1px;
  font-size: 14px;
  font-weight: 700;
}

.parametre-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.parametre {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 10px;
  border: none;
  overflow: hidden;
  padding-left: 6px;
  padding-right: 6px;
}

.nom-parametre {
  border: none;
  flex: auto;
  font-size: 12px;
  font-weight: 400;
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
  padding-left: 10px;
  padding-right: 10px;
  list-style: none;
  border-radius: 5px;
  background: var(--color-left-bar-2);
}

.dropdown-item {
  display: flex;
  align-items: center;
  padding: 10px;
  cursor: pointer;
}

input[type="checkbox"] {
  margin-right: 10px;
}

.selection-result {
  margin-top: 10px;
  font-style: italic;
}
</style>
