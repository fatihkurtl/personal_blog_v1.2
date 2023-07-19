<template>
  <section class="bg-white dark:bg-gray-900">
    <div class="py-8 px-4 mx-auto max-w-2xl lg:py-16">
      <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">
        Edit snippet
      </h2>
      <form @submit.prevent="submit" v-for="snippet in snippets" :key="snippet.id">
        <div class="grid gap-4 sm:grid-cols-3 sm:gap-6">
          <div class="sm:col-span-3">
            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Title of Snippet</label>
            <input type="text" name="title" id="title"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="Title" required="" :value="snippet.title" @input="updateTitle($event.target.value)" />
          </div>
          <div class="sm:col-span-3">
            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Subject of
              Snippet</label>
            <input type="text" name="subject" id="subject"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="Subject" required="" :value="snippet.subject" @input="updateSubject($event.target.value)" />
          </div>
          <div class="sm:col-span-3">
            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Snippets Photo</label>
            <input
              class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
              aria-describedby="file_input_help" id="file_input" type="file" @change="uploadPhoto"
              :value="snippet.file" />
            <p class="mt-1 text-sm text-gray-500 dark:text-gray-300" id="file_input_help">
              SVG, PNG, JPG or GIF (MAX. 800x400px).
            </p>
          </div>
          <div class="w-full">
            <label for="brand" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Snippets
              Hashtags</label>
            <input type="text" name="hashtags" id="hashtags"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="#hashtags" required="" :value="snippet.hashtags"
              @input="updateHashtags($event.target.value)" />
          </div>
          <div class="w-full">
            <label for="price" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Reading Time</label>
            <input type="number" name="readin_time" id="reading_time"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="5 mins read" required="" :value="snippet.reading_time"
              @input="updateReadingTime($event.target.value)" />
          </div>
          <div>
            <label for="category" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Snippet
              Category</label>
            <input type="category" name="category" id="category"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="Category" required="" :value="snippet.category" @input="updateCategory($event.target.value)" />
          </div>
          <div class="sm:col-span-3">
            <label for="description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Snippet
              Content</label>
            <textarea id="description" rows="24"
              class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="Your description here" :value="snippet.content"
              @input="updateContent($event.target.value)"></textarea>
          </div>
        </div>
        <Success v-if="useStore.getStatusAlarm" />
        <Warning v-if="useStore.getStatusWarning" />
        <UpdateButton />
      </form>
    </div>
  </section>
</template>

<script setup>
import { useStorePinia } from "~/stores/myStore";
import { ref, reactive, onMounted } from "vue";
import { updatePost } from "~/composables/update";
import Success from "~/components/notification/Success.vue";
import Warning from "~/components/notification/Warning.vue";
import UpdateButton from "~/components/auth/snippets/edit/UpdateButton.vue";

definePageMeta({
  middleware: "auth",
});

const { baseURL } = useUtils();
const useStore = useStorePinia();
const route = useRoute();

console.log('route.name :>> ', route.name);


// console.log("route name :>> ", route.name);
// console.log("post name :>> ", route.query.snippet);
// console.log('post id :>> ', route.params.id);

const snippetsData = reactive({
  title: null,
  subject: null,
  file: null,
  reading_time: null,
  content: null,
  category: null,
  hashtags: [],
});

const updateTitle = (e) => {
  snippetsData.title = e;
};

const updateSubject = (e) => {
  snippetsData.subject = e;
};

const updateHashtags = (e) => {
  snippetsData.hashtags = e;
};

const updateReadingTime = (e) => {
  snippetsData.reading_time = e;
};

const updateCategory = (e) => {
  snippetsData.category = e;
};

const updateContent = (e) => {
  snippetsData.content = e;
};
const snippets = ref([]);

const getSnippet = async () => {
  const apiURL = `${baseURL()}/api/snippets/${route.params.id}`;
  try {
    const requestOptions = {
      method: "GET",
      headers: {
        // "Content-Type": "application/json",
        // Authorization: `Token ${useStore.getAuth}`,
      },
    };

    const response = await $fetch(apiURL, requestOptions);

    if (response) {
      console.log("Response :>> ", response);
      snippets.value.push(response);
      console.log("snippets.value :>> ", snippets.value);
    } else {
      console.log("Error :>> ", response);
    }
  } catch (error) {
    console.log("error :>> ", error);
  }
};

onMounted(() => {
  const editedSnippet = localStorage.getItem('snippets');
  if (editedSnippet) {
    snippets.value[0] = null;
    snippets.value = JSON.parse(editedSnippet);
  } else {
    getSnippet();
  }
});

onBeforeUpdate(() => {
  localStorage.removeItem('snippets');
});

onBeforeUnmount(() => {
  localStorage.removeItem('snippets');
});

const maxFileSize = 3;

const uploadPhoto = (e) => {
  const files = e.target.files;
  let errors = [],
    allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;

  if (!files.length) return false;
  if (!allowedExtensions.exec(e.target.value)) {
    errors.push("Please upload file having extensions .jpeg/.jpg/.png only.");
    if (files[0].size / (1024 * 1024) > maxFileSize)
      errors.push("File size is too large (max 3 MB)");
    if (errors.length) {
      alert(errors.join("\n"));
      return (e.target.value = null);
    }
  }
  console.log("files :>> ", files[0]);
  snippetsData.file = files[0];
};


const submit = async () => {
  try {
    const formData = new FormData();
    formData.append("title", snippetsData.title);
    formData.append("subject", snippetsData.subject);
    formData.append("file", snippetsData.file);
    formData.append("reading_time", snippetsData.reading_time);
    formData.append("category", snippetsData.category);
    formData.append("hashtags", snippetsData.hashtags);
    formData.append("content", snippetsData.content);

    await updatePost(formData, route.params.id);
    localStorage.setItem('snippets', JSON.stringify(snippets.value));
  } catch (error) {
    console.log("error :>> ", error);
    // useStore.statusWarningFunc(false);
  }
};
</script>
