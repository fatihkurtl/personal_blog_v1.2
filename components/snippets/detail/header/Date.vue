<template>
<span class="ml-1.5 md:ml-2 text-gray-600 dark:text-gray-400">{{ date }}</span>
</template>

<script setup>
defineProps({
    date: {
        type: String,
        required: true
    }
});
</script>