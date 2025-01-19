<script lang="ts">
import { defineComponent } from 'vue';
import Edit from '../Icons/Edit.vue';
import Eye from '../Icons/Eye.vue';
import Start from '../Icons/Start.vue';
import { useToogleChoixStore } from '@/stores/tooglechoix.ts';

export default defineComponent({
    name: "Choix_mode",
    components: {
        Edit,
        Eye,
        Start,
    },
    setup() {
        const modeStore = useToogleChoixStore();

        return { 
            modeStore
        };
    }
})
</script>

<template>
    <div class="choix_mode">
        <RouterLink to ="/appli/edition" class="mode" @click="modeStore.toggle"><Edit />Edition</RouterLink>
        <RouterLink to ="/appli/simulation" class="mode" @click="modeStore.toggle"><Start />Simulation</RouterLink>
        <RouterLink to ="/appli/lecture" class="mode" @click="modeStore.toggle"><Eye />Lecture</RouterLink>
    </div>
</template>

<style scoped>
.choix_mode {
    position: absolute;
    display: flex;
    flex-direction: column;
    background-color: var(--color-left-bar-1);
    right: 20px;
    top: 5vh;
    border-radius: 8px;
    padding-right: 12px;
    padding-left: 12px;
    padding-top: 10px;
    padding-bottom: 10px;
    gap: 10px;
}

.mode {
    display: flex;
    align-items: center; /* Aligne les icônes et le texte verticalement */
    color: var(--color-text);
    text-decoration: none;
    font-size: 14px;
    font-weight: normal;
    gap: 16px;
}
</style>