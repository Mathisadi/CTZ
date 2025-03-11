import { defineStore } from "pinia";
import { toRef } from "vue"

import { callApi } from "./callApi";
import { errorMessages } from "./errorMessages";
import { grid } from "./gridProps";
import { routeSettigns } from "./routeSettings";
import { intersectionSettings } from "./intersectionSettings";
import { feuSettings } from "./feuSettings";
import { prioriteSettings } from "./prioriteSettings";
import { pietonSettings } from "./pietonSettings";
import { departSettings } from "./departSettings";
import { finSettings } from "./finSettings";
import { toolbarInteraction } from "./toolbarInteraction";

export const updateCell = defineStore("updateCell", () => {
  // On importe les stores
  const apiStore = callApi();
  const errorStore = errorMessages();

  // On importe les stores
  const storeGrid = grid();
  const storeRoute = routeSettigns();
  const storeIntersection = intersectionSettings();
  const storeFeu = feuSettings();
  const storePriorite = prioriteSettings();
  const storePieton = pietonSettings();
  const storeDepart = departSettings();
  const storeFin = finSettings();
  const toolbarStore = toolbarInteraction();

  // Constante de la grille
  const cells = toRef(storeGrid, "infoCell");

  const change_name_sens = (index) => {
    if (toolbarStore.isRouteToogle) {
      cells.value[index].nom = storeRoute.nom;
      cells.value[index].sens = storeRoute.sens_route;
    } else if (toolbarStore.isIntersectionToogle) {
      cells.value[index].nom = storeIntersection.nom;
      cells.value[index].sens = storeIntersection.sens_route;
    } else if (toolbarStore.isFeuToogle) {
      cells.value[index].nom = storeFeu.nom;
      cells.value[index].sens = storeFeu.sens_route;
    } else if (toolbarStore.isPrioriteToogle) {
      cells.value[index].nom = storePriorite.nom;
      cells.value[index].sens = storePriorite.sens_route;
    } else if (toolbarStore.isDepartToogle) {
      cells.value[index].nom = storeDepart.nom;
      cells.value[index].sens = storeDepart.sens_route;
    } else if (toolbarStore.isFinToogle) {
      cells.value[index].nom = storeFin.nom;
      cells.value[index].sens = storeFin.sens_route;
    } else if (toolbarStore.isPietonToogle) {
      cells.value[index].nom = storePieton.nom;
      cells.value[index].sens = storePieton.sens_route;
    }
  };

  // Constante couleur
  const color_route = "#76ABAE";
  const color_intersection = "#AE7676";
  const color_priorite = "#AEA176";
  const color_feu = "#A176AE";
  const color_depart = "#76ABAE";
  const color_fin = "#AE7676";
  const color_pieton = "#AE7676";

  const change_color = (index) => {
    if (toolbarStore.isRouteToogle) {
      cells.value[index].color = color_route;
    }

    if (toolbarStore.isIntersectionToogle) {
      cells.value[index].color = color_intersection;
    }

    if (toolbarStore.isFeuToogle) {
      cells.value[index].color = color_feu;
    }

    if (toolbarStore.isPrioriteToogle) {
      cells.value[index].color = color_priorite;
    }

    if (toolbarStore.isDepartToogle) {
      cells.value[index].color = color_depart;
    }

    if (toolbarStore.isFinToogle) {
      cells.value[index].color = color_fin;
    }

    if (toolbarStore.isPietonToogle) {
      cells.value[index].color = color_pieton;
    }
  };

  // Clear info
  const clear_info = () => {
    if (toolbarStore.isRouteToogle) {
      storeRoute.clear();
    } else if (toolbarStore.isIntersectionToogle) {
      storeIntersection.clear();
    } else if (toolbarStore.isFeuToogle) {
      storeFeu.clear();
    } else if (toolbarStore.isPrioriteToogle) {
      storePriorite.clear();
    } else if (toolbarStore.isDepartToogle) {
      storeDepart.clear();
    } else if (toolbarStore.isFinToogle) {
      storeFin.clear();
    } else if (toolbarStore.isPietonToogle) {
      storePieton.clear();
    }
  };
  // Update cell
  function majCell(index) {
    // On teste pour savoir si il y a une erreur dans les données
    errorStore.test();
    if (!errorStore.errorisToogle) {
      change_name_sens(index);
      change_color(index);
      apiStore.callApi(index);
      clear_info();
    } else {
      errorStore.updateError();
    }
  }

  return { majCell };
});
