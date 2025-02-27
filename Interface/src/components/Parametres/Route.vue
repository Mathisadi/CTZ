<script>
import { ref } from "vue";
import Dropbox from "../common/Dropbox.vue";
import Input from "../common/Input.vue";

export default {
  components: {
    Dropbox,
    Input
  },

  setup() {
    const isOpenDrop1 = ref(false);
    const items = ["G", "B", "D", "H"];
    const items_fullname = ["Gauche", "Bas", "Droite", "Haut"];
    const selectedDrop_1 = ref([]);

    const toggleDropdown = () => {
      isOpenDrop1.value = !isOpenDrop1.value;
    };

    return {
      isOpenDrop1,
      items,
      items_fullname,
      selectedDrop_1,
      toggleDropdown,
    };
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
        <p class="nom-parametre">Sens route</p>
        <!-- Dropdown -->
        <Dropbox :type="'route'" :param="'sens'" />
      </div>
      <!-- Direction -->
      <div class="parametre">
        <p class="nom-parametre">Direction possible</p>
        <!-- Dropdown -->
        <Dropbox :type="'route'" :param="'direction'" />
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
