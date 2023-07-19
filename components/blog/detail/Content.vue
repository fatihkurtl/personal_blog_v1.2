<template>
    <div class="prose prose-blockquote:dark:bg-gray-600 prose-blockquote:bg-gray-200 prose-img:rounded-xl md:prose-lg lg:prose-xl dark:prose-invert max-w-none dark:text-gray-100 prose-p text-gray-700 mb-4"
        v-html="renderedContent"></div>
</template>

<script setup>
defineProps({
    renderedContent: {
        type: String,
        required: true
    }
});
</script>

<style>
blockquote {
    background-color: #363535;
    border-left-color: #b7abab !important;
    color: #f3f4f6;
    border-top: 1px solid transparent;
    border-bottom: 1px solid transparent;
    padding-right: 8px;
    margin-top: 1.6em;
    margin-bottom: 1.6em;
    padding-left: 1.0666667em;
    font-weight: 500;
    font-style: italic;
    border-left-width: 0.25rem;
    quotes: "\201C" "\201D" "\2018" "\2019";
}
</style>