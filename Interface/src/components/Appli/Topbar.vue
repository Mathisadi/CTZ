<script>
import { defineComponent } from "vue";
import { useRoute } from "vue-router";
import More from "../Icons/More.vue";
import Choix_mode from "./Choix_mode.vue";
import { useToogleChoixStore } from "@/stores/tooglechoix";

export default defineComponent({
  components: {
    More,
    Choix_mode,
  },
  setup() {
    const buttonName = useRoute().name;
    const store = useToogleChoixStore();

    return { 
      buttonName,
      store
    };
  }
});
</script>

<template>
  <div class="topbar">
    <h1>CTZ</h1>
    <h2>| ... Project path</h2>
    <button class="mode" @click="store.toggle">{{ buttonName }}<More /></button>
  </div>

  <Choix_mode v-if="store.choixVisible" />
</template>

<style scoped>
.topbar {
  display: flex;
  flex-direction: row;
  align-items: center;
  background-color: var(--color-top-bar);
  width: 100vw;
  height: 5vh;
}

div h1 {
  display: flex;
  align-items: center;
  justify-content: center;
  top: 0;
  left: 0;
  width: 5%;
  height: 100%;
  font-size: 16px;
  font-weight: bold;
  color: var(--color-title);
}

div h2 {
  left: 5%;
  font-size: 14px;
  font-weight: normal;
  color: var(--color-white);
}

.mode {
  position: absolute;
  display: flex;
  align-items: center;
  right: 10px;
  gap: 5px;
  padding: 0 0px;
  color: var(--color-white);
  background-color: transparent;
  border: none;
  cursor: pointer;
  font-size: 14px;
  font-weight: normal;
}
</style>
