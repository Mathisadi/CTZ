<script>
import { ref, onMounted, onUnmounted } from "vue";
import Topbar from "@/components/Appli/Topbar.vue";
import Toolbar from "@/components/Appli/Toolbar.vue";
import Quadrillage from "@/components/Appli/Quadrillage.vue";
import Ruler_left from "@/components/Appli/Ruler_left.vue";
import Ruler_top from "@/components/Appli/Ruler_top.vue";
import Info_route from "@/components/Appli/Info_route.vue";
import { grid } from "@/stores/grid.js";

export default {
  components: {
    Topbar,
    Toolbar,
    Quadrillage,
    Ruler_left,
    Ruler_top,
    Info_route,
  },

  setup() {
    const container = ref(null);
    const gridStore = grid();

    const updateContainerSize = () => {
      if (container.value) {
        const rect = container.value.getBoundingClientRect();
        const width_grid = Math.round(rect.width);
        const height_grid = Math.round(rect.height);
        gridStore.updateTaille(width_grid, height_grid);
      }
    };

    onMounted(() => {
      updateContainerSize();
      window.addEventListener("resize", updateContainerSize);
    });

    onUnmounted(() => {
      window.removeEventListener("resize", updateContainerSize);
    });

    return {
      container
    };
  },
};
</script>

<template>
  <div class="main_container">
    <div class="toolbar-container"><Toolbar /></div>
    <div class="info">
      <Info_route />
    </div>
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
  width: 100vw;
  height: 5vh;
}

.main_container {
  position: fixed;
  display: flex;
  flex-direction: row;
  top: 5vh;
  width: 100vw;
  height: 95vh;
}

.toolbar-container {
  display: flex;
  flex-direction: column;
  background-color: var(--color-left-bar-1);
  height: 100%;
  width: 5%;
  max-width: 100px;
  min-width: 80px;
}

.info {
  background-color: var(--color-left-bar-2);
  min-width: 20vw;
  height: 100%;
  display: flex;
  flex-direction: column;
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
