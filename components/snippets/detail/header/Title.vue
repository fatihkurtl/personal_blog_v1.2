<template>
    <h1
        class="text-[34px] font-extrabold leading-10 tracking-tight text-gray-900 dark:text-gray-100 md:text-5xl md:leading-14 lg:text-[54px] lg:leading-[64px]">
        {{ title }}
    </h1>
</template>

<script setup>
defineProps({
    title: {
        type: String,
        required: true
    }
});
</script>