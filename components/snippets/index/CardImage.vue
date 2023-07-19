<template>
    <div class="p-3 lg:p-4">
        <div class="w-28 h-28 md:w-28 md:h-28">
            <img class="object-cover w-full h-full border-slate-800 md:h-full md:w-full" :src="`${image}`" alt="" />
        </div>
    </div>
</template>

<script setup>
defineProps({
    image: {
        type: String,
        required: true
    }
});
</script>