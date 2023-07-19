<template>
  <nav :class="['border-gray-200 bg-white dark:bg-slate-800 dark:border-gray-700 sticky top-0 z-10', { 'backdrop-filter backdrop-blur opacity-75': isScrolled }]">
  <div class="md:py-0 py-0">
  <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4 md:py-1.5">
    <ProfilePicture/>
    <MobileButton/>
    <div class="hidden w-full md:block md:w-auto" id="navbar-solid-bg">
      <ul class="flex flex-col items-center justify-center md:flex-row md:space-x-8 font-medium mt-4 rounded-lg bg-gray-50 md:mt-0 md:border-0 md:bg-transparent dark:bg-gray-800 md:dark:bg-transparent dark:border-gray-700">
        <Route/>
        <li>
          <ThemeButton/>
        </li>
      </ul>
    </div>
  </div>
  </div>
</nav>

</template>

<script setup>
import ProfilePicture from '~/components/navbar/ProfilePicture.vue';
import Route from '~/components/navbar/Route.vue';
import MobileButton from '~/components/navbar/MobileButton.vue';
import ThemeButton from '~/components/navbar/ThemeButton.vue';


// console.log("isDark.value :>> ", isDark.value);


const isScrolled = ref(false);
onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

const handleScroll = () => {
  isScrolled.value = window.pageYOffset > 0;
};

</script>

<style>
.navbar-scroll {
  opacity: 100;
  backdrop-filter: blur(10px);
}
.text-base {
  font-size: 1.15rem;
}
</style>