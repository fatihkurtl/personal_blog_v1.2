<template>
    <h2 class="text-xl font-bold mb-2 dark:text-white text-gray-900">
        <NuxtLink :to="{ path: `/blog/${id}`, query: { post: title } }">
            {{ title }}</NuxtLink>
    </h2>
</template>

<script setup>
defineProps({
    id: {
        type: Number,
        required: true
    },
    title: {
        type: String,
        required: true
    }
});
</script>