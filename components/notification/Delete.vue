<template>
  <transition name="slide-fade">
    <div class="fixed inset-0 flex items-center justify-center animate-pulse">
      <div
        class="max-w-md mx-auto bg-red-700 dark:bg-red-800 rounded-lg shadow-lg overflow-hidden"
      >
        <div class="flex items-center justify-between p-4">
          <div class="flex items-center">
            <svg
              class="h-6 w-6 text-red-500 mr-2 animate-pulse"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
            <p class="text-lg font-medium text-white">Successfull!</p>
          </div>
        </div>
        <div class="px-4 py-2">
          <p class="font-medium text-white dark:text-white">
            Post successfully deleted!
          </p>
        </div>
      </div>
    </div>
  </transition>
</template>
