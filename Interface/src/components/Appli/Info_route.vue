<script>
import { ref } from "vue";

export default {
    setup() {
        const isOpenDrop1 = ref(false)
        const items = ["Gauche", "Bas", "Droite", "Haut"]
        const selectedDrop_1 = ref([])

        const toggleDropdown = () => {
            isOpenDrop1.value = !isOpenDrop1.value;
        }
        
        return {
            isOpenDrop1, 
            items,
            selectedDrop_1,
            toggleDropdown
        };
    }
}
</script>

<template>
    <div>
      <button @click="toggleDropdown" class="dropdown-button">
        {{ selectedDrop_1.join(", ") || "Sélectionnez un élément" }}
      </button>
      <ul v-if="isOpenDrop1" class="dropdown-menu">
        <li v-for="(item, index) in items" :key="index">
          <label class="dropdown-item">
            <input
              type="checkbox"
              :value="item"
              v-model="selectedDrop_1"
            />
            {{ item }}
          </label>
        </li>
      </ul>
    </div>
</template>
    
<style>
  .dropdown-button {
    padding: 10px 20px;
    background-color: var(--color-left-bar-2);
    color: white;
    border: none;
    border-radius: 2px;
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
  
  .dropdown-item:hover {
    background-color: #f0f0f0;
  }
  
  input[type="checkbox"] {
    margin-right: 10px;
  }
  
  .selection-result {
    margin-top: 10px;
    font-style: italic;
  }
  </style>
  