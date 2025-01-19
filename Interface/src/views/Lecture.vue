<script lang="ts">
import { defineComponent } from 'vue';
import Topbar from '@/components/Appli/Topbar.vue';
import Toolbar from '@/components/Appli/Toolbar.vue';

export default defineComponent({
    components: {
        Topbar,
        Toolbar
    },
})
</script>

<template>
    <body>
        <Topbar />
        <Toolbar />
    </body>
</template>