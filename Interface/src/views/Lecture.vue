<script>
import { defineComponent } from "vue";
import Topbar from "@/components/Appli/Topbar.vue";
import Quadrillage from "@/components/Appli/Quadrillage.vue";
import Ruler_left from "@/components/Appli/Ruler_left.vue";
import Ruler_top from "@/components/Appli/Ruler_top.vue";

export default defineComponent({
  components: {
    Topbar,
    Quadrillage,
    Ruler_left,
    Ruler_top,
  },
});
</script>

<template>
  <div class="main_container">
    <div class="grid">
      <div class="left-ruler"><Ruler_left /></div>
      <div class="quadrillage-container" ref="container"><Quadrillage /></div>
      <div class="top-ruler"><Ruler_top /></div>
      <div class="carre"></div>
    </div>
  </div>
  <div class="topbar-container"><Topbar /></div>
</template>

<style scoped>
.topbar-container {
  position: fixed;
  top: 0;
}

.main_container {
  position: fixed;
  display: flex;
  flex-direction: row;
  top: 5vh;
  width: 100vw;
  height: 95vh;
}

.grid {
  flex: 1;
  display: flex;
  flex-direction: row;
  min-width: 0;
}

.left-ruler {
  display: flex;
  flex-direction: row;
  background-color: var(--color-left-bar-1);
  border: 2px solid var(--color-line);
  width: 20px;
  overflow: hidden;
  height: 100%;
}

.top-ruler {
  position: absolute;
  flex-direction: row;
  background-color: var(--color-left-bar-1);
  border: 2px solid var(--color-line);
  height: 20px;
  top: 0;
  overflow: hidden;
  width: 100%;
}

.carre {
  position: absolute;
  background-color: var(--color-left-bar-1);
  border: 2px solid var(--color-line);
  height: 20px;
  width: 20px;
  top: 0;
}

.quadrillage-container {
  flex: 1;
  overflow: hidden;
  cursor: crosshair;
}
</style>
