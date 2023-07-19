<script setup>
import { useStorePinia } from "~/stores/myStore";

const useStore = useStorePinia();
</script>

<template>
    <h1 v-if="useStore.getAuth != true && useStore.getAuth == null"
        class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
        Sign in to your account
    </h1>
    <h1 v-if="useStore.getAuth == false"
        class="text-xl font-bold leading-tight tracking-tight text-red-500 md:text-2xl dark:text-red-500">
        Username or password is incorrect
    </h1>
    <h1 v-if="useStore.getAuth == true"
        class="text-xl font-bold leading-tight tracking-tight text-green-500 md:text-2xl dark:text-green-500">
        Login successful
    </h1>
</template>