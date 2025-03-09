import { defineStore } from "pinia";
import { ref } from "vue";

import { toolbarInteraction } from "./toolbarInteraction";
import { routeSettigns } from "./routeSettings";
import { intersectionSettings } from "./intersectionSettings";
import { feuSettings } from "./feuSettings";
import { prioriteSettings } from "./prioriteSettings";
import { pietonSettings } from "./pietonSettings";
import { departSettings } from "./departSettings";
import { finSettings } from "./finSettings";

export const callApi = defineStore("callApi", () => {
  // On importe les stores
  const typeStore = toolbarInteraction();
  const routeStore = routeSettigns();
  const intersectionStore = intersectionSettings();
  const feuStore = feuSettings();
  const prioriteStore = prioriteSettings();
  const pietonStore = pietonSettings();
  const departStore = departSettings();
  const finStore = finSettings();

  // Upadate data
  function cellInfo() {
    if (typeStore.isRouteToogle) {
      return routeStore.getRouteSettings();
    } else if (typeStore.isIntersectionToogle) {
      return intersectionStore.getIntersectionSettings();
    } else if (typeStore.isFeuToogle) {
      return feuStore.getFeuSettings();
    } else if (typeStore.isPrioriteToogle) {
      return prioriteStore.getPrioriteSettings();
    } else if (typeStore.isPietonToogle) {
      return pietonStore.getPietonSettings();
    } else if (typeStore.isDepartToogle) {
      return departStore.getDepartSettings();
    } else if (typeStore.isFinToogle) {
      return finStore.getFinSettings();
    }
  }

  function apiRoutes(index) {
    // Chemin de base
    const path = "/api/build/" + String(index);

    if (typeStore.isRouteToogle) {
      return path + "/route";
    } else if (typeStore.isIntersectionToogle) {
      return path + "/intersection";
    } else if (typeStore.isFeuToogle) {
      return path + "/feu";
    } else if (typeStore.isPrioriteToogle) {
      return path + "/priorite";
    } else if (typeStore.isPietonToogle) {
      return path + "/pieton";
    } else if (typeStore.isDepartToogle) {
      if (departStore.type_depart === "Voiture") {
        return path + "/depart";
      } else {
        return path + "/departPieton";
      }
    } else if (typeStore.isFinToogle) {
      return path + "/fin";
    }
  }

  async function callApi(index) {
    // Le path
    const path = apiRoutes(index);
    // La data
    const data = cellInfo();

    const responseData = ref(null);
    try {
      const response = await fetch(path, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      const result = await response.json();
      responseData.value = result;
    } catch (error) {
      console.error("Erreur:", error);
    }
  }

  return { callApi };
});
