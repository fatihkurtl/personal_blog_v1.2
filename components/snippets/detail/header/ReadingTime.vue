<template>
    <span class="ml-1.5 md:ml-2 text-gray-600 dark:text-gray-400">
        {{ reading_time }} min read
    </span>
</template>

<script setup>
defineProps({
    reading_time: {
        type: String,
        required: true
    }
});
</script>