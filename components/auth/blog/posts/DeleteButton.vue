<template>
    <a href="#" @click="deletePost(id)"
        class="ml-3 font-medium text-blue-600 dark:text-blue-500 hover:text-red-600 dark:hover:text-red-600 hover:underline">Delete</a>
</template>

<script setup>
defineProps({
    id: {
        type: Number,
        required: true
    }
});

const deletePost = inject('deletePost');
</script>