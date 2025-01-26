<script>
import Topbar from '@/components/Appli/Topbar.vue';
import Toolbar from '@/components/Appli/Toolbar.vue';
import Quadrillage from '@/components/Appli/Quadrillage.vue';
import Ruler_left from '@/components/Appli/Ruler_left.vue';


export default{
    components: {
        Topbar,
        Toolbar,
        Quadrillage,
        Ruler_left
    },
}
</script>

<template>
    <div class="topbar-container"><Topbar /></div>
    <div class="main_cotainer">
        <div class="toolbar-container"><Toolbar /></div>
        <div class="quadrillage-container"><Quadrillage /></div>
    </div>
</template>

<style scoped>
.topbar-container {
    position: fixed;
    top: 0;
    width: 100vw;
    height: 5vh;
}

.main_cotainer {
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
    height: 95vh;
    width: 5vw;
    max-width: 100px;
    min-width: 80px;
}

.left-ruler {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: var(--color-left-bar-1);
    border: 2px solid var(--color-line);
    width: 20px;
}

.quadrillage-container {
    flex: 1;
    overflow: hidden;
    cursor: crosshair;
}

</style>