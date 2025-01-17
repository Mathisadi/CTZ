<script lang="ts">
import { defineComponent } from 'vue';
import Edit from '../Icons/Edit.vue';

export default defineComponent({
    name: "Choix_mode",
    components: {
        Edit
    }
})
</script>

<template>
    <div class="choix_mode">
        <RouterLink to ="/appli/edition" class="edition"><Edit />Edition</RouterLink>
        <RouterLink to ="/appli/lecture" class="lecture">Lecture</RouterLink>
        <RouterLink to ="/appli/simulation" class="simulation">Simulation</RouterLink>
    </div>
</template>

<style>
.choix_mode {
    position: absolute;
    background-color: var(--color-left-bar-1);
    right: 20px;
    top:5vh;
    height: 14vh;
    width: 8vw;
    border-radius: 8px;
}

.edition {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 33%;
    color: var(--color-text);
    text-decoration: none;
    gap: 10px;
}

.lecture {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 33%;
    color: var(--color-text);
    text-decoration: none;
}

.simulation {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 33%;
    color: var(--color-text);
    text-decoration: none;
}
</style>