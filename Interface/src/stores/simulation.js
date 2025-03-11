import { ref } from "vue";
import { defineStore } from "pinia";

export const simulation = defineStore(
  "simulation",
  () => {
    // Constante
    const isSimu = ref(false);
    const isLoading = ref(false)

    // On appelle l'api pour savoir si on a simulé ou pas
    async function isSimulated() {
      // Le path
      const path = "/api/isSimu";

      try {
        const response = await fetch(path, {
          method: "GET",
        });

        // Réponse
        const result = await response.json();
        isSimu.value = result;
        isLoading.value = false;

      } catch (error) {
        console.error("Erreur:", error);
        isLoading.value = false;
      }
    }

    async function launchSimulation() {
      // Le path
      const path = "/api/simulation/launch";

      isLoading.value = true;

      try {
        const response = await fetch(path, {
          method: "POST",
        });
      isSimu.value = true
      } catch (error) {
        console.error("Erreur:", error);
      }
    }

    return {
      isSimulated,
      launchSimulation,
      isSimu,
      isLoading
    };
  },
  {
    persist: false,
  }
);
