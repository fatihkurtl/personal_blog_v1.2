<template>
  <NuxtLayout>
    <div class="dark:bg-slate-800 bg-white" style="position: relative; min-height: 100vh;">
      <Navbar />
      <NuxtPage />
      <Footer />
    </div>
  </NuxtLayout>
</template>

<script setup>
import Navbar from '~/layouts/Navbar.vue';
import Footer from '~/layouts/Footer.vue';
</script>

<style>
.page-enter-active,
.page-leave-active {
  transition: all 0.4s;
}

.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(1rem);
}
</style>