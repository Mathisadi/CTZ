<script lang="ts">
import { defineComponent } from 'vue';
import Topbar from '../components/Appli/Topbar.vue';

export default defineComponent({
    components: {
        Topbar,
    },

    return () {
        Topbar
    }
})
</script>

<template>
    <body>
        <Topbar />
    </body>
</template>