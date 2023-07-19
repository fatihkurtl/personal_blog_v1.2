<template>
    <div class="space-y-2 pt-6 pb-8 md:space-y-5">
        <nav class="flex justify-between dark:text-gray-100 text-gray-600 font-medium">
            <button @click="loadPrevPage">Previous</button>
            <span>{{ currentPage }} of
                {{ totalPages }}</span>
            <button @click="loadNextPage">Next</button>
        </nav>
    </div>
</template>

<script setup>
const loadPrevPage = inject('loadPrevPage');
const loadNextPage = inject('loadNextPage');
const currentPage = inject('currentPage');
const totalPages = inject('totalPages');
</script>