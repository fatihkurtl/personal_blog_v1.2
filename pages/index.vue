<template>
  <div class="md:container md:mx-auto bg-white dark:bg-slate-800">
    <div class="md:flex md:justify-center">
      <div class="md:w-1/2 md:p-4 mt-6">
        <About/>
      </div>
      <div class="md:w-1/2 md:p-4 max-w-sm mt-6 ml-2">
        <Profile />
      </div>
    </div>
  </div>
</template>
<script setup>
import Profile from "~/layouts/Profile.vue";
import About from "~/layouts/About.vue";
</script>

<style scoped>



</style>
