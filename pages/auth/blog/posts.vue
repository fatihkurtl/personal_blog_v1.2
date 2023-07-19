<template>
  <section class="bg-gray-50 dark:bg-gray-900 p-3 sm:p-5">
    <div class="mx-auto max-w-screen-xl px-4 lg:px-12">
      <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
        <div class="pb-4 bg-white dark:bg-gray-900">
          <label for="table-search" class="sr-only">Search</label>
          <div class="relative mt-1 grid gap-4 sm:grid-cols-2 sm:gap-6">
            <Search />
            <!-- Add Post Button -->
            <RouteOfAdd />
            <!-- Add Post Button -->
          </div>
        </div>
        <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
          <TableHead />
          <Delete v-if="useStore.getStatusDelete" />
          <tbody>
            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
              v-for="post in posts" :key="post.id">
              <td class="w-4 p-4">
                <div class="flex items-center">
                  <input id="checkbox-table-search-1" type="checkbox" :value="post.id" :checked="post.selected"
                    @click="post.selected = !post.selected"
                    class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />
                  <label for="checkbox-table-search-1" class="sr-only">checkbox</label>
                </div>
              </td>
              <TableContent :id="post.id" :title="post.title" :categories="post.categories?.[0]" :date="post.create_at" />
              <td class="px-6 py-4">
                <div class="grid gap-4 sm:grid-cols-2 sm:gap-6">
                  <div class="sm:col-span-1">
                    <EditButton :id="post.id" :title="post.title" />
                    <DeleteButton :id="post.id" />
                  </div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- Pagination -->
      <div class="flex flex-col items-end">
        <!-- Help text -->
        <PaginationInfo :currentPage="currentPage" :totalPages="totalPages" :totalPosts="totalPosts" />
        <PaginationButton />
      </div>
      <!-- Pagination -->
    </div>
    <!-- </div> -->
  </section>
</template>

<script>
import { useStorePinia } from "~/stores/myStore";
import { ref, onMounted, watch } from "vue";
import { deleteData } from "~/composables/delete";
import Delete from "~/components/notification/Delete.vue";
import RouteOfAdd from '~/components/auth/blog/posts/RouteOfAdd.vue';
import Search from '~/components/auth/blog/posts/Search.vue';
import TableHead from '~/components/auth/blog/posts/TableHead.vue';
import TableContent from '~/components/auth/blog/posts/TableContent.vue';
import EditButton from '~/components/auth/blog/posts/EditButton.vue';
import DeleteButton from '~/components/auth/blog/posts/DeleteButton.vue';
import PaginationInfo from '~/components/auth/blog/posts/PaginationInfo.vue';
import PaginationButton from '~/components/auth/blog/posts/PaginationButton.vue';

definePageMeta({
  middleware: "auth",
});

export default (await import("vue")).defineComponent({
  components: {
    Delete,
    RouteOfAdd,
    Search,
    TableHead,
    TableContent,
    EditButton,
    DeleteButton,
    PaginationInfo,
    PaginationButton,
  },
  setup() {
    const { baseURL } = useUtils();
    const useStore = useStorePinia();
    const DEFAULT_PAGE = 1;
    const DEFAULT_PER_PAGE = 7;
    const posts = ref([]);
    const totalPosts = ref(0);
    const totalPages = ref(0);
    const prevUrl = ref(null);
    const nextUrl = ref(null);
    const currentPage = ref(1);

    const searchQuery = ref("");
    const data = ref([]);

    const selectAll = ref(false);

    watch(selectAll, (newValue) => {
      posts.value.forEach((post) => {
        post.selected = newValue;
      });
    });

    posts.value.forEach((post) => {
      post.selected = ref(false);
    });

    watch(posts, () => {
      try {
        const allSelected = posts.value.every((post) => post.selected);
        selectAll.value = allSelected;
      } catch (error) {
        console.log(error);
      }
    });

    const searchPosts = async (e) => {
      try {
        searchQuery.value = e;
        const response = await $fetch(
          `${baseURL()}/api/posts?search=${searchQuery.value}`
        );
        if (response) {
          console.log("response.data :>> ", response[0]);
          posts.value = response;
        } else {
          getPosts();
          searchQuery.value = null;
        }
      } catch (error) {
        console.log("error :>> ", error);
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
        console.log("error :>> ", error);
      }
    });

    async function getPosts(page = DEFAULT_PAGE, perPage = DEFAULT_PER_PAGE) {
      try {
        currentPage.value = page;
        const response = await $fetch(
          `${baseURL()}/api/posts?page=${page}&per_page=${perPage}`
        );
        // const data = await response.json();
        posts.value = response.posts;
        totalPosts.value = response.total;
        totalPages.value = response.pages;
        prevUrl.value = response.prev_url;
        nextUrl.value = response.next_url;
        console.log('posts :>> ', posts);
      } catch (error) {
        console.error("Error fetching posts:", error);
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

    onMounted(() => {
      getPosts();
    });

    const postID = ref(null); //

    const selectedPost = (e) => {
      try {
        console.log("selected post id :>> ", e.target.value);
        postID.value = e.target.value; //
      } catch (error) {
        console.log("error :>> ", error);
      }
    };

    const deletePost = async (id) => {
      console.log("delete post id :>> ", id);
      await deleteData(id);
    };

    provide('searchPosts', searchPosts);
    provide('searchQuery', searchQuery);
    provide('selectAll', selectAll);
    provide('deletePost', deletePost);
    provide('loadPrevPage', loadPrevPage);
    provide('loadNextPage', loadNextPage);

    return {
      posts,
      totalPosts,
      totalPages,
      prevUrl,
      nextUrl,
      useStore,
      postID,
      searchQuery, //
      data, //
      selectAll,
      currentPage,
      searchPosts, //
      loadPrevPage,
      loadNextPage,
      selectedPost,
      deletePost,
    };
  },
});
</script>
