<script lang="ts">
export default {
    name: "Topbar"
}
</script>

<template>
    <div class="topbar">
        <h1>CTZ</h1>
        <h2>Nom de l'utilisateur</h2>
    </div>
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
    right: 20px;
    font-size: 14px;
    font-weight: normal;
    color: var(--color-white);
}
</style>