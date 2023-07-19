<template>
    <div class="flex flex-col justify-between p-2 leading-normal">
        <h5 class="mb-1 font-bold tracking-tight text-gray-900 dark:text-white">
            {{ title }}
        </h5>
        <p class="mb-2 text-sm font-bold text-gray-500 dark:text-gray-400">
            {{ subject }}
        </p>
    </div>
</template>

<script setup>
defineProps({
    title: {
        type: String,
        required: true
    },
    subject: {
        type: String,
        required: true
    }
});
</script>