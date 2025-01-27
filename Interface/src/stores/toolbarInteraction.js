import { ref } from 'vue';
import { defineStore } from 'pinia';

export const toolbarInteraction = defineStore('toolbarInteraction', () => {
    const bgColor_route =  ref('transparent');
    const bgColor_intersection = ref('transparent');
    const bgColor_feu = ref('transparent');
    const bgColor_priorite = ref('transparent');
    const bgColor_pieton = ref('transparent');
    const bgColor_depart = ref('transparent');
    const bgColor_fin = ref('transparent');
    const bgColor_selection = ref('transparent');
    const bgColor_parametres = ref('transparent');

    const isRouteToogle = ref(false);
    const isIntersectionToogle = ref(false);
    const isFeuToogle = ref(false);
    const isPrioriteToogle = ref(false);
    const isPietonToogle = ref(false);
    const isDepartToogle = ref(false);
    const isFinToogle = ref(false);
    const isSelectionToogle = ref(false);
    const isParametresToogle = ref(false);

    const changeColor_route = () => {
        // Change la couleur de fond
        bgColor_route.value = 'var(--color-left-bar-2)'; // Change la couleur de fond
        bgColor_intersection.value = 'transparent';
        bgColor_feu.value = 'transparent';
        bgColor_priorite.value = 'transparent';
        bgColor_pieton.value = 'transparent';
        bgColor_depart.value = 'transparent';
        bgColor_fin.value = 'transparent';
        bgColor_selection.value = 'transparent';
        bgColor_parametres.value = 'transparent';

        // Mettre à jour l'état des boutons
        isRouteToogle.value = true;
        isIntersectionToogle.value = false;
        isFeuToogle.value = false;
        isPrioriteToogle.value = false;
        isPietonToogle.value = false;
        isDepartToogle.value = false;
        isFinToogle.value = false;
        isSelectionToogle.value = false;
        isParametresToogle.value = false;
    }
    
    const changeColor_intersection = () => {
        // Change la couleur de fond
        bgColor_route.value = 'transparent';
        bgColor_intersection.value = 'var(--color-left-bar-2)';
        bgColor_feu.value = 'transparent';
        bgColor_priorite.value = 'transparent';
        bgColor_pieton.value = 'transparent';
        bgColor_depart.value = 'transparent';
        bgColor_fin.value = 'transparent';
        bgColor_selection.value = 'transparent';
        bgColor_parametres.value = 'transparent';

        // Mettre à jour l'état des boutons
        isRouteToogle.value = false;
        isIntersectionToogle.value = true;
        isFeuToogle.value = false;
        isPrioriteToogle.value = false;
        isPietonToogle.value = false;
        isDepartToogle.value = false;
        isFinToogle.value = false;
        isSelectionToogle.value = false;
        isParametresToogle.value = false;
    }

    const changeColor_feu = () => {
        // Change la couleur de fond
        bgColor_route.value = 'transparent';
        bgColor_intersection.value = 'transparent';
        bgColor_feu.value = 'var(--color-left-bar-2)';
        bgColor_priorite.value = 'transparent';
        bgColor_pieton.value = 'transparent';
        bgColor_depart.value = 'transparent';
        bgColor_fin.value = 'transparent';
        bgColor_selection.value = 'transparent';
        bgColor_parametres.value = 'transparent';

        // Mettre à jour l'état des boutons
        isRouteToogle.value = false;
        isIntersectionToogle.value = false;
        isFeuToogle.value = true;
        isPrioriteToogle.value = false;
        isPietonToogle.value = false;
        isDepartToogle.value = false;
        isFinToogle.value = false;
        isSelectionToogle.value = false;
        isParametresToogle.value = false;
    }   

    const changeColor_priorite = () => {
        // Change la couleur de fond
        bgColor_route.value = 'transparent';
        bgColor_intersection.value = 'transparent';
        bgColor_feu.value = 'transparent';
        bgColor_priorite.value = 'var(--color-left-bar-2)';
        bgColor_pieton.value = 'transparent';
        bgColor_depart.value = 'transparent';
        bgColor_fin.value = 'transparent';
        bgColor_selection.value = 'transparent';
        bgColor_parametres.value = 'transparent';

        // Mettre à jour l'état des boutons
        isRouteToogle.value = false;
        isIntersectionToogle.value = false;
        isFeuToogle.value = false;
        isPrioriteToogle.value = true;
        isPietonToogle.value = false;
        isDepartToogle.value = false;
        isFinToogle.value = false;
        isSelectionToogle.value = false;
        isParametresToogle.value = false;
    }

    const changeColor_pieton = () => {
        // Change la couleur de fond
        bgColor_route.value = 'transparent';
        bgColor_intersection.value = 'transparent';
        bgColor_feu.value = 'transparent';
        bgColor_priorite.value = 'transparent';
        bgColor_pieton.value = 'var(--color-left-bar-2)';
        bgColor_depart.value = 'transparent';
        bgColor_fin.value = 'transparent';
        bgColor_selection.value = 'transparent';
        bgColor_parametres.value = 'transparent';

        // Mettre à jour l'état des boutons
        isRouteToogle.value = false;
        isIntersectionToogle.value = false;
        isFeuToogle.value = false;
        isPrioriteToogle.value = false;
        isPietonToogle.value = true;
        isDepartToogle.value = false;
        isFinToogle.value = false;
        isSelectionToogle.value = false;
        isParametresToogle.value = false;
    }

    const changeColor_depart = () => {
        // Change la couleur de fond
        bgColor_route.value = 'transparent';
        bgColor_intersection.value = 'transparent';
        bgColor_feu.value = 'transparent';
        bgColor_priorite.value = 'transparent';
        bgColor_pieton.value = 'transparent';
        bgColor_depart.value = 'var(--color-left-bar-2)';
        bgColor_fin.value = 'transparent';
        bgColor_selection.value = 'transparent';
        bgColor_parametres.value = 'transparent';

        // Mettre à jour l'état des boutons
        isRouteToogle.value = false;
        isIntersectionToogle.value = false;
        isFeuToogle.value = false;
        isPrioriteToogle.value = false;
        isPietonToogle.value = false;
        isDepartToogle.value = true;
        isFinToogle.value = false;
        isSelectionToogle.value = false;
        isParametresToogle.value = false;
    }

    const changeColor_fin = () => {
        // Change la couleur de fond
        bgColor_route.value = 'transparent';
        bgColor_intersection.value = 'transparent';
        bgColor_feu.value = 'transparent';
        bgColor_priorite.value = 'transparent';
        bgColor_pieton.value = 'transparent';
        bgColor_depart.value = 'transparent';
        bgColor_fin.value = 'var(--color-left-bar-2)';
        bgColor_selection.value = 'transparent';
        bgColor_parametres.value = 'transparent';

        // Mettre à jour l'état des boutons
        isRouteToogle.value = false;
        isIntersectionToogle.value = false;
        isFeuToogle.value = false;
        isPrioriteToogle.value = false;
        isPietonToogle.value = false;
        isDepartToogle.value = false;
        isFinToogle.value = true;
        isSelectionToogle.value = false;
        isParametresToogle.value = false;
    }

    const changeColor_selection = () => {
        // Change la couleur de fond
        bgColor_route.value = 'transparent';
        bgColor_intersection.value = 'transparent';
        bgColor_feu.value = 'transparent';
        bgColor_priorite.value = 'transparent';
        bgColor_pieton.value = 'transparent';
        bgColor_depart.value = 'transparent';
        bgColor_fin.value = 'transparent';
        bgColor_selection.value = 'var(--color-left-bar-2)';
        bgColor_parametres.value = 'transparent';

        // Mettre à jour l'état des boutons
        isRouteToogle.value = false;
        isIntersectionToogle.value = false;
        isFeuToogle.value = false;
        isPrioriteToogle.value = false;
        isPietonToogle.value = false;
        isDepartToogle.value = false;
        isFinToogle.value = false;
        isSelectionToogle.value = true;
        isParametresToogle.value = false;
    }

    const changeColor_parametres = () => {
        // Change la couleur de fond
        bgColor_route.value = 'transparent';
        bgColor_intersection.value = 'transparent';
        bgColor_feu.value = 'transparent';
        bgColor_priorite.value = 'transparent';
        bgColor_pieton.value = 'transparent';
        bgColor_depart.value = 'transparent';
        bgColor_fin.value = 'transparent';
        bgColor_selection.value = 'transparent';
        bgColor_parametres.value = 'var(--color-left-bar-2)';

        // Mettre à jour l'état des boutons
        isRouteToogle.value = false;
        isIntersectionToogle.value = false;
        isFeuToogle.value = false;
        isPrioriteToogle.value = false;
        isPietonToogle.value = false;
        isDepartToogle.value = false;
        isFinToogle.value = false;
        isSelectionToogle.value = false;
        isParametresToogle.value = true;
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
        changeColor_parametres,
        isRouteToogle,
        isIntersectionToogle,
        isFeuToogle,
        isPrioriteToogle,
        isPietonToogle,
        isDepartToogle,
        isFinToogle,
        isSelectionToogle,
        isParametresToogle
    }
});