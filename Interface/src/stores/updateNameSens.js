import { defineStore } from "pinia";
import { grid } from "./gridProps";
import { routeSettigns } from "./routeSettings";
import { intersectionSettings } from "./intersectionSettings";
import { feuSettings } from "./feuSettings";
import { prioriteSettings } from "./prioriteSettings";
import { pietonSettings } from "./pietonSettings";
import { departSettings } from "./departSettings";
import { finSettings } from "./finSettings";
import { toolbarInteraction } from "./toolbarInteraction";


export const updateNameSens = defineStore("updateNameSens", () => {
  // On importe les stores
  const storeGrid = grid();
  const storeRoute = routeSettigns();
  const storeIntersection = intersectionSettings();
  const storeFeu = feuSettings();
  const storePriorite = prioriteSettings();
  const storePieton = pietonSettings();
  const storeDepart = departSettings();
  const storeFin = finSettings();

  // Constante de la grille
  const cells = storeGrid.infoCell;

  // Etats des boutons
  const toolbarStore = toolbarInteraction();

  const change_name_sens = (index) => {
    if (toolbarStore.isRouteToogle) {
      cells[index].nom = storeRoute.nom;
      cells[index].sens = storeRoute.sens_route;
      console.log(storeRoute.nom);
    } else if (toolbarStore.isIntersectionToogle) {
      cells[index].nom = storeIntersection.nom;
      cells[index].sens = storeIntersection.sens_route;
    } else if (toolbarStore.isFeuToogle) {
      cells[index].nom = storeFeu.nom;
      cells[index].sens = storeFeu.sens_route;
    } else if (toolbarStore.isPrioriteToogle) {
      cells[index].nom = storePriorite.nom;
      cells[index].sens = storePriorite.sens_route;
    } else if (toolbarStore.isDepartToogle) {
      cells[index].nom = storeDepart.nom;
      cells[index].sens = storeDepart.sens_route;
    } else if (toolbarStore.isFinToogle) {
      cells[index].nom = storeFin.nom;
      cells[index].sens = storeFin.sens_route;
    } else if (toolbarStore.isPietonToogle) {
      cells[index].nom = storePieton.nom;
      cells[index].sens = storePieton.sens_route;
    }
  };

  return {
    change_name_sens,
  };
});
