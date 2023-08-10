<template>
    <input type="text" v-model="searchQuery" @change="searchPosts($event.target.value)"
        class="w-full dark:bg-slate-900 rounded-lg px-4 py-2 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-600"
        placeholder="Search blog posts..." />
</template>

<script setup>

const searchQuery = inject('searchQuery');
const searchPosts = inject('searchPosts');

</script>