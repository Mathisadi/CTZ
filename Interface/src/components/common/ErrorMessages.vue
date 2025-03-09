<script>
import { errorMessages } from "@/stores/ErrorMessages";

export default {
  setup() {
    // Stores
    const storeError = errorMessages();

    return {
      storeError,
    };
  },
};
</script>

<template>
  <div v-if="storeError.errorisToogle" class="error">
    {{ storeError.ErrorMessage }}
  </div>
</template>

<style scoped>
.error {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  text-align: center;
  width: 250px; /* Ne dépassera jamais la largeur du parent */
  white-space: normal; /* Permet le retour à la ligne */
  overflow-wrap: break-word; /* Coupe les mots trop longs */
  box-sizing: border-box; /* Inclut les padding/border dans la largeur */
  color: rgb(212, 53, 53);
  font-size: 12px;
  font-weight: 400;
  border: none;
}
</style>
