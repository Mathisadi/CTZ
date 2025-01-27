import { ref } from 'vue';
import { defineStore } from 'pinia';

export const mouvement = defineStore('mouvement', () => {
    // Constante de la grille
    const offset = ref({ x: -5090, y: -5070 });
    const startPosition = ref({ x: 0, y: 0 });
    const isDraging = ref(false);

    // Drag
    function startDrag(event){
        isDraging.value = true;
        startPosition.value = { x: event.clientX, y: event.clientY };
    };

    function onDrag(event){
    if (isDraging.value) {
        const dx = event.clientX - startPosition.value.x;
        const dy = event.clientY - startPosition.value.y;
        offset.value.x += dx;
        offset.value.y += dy;
        startPosition.value = { x: event.clientX, y: event.clientY };
    }
    };

    function endDrag(){
        isDraging.value = false;
    };

    return { offset, startPosition, startDrag, onDrag, endDrag };
});



