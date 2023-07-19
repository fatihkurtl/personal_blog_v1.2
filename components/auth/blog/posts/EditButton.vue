<template>
    <NuxtLink :to="{
        path: `/auth/blog/edit/${id}`,
        query: { post: title },
    }" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</NuxtLink>
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