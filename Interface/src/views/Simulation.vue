<script>
import { defineComponent } from "vue";
import Topbar from "@/components/Appli/Topbar.vue";
import Video from "@/components/common/Video.vue";

export default defineComponent({
  components: {
    Topbar,
    Video,
  },
});
</script>

<template>
  <div class="main_container"><Video /></div>
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
</style>
