import { ref } from "vue";
import { defineStore } from "pinia";
import { routeSettigns } from "./routeSettings";
import { intersectionSettings } from "./intersectionSettings";
import { feuSettings } from "./feuSettings";
import { prioriteSettings } from "./prioriteSettings";
import { pietonSettings } from "./pietonSettings";
import { departSettings } from "./departSettings";
import { finSettings } from "./finSettings";
import { toolbarInteraction } from "./toolbarInteraction";

export const errorMessages = defineStore("errorMessages", () => {
  // Stores
  const storeRoute = routeSettigns();
  const storeIntersection = intersectionSettings();
  const storeFeu = feuSettings();
  const storePriorite = prioriteSettings();
  const storePieton = pietonSettings();
  const storeDepart = departSettings();
  const storeFin = finSettings();
  const storeToolbar = toolbarInteraction();

  // Error message
  const ErrorMessage = ref("");
  const errorisToogle = ref(false);

  // Test
  const test = () => {
    if (storeToolbar.isRouteToogle) {
      errorisToogle.value = !storeRoute.testFilled();
    } else if (storeToolbar.isIntersectionToogle) {
      errorisToogle.value = !storeIntersection.testFilled();
    } else if (storeToolbar.isFeuToogle) {
      errorisToogle.value = !storeFeu.testFilled();
    } else if (storeToolbar.isPrioriteToogle) {
      errorisToogle.value = !storePriorite.testFilled();
    } else if (storeToolbar.isPietonToogle) {
      errorisToogle.value = !storePieton.testFilled();
    } else if (storeToolbar.isDepartToogle) {
      errorisToogle.value = !storeDepart.testFilled();
    } else if (storeToolbar.isFinToogle) {
      errorisToogle.value = !storeFin.testFilled();
    }
  };

  const error = () => {
    if (storeToolbar.isRouteToogle && errorisToogle.value) {
      ErrorMessage.value =
        "Des données sont manquantes ou mal renseignées. Pour rappel la somme des probabilités doit-être égale à 1";
    } else if (storeToolbar.isIntersectionToogle && errorisToogle.value) {
      ErrorMessage.value = "Des données sont manquantes ou mal renseignées.";
    } else if (storeToolbar.isFeuToogle && errorisToogle.value) {
      ErrorMessage.value =
        "Des données sont manquantes ou mal renseignées. Pour rappel la somme des probabilités doit-être égale à 1";
    } else if (storeToolbar.isPrioriteToogle && errorisToogle.value) {
      ErrorMessage.value =
        "Des données sont manquantes ou mal renseignées. Pour rappel la somme des probabilités doit-être égale à 1";
    } else if (storeToolbar.isPietonToogle && errorisToogle.value) {
      ErrorMessage.value =
        "Des données sont manquantes ou mal renseignées. Pour rappel la somme des probabilités doit-être égale à 1";
    } else if (storeToolbar.isDepartToogle && errorisToogle.value) {
      ErrorMessage.value = "Des données sont manquantes ou mal renseignées.";
    } else if (storeToolbar.isFinToogle && errorisToogle.value) {
      ErrorMessage.value = "Des données sont manquantes ou mal renseignées.";
    }
  };

  const updateError = () => {
    error();
    setTimeout(() => {
      errorisToogle.value = false;
      ErrorMessage.value = "";
    }, 3000);
  };

  return { ErrorMessage, errorisToogle, updateError, test };
});
