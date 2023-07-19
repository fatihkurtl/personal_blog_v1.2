<template>
    <div class="flex flex-col space-y-1.5">
        <nuxt-link class="hover:underline bg-inherit font-poppins" to="/blog">
            <Writings/>
        </nuxt-link>
        <nuxt-link class="hover:underline bg-inherit font-poppins" to="/snippets">
        <Collections/>
    </nuxt-link>
</div>
</template>

<script setup>
import Writings from './Writings.vue'; 
import Collections from './Collections.vue'; 
</script>