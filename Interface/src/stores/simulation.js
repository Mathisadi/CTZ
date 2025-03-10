import { ref } from "vue";
import { defineStore } from "pinia";

export const simulation = defineStore(
  "simulation",
  () => {
    const isSimulated = ref(false)

    const startSimulation = () => {
      isSimulated.value = true;
    };

    return {
      isSimulated
    };
  },
  {
    persist: true,
  }
);
