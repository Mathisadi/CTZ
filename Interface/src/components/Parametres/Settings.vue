<script>
import Dropbox from "../common/Dropbox.vue";
import Input from "../common/Input.vue";

export default {
  components: {
    Dropbox,
    Input
  },
};
</script>

<template>
  <div class="container">
    <div class="title">
      <p>Paramètres Route</p>
    </div>
    <div class="parametre-container">
      <!-- Nom de la route -->
      <div class="parametre">
        <p class="nom-parametre">Nom</p>
        <!-- Input -->
        <Input :type="'route'" :param="'nom'" />
      </div>
      <!-- Sens de la route -->
      <div class="parametre">
        <p class="nom-parametre">Sens</p>
        <!-- Dropdown -->
        <Dropbox :type="'route'" :param="'sens'" />
      </div>
      <!-- Proba de touner à gauche  -->
      <div class="parametre">
        <p class="nom-parametre">Proba dir gauche</p>
        <!-- Input -->
        <Input :type="'route'" :param="'proba-gauche'" />
      </div>
      <!-- Proba de touner à droite  -->
      <div class="parametre">
        <p class="nom-parametre">Proba dir droite</p>
        <!-- Input -->
        <Input :type="'route'" :param="'proba-droite'" />
      </div>
      <!-- Proba de tourner en bas -->
      <div class="parametre">
        <p class="nom-parametre">Proba dir bas</p>
        <!-- Input -->
        <Input :type="'route'" :param="'proba-bas'" />
      </div>
      <!-- Proba de tourner en haut -->
      <div class="parametre">
        <p class="nom-parametre">Proba dir haut</p>
        <!-- Input -->
        <Input :type="'route'" :param="'proba-haut'" />
      </div>
      <!-- Longeur de la route -->
      <div class="parametre">
        <p class="nom-parametre">Longueur de la route</p>
        <!-- Input -->
        <Input :type="'route'" :param="'len'" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  background-color: transparent;
  padding: 10px;
  gap: 20px;
}

.title {
  border: none;
  padding-bottom: 6px;
  padding-left: 6px;
  border-bottom: var(--color-underline) solid 1px;
  font-size: 14px;
  font-weight: 700;
}

.parametre-container {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.parametre {
  display: flex;
  flex-direction: row;
  align-items:end;
  gap: 10px;
  border: none;
  padding-left: 6px;
  padding-right: 6px;
}

.nom-parametre {
  border: none;
  flex: auto;
  font-size: 12px;
  font-weight: 400;
}

</style>
