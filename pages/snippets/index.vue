<template>
  <div class="dark:bg-slate-800 bg-white">
    <section class="container mx-auto px-4 py-6 max-w-5xl">
      <div class="flex flex-wrap -mx-4">
        <Header />
      </div>
      <hr class="h-px my-1 bg-gray-200 border-0 dark:bg-gray-700" />
      <div class="container py-12">
        <div class="grid-cols-2 gap-6 lg:grid">
          <!-- Card -->
          <NuxtLink v-for="snippet in snippets" :key="snippet.id" :to="{ path: `/snippets/${snippet.id}`, query: {snippet: snippet.title} }"
            class="card-container relative flex flex-col items-center bg-white border border-gray-300 hover:border-gray-400 dark:hover:border-gray-200 rounded-md md:flex-row md:max-w-xl dark:border-gray-700 dark:bg-slate-800">
            <CardImage :image="snippet.image" />
            <CardContent :title="snippet.title" :subject="snippet.subject" />
          </NuxtLink>
        </div>
      </div>
      <!-- Pagination -->
      <Pagination :currentPage="currentPage" :totalPages="totalPages" />
      <!-- Pagination -->
    </section>
  </div>
</template>

<script setup>
import { useStorePinia } from "~/stores/myStore";
import { ref, onMounted, watch } from "vue";
import Header from "~/components/snippets/index/Header.vue";
import CardImage from "~/components/snippets/index/CardImage.vue";
import CardContent from "~/components/snippets/index/CardContent.vue";
import Pagination from "~/components/snippets/index/Pagination.vue";



const { baseURL } = useUtils();

const useStore = useStorePinia();
const DEFAULT_PAGE = 1;
const DEFAULT_PER_PAGE = 7;
const snippets = ref([]);
const totalSnippets = ref(0);
const totalPages = ref(0);
const prevUrl = ref(null);
const nextUrl = ref(null);
const currentPage = ref(1);


async function getSnippets(page = DEFAULT_PAGE, perPage = DEFAULT_PER_PAGE) {
  try {
    currentPage.value = page;
    const response = await $fetch(`${baseURL()}/api/snippets?page=${page}&per_page=${perPage}`);
    snippets.value = response.snippets;
    totalSnippets.value = response.total;
    totalPages.value = response.pages;
    prevUrl.value = response.prev_url;
    nextUrl.value = response.next_url;
    console.log('response :>> ', response);
    console.log('snippets :>> ', snippets.value.length);
  } catch (error) {
    console.log("Error fetching snippets:", error);
  }
}

const loadPrevPage = () => {
  if (prevUrl.value) {
    const url = new URL(prevUrl.value);
    const page = Number(url.searchParams.get("page"));
    const perPage = Number(url.searchParams.get("per_page"));
    getSnippets(page, perPage);
  }
};

const loadNextPage = () => {
  if (nextUrl.value) {
    const url = new URL(nextUrl.value);
    const page = Number(url.searchParams.get("page"));
    const perPage = Number(url.searchParams.get("per_page"));
    getSnippets(page, perPage);
  }
};

onMounted(() => {
  getSnippets();
});

provide('loadPrevPage', loadPrevPage)
provide('loadNextPage', loadNextPage)

</script>

<style></style>
