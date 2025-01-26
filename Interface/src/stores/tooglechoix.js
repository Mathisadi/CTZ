import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useToogleChoixStore = defineStore('tooglechoix', () => {
  const choixVisible = ref(false);
  function toggle() {
    choixVisible.value = !choixVisible.value;
  }

  return { choixVisible, toggle };
});