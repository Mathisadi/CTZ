<template>
    <div class="video-container">
        <video src="../../res/animation.mp4" controls class="video"></video>
    </div>
</template>

<style scoped>
.video-container {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    justify-content: center;
    align-items: center;
}

.video {
    border-radius: 3px;
}
</style>