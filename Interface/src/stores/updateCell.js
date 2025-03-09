import { defineStore, storeToRefs } from "pinia";

import { callApi } from "./callApi";
import { updateColorCell } from "./updateColorGrid";
import { errorMessages } from "./errorMessages";

export const updateCell = defineStore("updateCell", () => {
  // On importe les stores
  const apiStore = callApi();
  const colorStore = updateColorCell();
  const errorStore = errorMessages();

  // Update cell
  function majCell(index) {
    // On teste pour savoir si il y a une erreur dans les données
    errorStore.test()
    console.log(errorStore.errorisToogle);
    if (!errorStore.errorisToogle) {
      colorStore.change_color(index);
      apiStore.callApi(index);
    } else {
      errorStore.updateError();
    }
  }

  return { majCell };

});
