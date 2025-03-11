import { ref } from "vue";
import { defineStore } from "pinia";

export const grid = defineStore("grid", () => {
  // Nbr col et ligne
  const cols = ref(101);
  const rows = ref(101);

  // Taille de la grille
  const width_grid = ref(0);
  const height_grid = ref(0);

  // Taille de la grille
  const updateTaille = (width, height) => {
    width_grid.value = width;
    height_grid.value = height;
  };

  // Info des cellules
  const infoCell = ref(
    Array.from({ length: rows.value * cols.value }, () => ({
      color: "#222831",
      nom: "",
      sens: "",
    }))
  );

  // clear le tableau
  async function clear() {
    // Le path
    const path = "/api/clearData";

    try {
      const response = await fetch(path, {
        method: "post",
      });

      // Réponse
      const result = await response.json();
      
      // On clear le tableau de la page
      infoCell.value = Array.from({ length: rows.value * cols.value }, () => ({
        color: "#222831",
        nom: "",
        sens: "",
      }));

    } catch (error) {
      console.error("Erreur:", error);
    }
  }
  
  return { cols, rows, width_grid, height_grid, updateTaille, infoCell, clear };
},
{
  persist: true,
}
);
