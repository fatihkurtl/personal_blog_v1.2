<template>
  <section class="bg-gray-50 dark:bg-gray-900 p-3 sm:p-5">
    <div class="mx-auto max-w-screen-xl px-4 lg:px-12">
      <!-- Start coding here -->
      <!-- <div class="bg-white dark:bg-gray-800 relative shadow-md sm:rounded-lg overflow-hidden"> -->

      <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
        <div class="pb-4 bg-white dark:bg-gray-900">
          <label for="table-search" class="sr-only">Search</label>
          <div class="relative mt-1 grid gap-4 sm:grid-cols-2 sm:gap-6">
            <Search />
            <!-- Add Snippets Button -->
            <RouteOfAdd />
            <!-- Add Snippets Button -->
          </div>
        </div>
        <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
          <TableHead />
          <Delete v-if="useStore.getStatusDelete" />
          <tbody>
            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
              v-for="snippet in snippets" :key="snippet.id">
              <td class="w-4 p-4">
                <div class="flex items-center">
                  <input id="checkbox-table-search-1" type="checkbox" :value="snippet.id" :checked="snippet.selected"
                    @click="snippet.selected = !snippet.selected"
                    class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />
                  <label for="checkbox-table-search-1" class="sr-only">checkbox</label>
                </div>
              </td>
              <TableContent :id="snippet.id" :title="snippet.title" :categories="snippet.categories?.[0]"
                :date="snippet.create_at" />
              <td class="px-6 py-4">
                <div class="grid gap-4 sm:grid-cols-2 sm:gap-6">
                  <div class="sm:col-span-1">
                    <EditButton :id="snippet.id" :title="snippet.title" />
                    <DeleteButton :id="snippet.id" />
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
        <PaginationInfo :currentPage="currentPage" :totalPages="totalPages" :totalSnippets="totalSnippets" />
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
import Search from "~/components/auth/snippets/posts/Search.vue";
import RouteOfAdd from "~/components/auth/snippets/posts/RouteOfAdd.vue";
import TableHead from "~/components/auth/snippets/posts/TableHead.vue";
import TableContent from "~/components/auth/snippets/posts/TableContent.vue";
import EditButton from "~/components/auth/snippets/posts/EditButton.vue";
import DeleteButton from "~/components/auth/snippets/posts/DeleteButton.vue";
import PaginationInfo from "~/components/auth/snippets/posts/PaginationInfo.vue";
import PaginationButton from "~/components/auth/snippets/posts/PaginationButton.vue";

definePageMeta({
  middleware: "auth",
});

export default (await import("vue")).defineComponent({
  components: {
    Delete,
    Search,
    RouteOfAdd,
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
    const snippets = ref([]);
    const totalSnippets = ref(0);
    const totalPages = ref(0);
    const prevUrl = ref(null);
    const nextUrl = ref(null);
    const currentPage = ref(1);

    const searchQuery = ref("");
    const data = ref([]);

    const selectAll = ref(false);

    const route = useRoute();

    watch(selectAll, (newValue) => {
      snippets.value.forEach((snippet) => {
        snippet.selected = newValue;
      });
    });

    snippets.value.forEach((snippet) => {
      snippet.selected = ref(false);
    });

    watch(snippets, () => {
      try {
        const allSelected = snippets.value.every((snippet) => snippet.selected);
        selectAll.value = allSelected;
      } catch (error) {
        console.log(error);
      }
    });

    const searchSnippets = async (e) => {
      try {
        searchQuery.value = e;
        const response = await $fetch(
          `${baseURL()}/api/snippets?search=${searchQuery.value}`
        );
        if (response) {
          console.log("response.data :>> ", response[0]);
          snippets.value = response;
        } else {
          getSnippets();
          searchQuery.value = null;
        }
      } catch (error) {
        console.log("error :>> ", error);
      }
    };

    watch(searchQuery, (newValue, oldValue) => {
      try {
        if (newValue === "") {
          getSnippets();
        } else {
          searchSnippets(newValue);
        }
      } catch (error) {
        console.log("error :>> ", error);
      }
    });

    async function getSnippets(
      page = DEFAULT_PAGE,
      perPage = DEFAULT_PER_PAGE
    ) {
      try {
        currentPage.value = page;
        const response = await $fetch(
          `${baseURL()}/api/snippets?page=${page}&per_page=${perPage}`
        );
        // const data = await response.json();
        snippets.value = response.snippets;
        totalSnippets.value = response.total;
        totalPages.value = response.pages;
        prevUrl.value = response.prev_url;
        nextUrl.value = response.next_url;
      } catch (error) {
        console.log("error :>> ", error);
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

    const snippetID = ref(null);

    const selectedSnippet = (e) => {
      try {
        console.log("e.target.value :>> ", e.target.value);
        snippetID.value = e.target.value;
      } catch (error) {
        console.log("error :>> ", error);
      }
    };

    // const route = "api/delete/snippets";

    const deleteSnippet = async (id) => {
      console.log("delete snippet id :>> ", id);
      await deleteData(id);
    };

    provide('searchSnippets', searchSnippets);
    provide('searchQuery', searchQuery);
    provide('selectAll', selectAll);
    provide('deleteSnippet', deleteSnippet);
    provide('loadPrevPage', loadPrevPage);
    provide('loadNextPage', loadNextPage);

    return {
      snippets,
      totalSnippets,
      totalPages,
      prevUrl,
      nextUrl,
      useStore,
      snippetID,
      route,
      searchQuery,
      data,
      selectAll,
      currentPage,
      searchSnippets,
      loadPrevPage,
      loadNextPage,
      selectedSnippet,
      deleteSnippet,
    };
  },
});
</script>
