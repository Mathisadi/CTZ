<template>
  <div>
    <button @click="getResponse">Obtenir la réponse</button>
    <!-- Affiche la réponse formatée -->
    <pre>{{ responseData }}</pre>
  </div>
</template>

<script setup>
import { ref } from "vue";

const responseData = ref(null);

const data = {
  nom: "test",
  sens: "test",
  proba_g: 0.5,
  proba_d: 0.5,
  proba_b: 0.5,
  proba_h: 0.5,
  len: 100, 
};

const getResponse = async () => {
  try {
    const response = await fetch("/api/build/3/route", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    const result = await response.json();
    responseData.value = result;
  } catch (error) {
    console.error("Erreur:", error);
  }
};

</script>
