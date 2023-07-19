<template>
  <div class="px-4 py-2">
    <h2 class="font-poppins text-xl text-gray-600 dark:text-white mb-2">
      {{ response.name }}
    </h2>
    <p class="text-base font-poppins text-gray-600 dark:text-white mb-4">
      {{ response.title }}
    </p>
    <ul class="text-base text-white">
      <li class="mb-2 flex items-center">
        <svg class="mr-2 font-thin text-gray-600 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
          width="20" height="20" fill="none" viewBox="0 0 20 20">
          <path stroke="currentColor" stroke-linecap="round" stroke-width="2"
            d="M1 10c1.5 1.5 5.25 3 9 3s7.5-1.5 9-3m-9-1h.01M2 19h16a1 1 0 0 0 1-1V6a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1ZM14 5V3a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v2h8Z" />
        </svg>
        <span class="font-poppins mr-2 text-gray-600 dark:text-white">{{ response.work }}</span>
      </li>
      <li class="mb-2 flex items-center">
        <svg xmlns="http://www.w3.org/2000/svg" class="mr-2 text-gray-600 dark:text-white" width="20" height="20"
          viewBox="0 0 512 512">
          <path fill="currentColor"
            d="M256 89.61L22.486 177.18L256 293.937l111.22-55.61l-104.337-31.9A16 16 0 0 1 256 208a16 16 0 0 1-16-16a16 16 0 0 1 16-16l-2.646 8.602l18.537 5.703a16 16 0 0 1 .008.056l27.354 8.365L455 246.645v12.146a16 16 0 0 0-7 13.21a16 16 0 0 0 7.293 13.406C448.01 312.932 448 375.383 448 400c16 10.395 16 10.775 32 0c0-24.614-.008-87.053-7.29-114.584A16 16 0 0 0 480 272a16 16 0 0 0-7-13.227v-25.42L413.676 215.1l75.838-37.92L256 89.61zM119.623 249L106.5 327.74c26.175 3.423 57.486 18.637 86.27 36.627c16.37 10.232 31.703 21.463 44.156 32.36c7.612 6.66 13.977 13.05 19.074 19.337c5.097-6.288 11.462-12.677 19.074-19.337c12.453-10.897 27.785-22.128 44.156-32.36c28.784-17.99 60.095-33.204 86.27-36.627L392.375 249h-6.25L256 314.063L125.873 249h-6.25z" />
        </svg>
        <span class="font-poppins mr-2 text-gray-600 dark:text-white">{{ response.graduate }}</span>
      </li>
      <li class="mb-2 flex items-center">
        <svg class="mr-2 font-thin text-gray-600 dark:text-white" width="20" height="20" aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 21">
          <g stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
            <path d="M8 12a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z" />
            <path
              d="M13.8 12.938h-.01a7 7 0 1 0-11.465.144h-.016l.141.17c.1.128.2.252.3.372L8 20l5.13-6.248c.193-.209.373-.429.54-.66l.13-.154Z" />
          </g>
        </svg>
        <span class="font-poppins mr-2 text-gray-600 dark:text-white">{{ response.location }}</span>
        <!-- <Flag/> -->
      </li>
      <li class="mb-2 flex items-center text-gray-600 dark:text-white">
        <svg class="mr-2 text-gray-600 dark:text-white" width="20" height="20" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
          fill="none" viewBox="0 0 20 16">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="m19 2-8.4 7.05a1 1 0 0 1-1.2 0L1 2m18 0a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1m18 0v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2" />
        </svg>
        <a href="mailto:fatihkurt.dev@gmail.com" class="font-poppins mr-2 text-gray-600 dark:text-white">{{ response.email
        }}</a>
      </li>
    </ul>
  </div>
</template>

<script setup>
const response = await $fetch('/api/profile');
</script>