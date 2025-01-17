<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useRoute } from 'vue-router';
import More from '../Icons/More.vue';
import Choix_mode from './Choix_mode.vue';

export default defineComponent({
    name: "Topbar",
    components: {
        More,
        Choix_mode
    },
    setup(){
        const buttonName = useRoute().name
        const choixisVisible = ref(true)

        const tooglechoix = () => {
            choixisVisible.value = !choixisVisible.value
        }

        return {
            buttonName,
            choixisVisible,
            tooglechoix
        }
    },
})
</script>

<template>
    <div class="topbar">
        <h1>CTZ</h1>
        <h2>| ... Project path</h2>
        <button class="mode" @click="tooglechoix">{{buttonName}}<More /></button>
    </div>

    <Choix_mode v-if="choixisVisible" />
</template>

<style>
.topbar {
    position: absolute;
    display: flex;
    align-items: center;
    background-color: var(--color-top-bar);
    width: 100vw;
    height: 5vh;
}

div h1 {
    position: absolute;
    left: 20px;
    font-size: 16px;
    font-weight: bold;
    color: var(--color-title);
}

div h2 {
    position: absolute;
    left: 60px;
    font-size: 14px;
    font-weight: normal;
    color: var(--color-white);
}

.mode {
    position: absolute;
    display: flex;
    align-items: center;
    right: 10px;
    height: 100%;
    font-size: 14px;
    gap: 5px;
    padding: 0 0px;
    color: var(--color-white);
    background-color: transparent;
    border: none;
    cursor: pointer;
}
</style>