<script lang="ts">
import { defineComponent } from 'vue';
import Topbar from '../components/Menu/Topbar.vue';
import Leftbar from '../components/Menu/Leftbar.vue';

export default defineComponent({
    components: {
        Topbar,
        Leftbar
    },
})

</script>


<template>
    <body>
        <Topbar />
        <Leftbar />
    </body>
</template>
