<template>
    <button
      aria-label="Scroll To Top"
      type="button"
      @click="scrollToTop"
      :style="{ opacity: showScrollButton ? '1' : '0' }"
      class="fixed right-8 bottom-8 hidden rounded-md bg-gray-700 p-2 text-gray-100 transition-opacity hover:bg-gray-800 dark:hover:bg-gray-600 md:inline-block"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
      >
        <path
          fill="currentColor"
          d="M12 20q-.425 0-.713-.288T11 19V7.825L6.125 12.7q-.3.3-.713.3t-.712-.3q-.3-.3-.3-.7t.3-.7l6.6-6.6q.15-.15.325-.212T12 4.425q.2 0 .388.063t.312.212l6.6 6.6q.3.3.3.7t-.3.7q-.3.3-.713.3t-.712-.3L13 7.825V19q0 .425-.288.713T12 20Z"
        />
      </svg>
    </button>
</template>
  
<script setup>
  const showScrollButton = ref(false);
  
  const handleScroll = () => {
    const scrollPosition =
      window.pageYOffset ||
      document.documentElement.scrollTop ||
      document.body.scrollTop ||
      0;
    const windowHeight = window.innerHeight;
    const fullHeight = document.documentElement.scrollHeight;
  
    showScrollButton.value =
      scrollPosition > windowHeight / 2 &&
      scrollPosition + windowHeight < fullHeight;
  };
  
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  };
  
  onMounted(() => {
    window.addEventListener("scroll", handleScroll);
  });
  
  onBeforeUnmount(() => {
    window.removeEventListener("scroll", handleScroll);
  });
</script>
  