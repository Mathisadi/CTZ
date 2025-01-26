<script>
import { ref, onUnmounted } from "vue";

export default{
  name: "VerticalRuler",
  setup() {
    const rulerRef = ref(null); // Référence de la règle
    const marks = Array.from({ length: 100 }, (_, i) => i * 10); // Graduation chaque 10px
    const guides = ref([]); // Liste des positions des repères
    const draggingGuideIndex = ref(null); // Index du repère en cours de déplacement

    // Ajouter un repère à l'endroit cliqué
    const addGuide = (event) => {
      const rulerBounds = rulerRef.value.getBoundingClientRect();
      const position = event.clientY - rulerBounds.top; // Position relative à la règle
      guides.value.push(position);
    };

    // Début du déplacement d'un repère
    const startDragging = (index) => {
      draggingGuideIndex.value = index;
      document.addEventListener("mousemove", onMouseMove);
      document.addEventListener("mouseup", stopDragging);
    };

    // Déplacement d'un repère
    const onMouseMove = (event) => {
      if (draggingGuideIndex.value === null) return;

      const rulerBounds = rulerRef.value.getBoundingClientRect();
      let position = event.clientY - rulerBounds.top;

      // Conserver le repère dans les limites de la règle
      if (position < 0) position = 0;
      if (position > rulerBounds.height) position = rulerBounds.height;

      // Mettre à jour la position du repère
      guides.value[draggingGuideIndex.value] = position;
    };

    // Fin du déplacement
    const stopDragging = () => {
      draggingGuideIndex.value = null;
      document.removeEventListener("mousemove", onMouseMove);
      document.removeEventListener("mouseup", stopDragging);
    };

    // Nettoyer les événements quand le composant est détruit
    onUnmounted(() => {
      document.removeEventListener("mousemove", onMouseMove);
      document.removeEventListener("mouseup", stopDragging);
    });

    return {
      rulerRef,
      marks,
      guides,
      addGuide,
      startDragging,
    };
  },
};
</script>

<template>
    <div class="vertical-ruler" ref="rulerRef" @click="addGuide">
      <!-- Affichage des graduations -->
      <div v-for="mark in marks" :key="mark" class="mark" :style="{ top: `${mark}px` }"></div>
  
      <!-- Affichage des repères (guides) -->
      <div
        v-for="(guide, index) in guides"
        :key="index"
        class="guide"
        :style="{ top: `${guide}px` }"
        @mousedown="startDragging(index)"
      ></div>
    </div>
</template>
  

<style>
  .vertical-ruler {
    position: relative;
    width: 50px; /* Largeur de la règle */
    height: 100vh; /* Hauteur de la règle */
    background-color: #f5f5f5; /* Couleur de fond */
    border-right: 1px solid #ccc; /* Bordure droite */
    user-select: none; /* Désactiver la sélection de texte */
    cursor: crosshair;
  }
  
  .mark {
    position: absolute;
    left: 0;
    width: 100%;
    height: 1px;
    background-color: #ccc; /* Couleur des graduations */
  }
  
  .mark:nth-child(5n) {
    background-color: #888; /* Graduations plus marquées tous les 5 pas */
  }
  
  .guide {
    position: absolute;
    left: 0;
    width: 100%;
    height: 1px;
    background-color: red; /* Couleur des repères */
    cursor: pointer;
  }
  </style>
  