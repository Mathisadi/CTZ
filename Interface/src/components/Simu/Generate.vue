<script>
import Play from "../Icons/Play.vue";
import { simulation } from "@/stores/simulation";
import { toRef } from "vue";

export default {
  components: {
    Play,
  },
  setup() {
    const store = simulation();
    const isLoading = toRef(store, "isLoading");

    return {
      store,
      isLoading,
    };
  },
};
</script>

<template>
  <div class="button-container">
    <button class="button-generate" @click="store.launchSimulation">
      Lancer la simulation<Play />
    </button>
    <div v-if="isLoading" class="spinner"></div>
  </div>
</template>

<style scoped>
.button-container {
  display: flex;
  gap: 20px;
  flex-direction: column;
  width: 100%;
  height: 100%;
  justify-content: center;
  align-items: center;
}

.button-generate {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 10px;
  height: 40px;
  background-color: var(--color-title);
  color: var(--color-text);
  font-size: 16px;
  font-weight: 400;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 6px solid var(--color-text);
  border-top: 6px solid var(--color-title);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
