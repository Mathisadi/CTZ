import { ref } from 'vue';
import { defineStore } from 'pinia';

export const grid = defineStore('grid', () => {
    // Nbr col et ligne
    const cols = ref(101);
    const rows = ref(101);

    // Taille de la grille
    const width_grid = ref(0)
    const height_grid = ref(0)

    const updateTaille = (width, height) => {
        width_grid.value = width;
        height_grid.value = height;
    };

    return { cols, rows, width_grid, height_grid, updateTaille };
});