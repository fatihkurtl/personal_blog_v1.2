<template>
<span class="text-sm text-gray-700 dark:text-gray-400">
          Showing
          <span class="font-semibold text-gray-900 dark:text-white">{{ currentPage }}</span> to
          <span class="font-semibold text-gray-900 dark:text-white">{{ totalPages }}</span> of
          <span class="font-semibold text-gray-900 dark:text-white">{{
            totalPosts
          }}</span>
          Entries
        </span>
</template>

<script setup>
defineProps({
    currentPage: {
        type: Number,
        required: true
    },
    totalPages: {
        type: Number,
        required: true
    },
    totalPosts: {
        type: Number,
        required: true
    },
});
</script>