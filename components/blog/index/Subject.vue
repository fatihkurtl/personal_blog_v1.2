<template>
    <p id="subject" class="text-gray-600 max-w-none dark:text-gray-400 mb-4">
        {{ subject }}
    </p>
</template>

<script setup>
defineProps({
    subject: {
        type: String,
        required: true
    }
});
</script>