import { defineStore } from "pinia";
import { grid } from "./gridProps";
import { toolbarInteraction } from "./toolbarInteraction";

export const updateColorCell = defineStore("updateColorCell", () => {
  // On importe les stores
  const storeGrid = grid();

  // Constante de la grille
  const cells = storeGrid.infoCell;

  // Constante couleur
  const color_route = "#76ABAE";
  const color_intersection = "#AE7676";
  const color_priorite = "#AEA176";
  const color_feu = "#A176AE";
  const color_depart = "#76ABAE";
  const color_fin = "#AE7676";
  const color_pieton = "#AE7676";

  // Etats des boutons
  const toolbarStore = toolbarInteraction();

  const change_color = (index) => {
    if (toolbarStore.isRouteToogle) {
      cells[index].color = color_route;
    }

    if (toolbarStore.isIntersectionToogle) {
      cells[index].color = color_intersection;
    }

    if (toolbarStore.isFeuToogle) {
      cells[index].color = color_feu;
    }

    if (toolbarStore.isPrioriteToogle) {
      cells[index].color = color_priorite;
    }

    if (toolbarStore.isDepartToogle) {
      cells[index].color = color_depart;
    }

    if (toolbarStore.isFinToogle) {
      cells[index].color = color_fin;
    }

    if (toolbarStore.isPietonToogle) {
      cells[index].color = color_pieton;
    }
  };

  return {
    change_color,
  };
});
