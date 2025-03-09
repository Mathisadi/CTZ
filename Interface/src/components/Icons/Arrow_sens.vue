<script>
import Arrow_left from "./Arrow_left.vue";
import Arrow_right from "./Arrow_right.vue";
import Arrow_down from "./Arrow_down.vue";
import Arrow_up from "./Arrow_up.vue";
import Arrow_range_horiz from "./Arrow_range_horiz.vue";
import Arrow_range_vert from "./Arrow_range_vert.vue";

import { computed } from "vue";

export default {
  props: ["sens"],
  components: {
    Arrow_left,
    Arrow_right,
    Arrow_down,
    Arrow_up,
    Arrow_range_horiz,
    Arrow_range_vert,
  },
  setup(props) {
    const icon = computed(() => {
      if (props.sens === 0) {
        return "left";
      } else if (props.sens === 2) {
        return "right";
      } else if (props.sens === 1) {
        return "down";
      } else if (props.sens === 3) {
        return "up";
      } else if (JSON.stringify(props.sens) === JSON.stringify([0, 2])) {
        return "horiz";
      } else if (JSON.stringify(props.sens) === JSON.stringify([1, 3])) {
        return "vert";
      } else {
        return "";
      }
    });

    return { icon };
  },
};
</script>

<template>
  <Arrow_left v-if="icon === 'left'" />
  <Arrow_right v-else-if="icon === 'right'" />
  <Arrow_down v-else-if="icon === 'down'" />
  <Arrow_up v-else-if="icon === 'up'" />
  <Arrow_range_horiz v-else-if="icon === 'horiz'" />
  <Arrow_range_vert v-else-if="icon === 'vert'" />
</template>
