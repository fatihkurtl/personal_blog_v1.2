<template>
  <div class="bg-white dark:bg-slate-800">
    <section class="container mx-auto px-4 py-6 max-w-5xl">
      <div class="flex flex-wrap -mx-4">
        <Header />
        <div class="w-full px-4 mb-6 flex justify-between items-center">
          <div class="relative w-2/3">
            <Search />
            <SearchIcon />
          </div>
          <TotalPost :count_of_post="totalPosts" />
        </div>
        <div class="w-full px-4 mb-6" v-for="post in posts" :key="post.id">
          <hr class="h-px my-1 bg-gray-200 border-0 dark:bg-gray-700" />
          <div class="overflow-hidden p-6">
            <Title :id="post.id" :title="post.title" />
            <Hashtags :hashtags="post.hashtags" />
            <Subject :subject="post.subject" />
            <div class="flex items-center justify-between">
              <Date :date="post.create_at" />
              <ReadMore :id="post.id" :title="post.title" />
            </div>
          </div>
        </div>
      </div>
      <Pagination />
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import TotalPost from "~/components/blog/index/TotalPost.vue";
import Header from "~/components/blog/index/Header.vue";
import Title from "~/components/blog/index/Title.vue";
import Subject from "~/components/blog/index/Subject.vue";
import Hashtags from "~/components/blog/index/Hashtags.vue";
import Date from "~/components/blog/index/Date.vue";
import ReadMore from "~/components/blog/index/ReadMore.vue";
import SearchIcon from "~/components/blog/index/SearchIcon.vue";
import Search from "~/components/blog/index/Search.vue";
import Pagination from "~/components/blog/index/Pagination.vue";

const { baseURL } = useUtils();

const DEFAULT_PAGE = 1;
const DEFAULT_PER_PAGE = 7;
const posts = ref([]);
const totalPosts = ref(0);
const totalPages = ref(0);
const prevUrl = ref(null);
const nextUrl = ref(null);
const currentPage = ref(null);

const searchQuery = ref("");

const findHashtagPosts = ref("");

const searchPosts = async (e) => {
  try {
    searchQuery.value = e;
    const response = await $fetch(`${baseURL()}/api/posts?search=${searchQuery.value}`);
    if (response) {
      posts.value = response;
      totalPosts.value = response.length;
    } else {
      getPosts();
      searchQuery.value = null;
    }
  } catch (error) {
    console.log('error :>> ', error);
  }
};

watch(searchQuery, (newValue, oldValue) => {
  try {
    if (newValue === "") {
      getPosts();
    } else {
      searchPosts(newValue);
    }
  } catch (error) {
    console.log('error :>> ', error);
  }
});



// NOT WORKING
const findHashtags = async (e) => {
  try {
    findHashtagPosts.value = e;
    console.log('e :>> ', e);
    const response = await $fetch(`${baseURL()}/api/getHashtags/posts?hashtag=${findHashtagPosts.value}`);
    if (response) {
      console.log('response :>> ', response);
      posts.value = response;
      totalPosts.value = response.length;
      console.log('findHashtagPosts :>> ', findHashtagPosts.value);
    } else {
      getPosts();
      findHashtagPosts.value = null;
    }
  } catch (error) {
    console.log('error :>> ', error);
  }
};

// NOT WORKING
// watch(findHashtagPosts, (newValue, oldValue) => {
//   try {
//     if (newValue === "") {
//       getPosts();
//     } else {
//       findHashtags(newValue);
//     }
//   } catch (error) {
//     console.log('error :>> ', error);
//   }
// });




async function getPosts(page = DEFAULT_PAGE, perPage = DEFAULT_PER_PAGE) {
  try {
    currentPage.value = page;
    const response = await $fetch(`${baseURL()}/api/posts?page=${page}&per_page=${perPage}`);
    posts.value = response.posts;
    totalPosts.value = response.total;
    totalPages.value = response.pages;
    prevUrl.value = response.prev_url;
    nextUrl.value = response.next_url;
  } catch (error) {
    console.log("Error fetching posts:", error);
  }
}

const loadPrevPage = () => {
  if (prevUrl.value) {
    const url = new URL(prevUrl.value);
    const page = Number(url.searchParams.get("page"));
    const perPage = Number(url.searchParams.get("per_page"));
    getPosts(page, perPage);
  }
};

const loadNextPage = () => {
  if (nextUrl.value) {
    const url = new URL(nextUrl.value);
    const page = Number(url.searchParams.get("page"));
    const perPage = Number(url.searchParams.get("per_page"));
    getPosts(page, perPage);
  }
};

provide('loadPrevPage', loadPrevPage);
provide('loadNextPage', loadNextPage);
provide('currentPage', currentPage);
provide('totalPages', totalPages);
provide('searchQuery', searchQuery);
provide('searchPosts', searchPosts);
provide('findHashtags', findHashtags);

onMounted(() => {
  getPosts();
});
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap");

body {
  font-family: "Roboto", sans-serif;
  font-size: 18px;
}

p {
  font-family: "Open Sans", sans-serif;
}

h1 {
  font-size: 48px;
}

h2 {
  font-size: 36px;
}
</style>
