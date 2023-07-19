<template>
  <transition name="slide-fade">
    <div class="fixed inset-0 flex items-center justify-center animate-pulse">
      <div
        class="max-w-md mx-auto bg-gray-200 dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden"
      >
        <div class="flex items-center justify-between p-4">
          <div class="flex items-center">
            <svg
              class="h-6 w-6 text-green-500 mr-2 animate-pulse"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M5 13l4 4L19 7"
              />
            </svg>
            <p class="text-lg font-medium text-green-700">Success !</p>
          </div>
        </div>
        <div class="px-4 py-2">
          <p
            v-if="
              route.name == 'auth-blog-share' ||
              route.name == 'auth-snippets-share'
            "
            class="font-medium text-gray-700 dark:text-gray-200"
          >
            Post Successfully Shared.
          </p>
          <p
            v-if="
              route.name == 'auth-snippets-edit-id' ||
              route.name == 'auth-blog-edit-id'
            "
            class="font-medium text-gray-700 dark:text-gray-200"
          >
            Post Successfully Edited.
          </p>
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { useStorePinia } from "~/stores/myStore";

const useStore = useStorePinia();
const route = useRoute();
</script>
