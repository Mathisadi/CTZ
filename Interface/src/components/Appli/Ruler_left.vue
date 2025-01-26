<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
    name: "Ruler",
});
</script>

<template>
    <div class="ruler-left">


    </div>
</template>

<style scoped>  
.ruler-top {
    position: fixed;
    display: flex;
    flex-direction: row;
    align-items: center;
    background-color: var(--color-top-bar);
    width: 100vw;
    height: 5vh;
}

.ruler-left {
    position: fixed;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: var(--color-left-bar-1);
    left: 0;
    top: 5vh;
    height: 95vh;
    width: 18vw;
}


</style>

