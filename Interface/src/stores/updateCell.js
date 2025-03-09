import { defineStore } from "pinia";

import { callApi } from "./callApi";
import { updateColorCell } from "./updateColorGrid";
import { errorMessages } from "./errorMessages";
import { updateNameSens } from "./updateNameSens";

export const updateCell = defineStore("updateCell", () => {
  // On importe les stores
  const apiStore = callApi();
  const colorStore = updateColorCell();
  const errorStore = errorMessages();
  const nameStore = updateNameSens();

  // Update cell
  function majCell(index) {
    // On teste pour savoir si il y a une erreur dans les données
    errorStore.test()
    if (!errorStore.errorisToogle) {
      nameStore.change_name_sens(index);
      colorStore.change_color(index);
      apiStore.callApi(index);
    } else {
      errorStore.updateError();
    }
  }

  return { majCell };

});
