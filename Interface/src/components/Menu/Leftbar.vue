<script lang="ts">
import { defineComponent } from 'vue';
import Add_circle from '../Icons/Add_circle.vue';
import Open_folder from '../Icons/Open_folder.vue';

export default defineComponent({
    name: "Leftbar",
    
    components: {
        Add_circle,
        Open_folder
    },

    return(){
        Add_circle;
        Open_folder
    }
})

</script>

<template>
    <div class="leftbar">
        <button class="new"><Add_circle />Nouveau</button>
        <button class="open"><Open_folder />Ouvrir</button>
        <div class="line"></div>
    </div>
</template>

<style>
.leftbar {
    position: absolute;
    display: flex;
    background-color: var(--color-left-bar-1);
    left: 0;
    top: 5vh;
    height: 95vh;
    width: 18vw;
}

.new {
    position: absolute;
    top: 20px;
    left: 20px;
    display: flex;
    align-items: center;
    background-color: var(--color-left-bar-2);
    height: 5%;
    width: 38%;
    border: none;
    font-size: 12px;
    font-weight: medium;
    color: var(--color-texte);
    padding: 8px;
    gap: 6px;
    border-radius: 4px;
    cursor: pointer;
}

.open {
    position: absolute;
    top: 20px;
    right: 20px;
    display: flex;
    align-items: center;
    background-color: var(--color-left-bar-2);
    height: 5%;
    width: 38%;
    border: none;
    font-size: 12px;
    font-weight: medium;
    color: var(--color-texte);
    padding: 8px;
    gap: 12px;
    border-radius: 4px;
    cursor: pointer;
}

.line {
    position: absolute;
    top: 80px;
    left: 5%;
    width: 90%;
    height: 1px;
    background-color: var(--color-underline);
}
</style>