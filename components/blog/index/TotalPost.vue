<template>
    <div class="text-sm dark:text-gray-100 text-gray-500 font-bold">
        <p>Showing {{ count_of_post }} results</p>
    </div>
</template>

<script setup>

defineProps({
    count_of_post: {
        type: Number,
        required: true
    }
});

</script>