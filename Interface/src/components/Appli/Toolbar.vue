<script>
import { defineComponent, ref } from 'vue';
import IconRoute from '../Icons/Route.vue';
import IconIntersection from '../Icons/Intersection.vue';
import IconFeu from '../Icons/Feu.vue';
import IconPriorite from '../Icons/Priorite.vue';
import IconPieton from '../Icons/Pieton.vue';
import IconDepart from '../Icons/Depart.vue';
import IconFin from '../Icons/Fin.vue';
import IconSelection from '../Icons/Selection.vue';
import IconParametre from '../Icons/Parametre.vue';

export default defineComponent({
    name: "Toolbar",
    components: {
        IconRoute,
        IconIntersection,
        IconFeu,
        IconPriorite,
        IconPieton,
        IconDepart,
        IconFin,
        IconSelection,
        IconParametre
    },
    setup() {
        const bgColor_route =  ref('transparent');
        const bgColor_intersection = ref('transparent');
        const bgColor_feu = ref('transparent');
        const bgColor_priorite = ref('transparent');
        const bgColor_pieton = ref('transparent');
        const bgColor_depart = ref('transparent');
        const bgColor_fin = ref('transparent');
        const bgColor_selection = ref('transparent');
        const bgColor_parametres = ref('transparent');

        const changeColor_route = () => {
            bgColor_route.value = 'var(--color-left-bar-2)'; // Change la couleur de fond
            bgColor_intersection.value = 'transparent';
            bgColor_feu.value = 'transparent';
            bgColor_priorite.value = 'transparent';
            bgColor_pieton.value = 'transparent';
            bgColor_depart.value = 'transparent';
            bgColor_fin.value = 'transparent';
            bgColor_selection.value = 'transparent';
            bgColor_parametres.value = 'transparent';
        }
        
        const changeColor_intersection = () => {
            bgColor_route.value = 'transparent';
            bgColor_intersection.value = 'var(--color-left-bar-2)';
            bgColor_feu.value = 'transparent';
            bgColor_priorite.value = 'transparent';
            bgColor_pieton.value = 'transparent';
            bgColor_depart.value = 'transparent';
            bgColor_fin.value = 'transparent';
            bgColor_selection.value = 'transparent';
            bgColor_parametres.value = 'transparent';
        }

        const changeColor_feu = () => {
            bgColor_route.value = 'transparent';
            bgColor_intersection.value = 'transparent';
            bgColor_feu.value = 'var(--color-left-bar-2)';
            bgColor_priorite.value = 'transparent';
            bgColor_pieton.value = 'transparent';
            bgColor_depart.value = 'transparent';
            bgColor_fin.value = 'transparent';
            bgColor_selection.value = 'transparent';
            bgColor_parametres.value = 'transparent';
        }   

        const changeColor_priorite = () => {
            bgColor_route.value = 'transparent';
            bgColor_intersection.value = 'transparent';
            bgColor_feu.value = 'transparent';
            bgColor_priorite.value = 'var(--color-left-bar-2)';
            bgColor_pieton.value = 'transparent';
            bgColor_depart.value = 'transparent';
            bgColor_fin.value = 'transparent';
            bgColor_selection.value = 'transparent';
            bgColor_parametres.value = 'transparent';
        }

        const changeColor_pieton = () => {
            bgColor_route.value = 'transparent';
            bgColor_intersection.value = 'transparent';
            bgColor_feu.value = 'transparent';
            bgColor_priorite.value = 'transparent';
            bgColor_pieton.value = 'var(--color-left-bar-2)';
            bgColor_depart.value = 'transparent';
            bgColor_fin.value = 'transparent';
            bgColor_selection.value = 'transparent';
            bgColor_parametres.value = 'transparent';
        }

        const changeColor_depart = () => {
            bgColor_route.value = 'transparent';
            bgColor_intersection.value = 'transparent';
            bgColor_feu.value = 'transparent';
            bgColor_priorite.value = 'transparent';
            bgColor_pieton.value = 'transparent';
            bgColor_depart.value = 'var(--color-left-bar-2)';
            bgColor_fin.value = 'transparent';
            bgColor_selection.value = 'transparent';
            bgColor_parametres.value = 'transparent';
        }

        const changeColor_fin = () => {
            bgColor_route.value = 'transparent';
            bgColor_intersection.value = 'transparent';
            bgColor_feu.value = 'transparent';
            bgColor_priorite.value = 'transparent';
            bgColor_pieton.value = 'transparent';
            bgColor_depart.value = 'transparent';
            bgColor_fin.value = 'var(--color-left-bar-2)';
            bgColor_selection.value = 'transparent';
            bgColor_parametres.value = 'transparent';
        }

        const changeColor_selection = () => {
            bgColor_route.value = 'transparent';
            bgColor_intersection.value = 'transparent';
            bgColor_feu.value = 'transparent';
            bgColor_priorite.value = 'transparent';
            bgColor_pieton.value = 'transparent';
            bgColor_depart.value = 'transparent';
            bgColor_fin.value = 'transparent';
            bgColor_selection.value = 'var(--color-left-bar-2)';
            bgColor_parametres.value = 'transparent';
        }

        const changeColor_parametres = () => {
            bgColor_route.value = 'transparent';
            bgColor_intersection.value = 'transparent';
            bgColor_feu.value = 'transparent';
            bgColor_priorite.value = 'transparent';
            bgColor_pieton.value = 'transparent';
            bgColor_depart.value = 'transparent';
            bgColor_fin.value = 'transparent';
            bgColor_selection.value = 'transparent';
            bgColor_parametres.value = 'var(--color-left-bar-2)';
        }

        return {
            bgColor_route,
            bgColor_intersection,
            bgColor_feu,
            bgColor_priorite,
            bgColor_pieton,
            bgColor_depart,
            bgColor_fin,
            bgColor_selection,
            bgColor_parametres,
            changeColor_route,
            changeColor_intersection,
            changeColor_feu,
            changeColor_priorite,
            changeColor_pieton,
            changeColor_depart,
            changeColor_fin,
            changeColor_selection,
            changeColor_parametres
        }
    }
})
</script>

<template>
    <div class="toolbar">
        <button class="icon" @click="changeColor_route()" :style="{ backgroundColor: bgColor_route }"><IconRoute />Route</button>
        <button class="icon" @click="changeColor_intersection()" :style="{ backgroundColor: bgColor_intersection }"><IconIntersection />Intersect°</button>
        <button class="icon" @click="changeColor_feu()" :style="{ backgroundColor: bgColor_feu }"><IconFeu />Feu</button>
        <button class="icon" @click="changeColor_priorite()" :style="{ backgroundColor: bgColor_priorite }"><IconPriorite />Priorité</button>
        <button class="icon" @click="changeColor_pieton()" :style="{ backgroundColor: bgColor_pieton }"><IconPieton />Pieton</button>
        <button class="icon" @click="changeColor_depart()" :style="{ backgroundColor: bgColor_depart }"><IconDepart />Depart</button>
        <button class="icon" @click="changeColor_fin()" :style="{ backgroundColor: bgColor_fin }"><IconFin />Fin</button>
        <button class="icon" @click="changeColor_selection()" :style="{ backgroundColor: bgColor_selection }"><IconSelection />Selection</button>
        <button class="icon_bas" @click="changeColor_parametres()" :style="{ backgroundColor: bgColor_parametres }"><IconParametre />Paramètres</button>
    </div>
</template>

<style scoped>
.toolbar {
    position: absolute;
    display: flex;
    align-items: center;
    flex-direction: column;
    background-color: var(--color-left-bar-1);
    left: 0;
    top: 5vh;
    height: 95vh;
    width: 5vw;
}

.icon {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    aspect-ratio: 1/1;
    color: var(--color-text);
    border: none;
    cursor: pointer;
    gap: 10px;
    font-size: 10px;
    font-weight: 400;
}

.icon_bas {
    position: absolute;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    aspect-ratio: 1/1;
    background-color: transparent;
    color: var(--color-text);
    border: none;
    cursor: pointer;
    gap: 10px;
    font-size: 10px;
    font-weight: 400;
    bottom: 0;
}
</style>