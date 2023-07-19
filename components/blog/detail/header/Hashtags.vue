<template>
    <div class="flex items-center">
        <a href="#"
            class="inline-block text-blue-500 dark:text-blue-400 hover:text-blue-600 dark:hover:text-blue-300 md:text-base px-1 py-1">{{
                hashtags[0] }}</a>
        <a href="#" v-if="hashtags[1]"
            class="inline-block text-blue-500 dark:text-blue-400 hover:text-blue-600 dark:hover:text-blue-300 px-1 py-1 md:text-base">{{
                hashtags[1] }}</a>
        <a href="#" v-if="hashtags[2]"
            class="inline-block text-blue-500 dark:text-blue-400 hover:text-blue-600 dark:hover:text-blue-300 px-1 py-1 md:text-base">{{
                hashtags[2] }}</a>
    </div>
</template>

<script setup>

defineProps({
    hashtags: {
        type: Array,
        required: true
    }
});

</script>