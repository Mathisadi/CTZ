import { ref } from "vue";
import { defineStore } from "pinia";
import { grid } from "./grid";

export const mouvement = defineStore("mouvement", () => {
  // store
  const taille_grid = grid();

  // Constante grid
  const cols = ref(taille_grid.cols);
  const rows = ref(taille_grid.rows);

  // Constante de la grille
  const offset = ref({
    x: -(cols.value * 100) / 2 - 30,
    y: -(rows.value * 100) / 2 - 10,
  });
  const startPosition = ref({ x: 0, y: 0 });
  const isDraging = ref(false);

  // Drag
  function startDrag(event) {
    isDraging.value = true;
    startPosition.value = { x: event.clientX, y: event.clientY };
  }

  // Fonction utilitaire pour limiter une valeur entre min et max
  function clamp(value, min, max) {
    return Math.min(Math.max(value, min), max);
  }

  function onDrag(event) {
    // Store grid
    const storeGrid = grid();
    const width = storeGrid.width_grid;
    const height = storeGrid.height_grid;

    if (isDraging.value) {
      // Calculer le delta
      const dx = event.clientX - startPosition.value.x;
      const dy = event.clientY - startPosition.value.y;

      // Calculer la nouvelle position
      const newX = offset.value.x + dx;
      const newY = offset.value.y + dy;

      // Définir les limites (ici, 0 pour la limite inférieure, et une limite calculée pour la droite/bas)
      const minX = width - cols.value * 100;
      const minY = height - rows.value * 100;

      // Limiter (clamp) les nouvelles coordonnées
      offset.value.x = clamp(newX, minX, 0);
      offset.value.y = clamp(newY, minY, 0);

      // Mettre à jour la position de départ
      startPosition.value = { x: event.clientX, y: event.clientY };
    }
  }

  function endDrag() {
    isDraging.value = false;
  }

  return { offset, startPosition, startDrag, onDrag, endDrag };
});
