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
import { useStorePinia } from "~/stores/myStore";
import Profile from "~/layouts/Profile.vue";
import About from "~/layouts/About.vue";
import { useDark, useToggle } from "@vueuse/core";

const useStore = useStorePinia();
const isDark = useDark();
console.log("isDark.value :>> ", isDark.value);

</script>

<style>



</style>
