<template>
  <div
    class="bg-white dark:text-white rounded-lg overflow-hidden shadow-lg shadow-blue-500/50 hover:shadow-blue-500 border-gray-300 border-solid hover:border-blue-500 hover:shadow-2xl transform hover:scale-110 duration-300">
    <div class="dark:bg-slate-700 bg-white shadow-lg rounded-lg overflow-hidden">
      <div class="bg-cover bg-center h-56" style="background-image: url('https://picsum.photos/600/300')"></div>
      <Info />
      <Icon />
      <div class="h-1.5 bg-gradient-to-r from-green-300 via-blue-500 to-purple-600"></div>
    </div>
  </div>
</template>

<script setup>
import Info from "~/components/profile/Info.vue";
import Icon from "~/components/profile/social/Icon.vue";

</script>
