<template>
    <button @click="toggleDark()"
        class="font-lato text-base block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-gray-200 md:border-0 md:hover:text-gray-900 md:p-2 md:py-1 dark:text-white md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white">
        <client-only>
          <span class="material-icons text-base h-6 w-6 mt-1" v-if="!isDark"> dark_mode </span>
          <span class="material-icons text-base h-6 w-6 mt-1" v-if="isDark"> light_mode </span>
        </client-only>
    </button>
</template>

<script setup>
import { useDark, useToggle } from "@vueuse/core";

const isDark = useDark();
const toggleDark = useToggle(isDark);
</script>
