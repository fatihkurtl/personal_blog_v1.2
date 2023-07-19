<template>
  <div class="text-lg leading-8 text-gray-600 dark:text-gray-400">
    <h2
      class="bg-gradient-to-r font-lato from-yellow-600 to-red-600 dark:bg-gradient-to-l dark:from-emerald-500 dark:to-lime-600 mb-8 font-poppins bg-clip-text text-4xl font-extrabold leading-[60px] tracking-tight text-transparent md:text-7xl md:leading-[86px]">
      About me
    </h2>
    <div class="mt-4 mb-8">
      <p class="text-gray-900 dark:text-white text-lg mb-4 font-lato">
        I'm {{ response.name }} - a {{ response.title }} in
        <Flag />
      </p>
      <p class="text-gray-600 dark:text-gray-400 text-lg mb-1 font-lato">
        My goal is to explain the code in a simple, innovative, and fun way.
      </p>
      <p class="text-gray-600 dark:text-gray-400 text-lg mb-4 font-lato">Vue is my favorite ✨.</p>
    </div>
    <Routes />
    <p class="my-8 flex">
      <span class="mr-2 text-gray-600 dark:text-gray-400 font-lato">Happy reading</span>
      <img src="/about/happy_reading.svg" alt="">
    </p>
  </div>
</template>

<script setup>
import Flag from "~/components/about/Flag.vue";
import Routes from "~/components/about/Routes.vue";

const response = await $fetch('/api/profile');
</script>
