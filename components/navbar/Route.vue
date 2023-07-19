<template>
    <li v-if="!route.name.includes('auth')">
        <NuxtLink to="/blog" exact
            class="font-lato text-base block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-gray-200 md:border-0 md:hover:text-gray-900 md:p-2 md:py-1 dark:text-white md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white"
            active-class="border-b-2 dark:bg-gray-700 bg-gray-300">
            Blog
        </NuxtLink>
    </li>
    <li v-if="route.name.includes('auth') && useStore.getAuth">
        <NuxtLink to="/auth/blog/posts" exact
            class="font-lato text-base block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-gray-200 md:border-0 md:hover:text-gray-900 md:p-2 md:py-1 dark:text-white md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white"
            active-class="border-b-2 dark:bg-gray-700 bg-gray-300">
            Blog Admin Panel
        </NuxtLink>
    </li>
    <li v-if="!route.name.includes('auth')">
        <NuxtLink to="/snippets" exact
            class="font-lato text-base block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-gray-200 md:border-0 md:hover:text-gray-900 md:p-2 md:py-1 dark:text-white md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white"
            active-class="border-b-2 dark:bg-gray-700 bg-gray-300">
            Snippets
        </NuxtLink>
    </li>
    <li v-if="route.name.includes('auth') && useStore.getAuth">
        <NuxtLink to="/auth/snippets/posts" exact
            class="font-lato text-base block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-gray-200 md:border-0 md:hover:text-gray-900 md:p-2 md:py-1 dark:text-white md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white"
            active-class="border-b-2 dark:bg-gray-700 bg-gray-300">
            Snippets Admin Panel
        </NuxtLink>
    </li>
    <li v-if="route.name.includes('auth') && useStore.getAuth">
        <NuxtLink to="/auth/login" @click="(useStore.authUser(null))" exact
            class="font-lato text-base block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-gray-200 md:border-0 md:hover:text-gray-900 md:p-2 md:py-1 dark:text-white md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white"
            active-class="border-b-2 dark:bg-gray-700 bg-gray-300">
            Log out
        </NuxtLink>
    </li>
</template>

<script setup>
import { useStorePinia } from "~/stores/myStore";

const useStore = useStorePinia();
const route = useRoute();
</script>