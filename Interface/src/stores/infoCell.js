import { defineStore } from "pinia";
import { grid } from "./gridProps";

export const infoCell = defineStore("infoCell", () => {
  // Constante de la grille
  const storeGrid = grid();
  const cols = storeGrid.cols;
  const rows = storeGrid.rows;

  // Info des cellules
  const data = ref(
    Array.from({ length: rows * cols }, () => ({
      color: "#222831",
      nom: "",
      dir: "",
    }))
  );

  return { updateCell };
});
