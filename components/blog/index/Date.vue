<template>
    <div class="text-sm text-gray-500 dark:text-white">
        <p class="text-gray-600 dark:text-white">
            {{ date }}
        </p>
    </div>
</template>

<script setup>
defineProps({
    date: {
        type: String,
        required: true
    }
});
</script>

