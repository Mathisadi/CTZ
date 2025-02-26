<script>
import { routeSettigns } from "@/stores/routeSettings";
import { computed } from "vue";

export default {
  props: ["type", "param"],
  setup(props) {
    // Store route setting
    const storeRoute = routeSettigns();

    // Fonction qui renvoie le bon élément en fonction des props
    const selectedValue = computed({
      get() {
        if (props.type === "route") {
          if (props.param === "len") {
            return storeRoute.longeur;
          }
        }
        return 0;
      },
      set(newValue) {
        if (props.type === "route") {
          if (props.param === "len") {
            storeRoute.longeur = newValue;
          }
        }
      },
    });

    return {
      selectedValue,
    };
  },
};
</script>

<template>
  <input
    class="input-container"
    v-model="selectedValue"
    type="text"
    placeholder="None"
  />
</template>

<style scoped>
.input-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 120px;
  padding-left: 10px;
  padding-right: 10px;
  padding-bottom: 4px;
  background-color: transparent;
  color: var(--color-text);
  font-size: 12px;
  font-weight: 400;
  border: none;
  border-bottom: var(--color-underline) solid 1px;
  cursor: pointer;
}


.input-container::placeholder {
  color: var(--color-text);
  font-size: 12px;
  font-weight: 400;
}

.input-container:focus {
  outline: none;
}

</style>
