<template>
    <NuxtLink :to="{ path: `/blog/${id}`, query: { post: title } }"
        class="inline-block dark:bg-slate-700 dark:hover:bg-slate-600 bg-slate-400 hover:bg-slate-500 rounded-md px-3 py-1 text-sm font-medium text-white">
        Read More</NuxtLink>
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
    },
});
</script>