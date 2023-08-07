<template>
  <section class="bg-white dark:bg-gray-900">
    <div class="py-8 px-4 mx-auto max-w-2xl lg:py-16">
      <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">
        Add a new snippet
      </h2>
      <form @submit.prevent="submit">
        <div class="grid gap-4 sm:grid-cols-3 sm:gap-6">
          <div class="sm:col-span-3">
            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Title of
              Snippet</label>
            <input type="text" name="title" id="title"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="Title" required="" v-model="snippetsData.title" />
          </div>
          <div class="sm:col-span-3">
            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Subject of
              Snippet</label>
            <input type="text" name="subject" id="subject"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="Subject" required="" v-model="snippetsData.subject" />
          </div>
          <div class="sm:col-span-3">
            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Photo of
              Snippet</label>
            <input
              class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
              aria-describedby="file_input_help" id="file_input" type="file" name="file" @change="uploadPhoto" />
            <p class="mt-1 text-sm text-gray-500 dark:text-gray-300" id="file_input_help">
              SVG, PNG, JPG or GIF (MAX. 800x400px).
            </p>
          </div>
          <div class="w-full">
            <label for="brand" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Subject
              Hashtags</label>
            <input type="text" name="hashtags" id="hashtags"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="#hashtags" required="" v-model="snippetsData.hashtags" />
          </div>
          <div class="w-full">
            <label for="price" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Reading Time</label>
            <input type="number" name="readin_time" id="reading_time"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="5 mins read" required="" v-model="snippetsData.reading_time" />
          </div>
          <div>
            <label for="category" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Category of
              Snippet</label>
            <input type="text" name="category" id="category"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="category" required="" v-model="snippetsData.category" />
          </div>
          <div class="sm:col-span-3">
            <label for="content" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Content of
              Snippet</label>
            <textarea id="content" rows="24"
              class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="Your content here" v-model="snippetsData.content"></textarea>
          </div>
          <Success v-if="useStore.getStatusAlarm" />
          <Warning v-if="useStore.getStatusWarning" />
        </div>
        <AddSnippetButton />
      </form>
    </div>
  </section>
</template>

<script setup>
import { useStorePinia } from "~/stores/myStore";
import { createPost } from "~/composables/share";
import Success from "~/components/notification/Success.vue";
import Warning from "~/components/notification/Warning.vue";
import AddSnippetButton from "~/components/auth/snippets/share/AddSnippetButton.vue";

definePageMeta({
  middleware: "auth",
});

const useStore = useStorePinia();

const route = useRoute();

console.log(route.name);

const snippetsData = reactive({
  title: null,
  file: null,
  subject: null,
  reading_time: null,
  hashtags: [],
  category: null,
  content: null,
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
  const enteredHashtags = snippetsData.hashtags.split(",");
  snippetsData.hashtags = enteredHashtags;
  try {
    const formData = new FormData();
    formData.append("title", snippetsData.title);
    formData.append("subject", snippetsData.subject);
    formData.append("file", snippetsData.file);
    formData.append("reading_time", snippetsData.reading_time);
    formData.append("hashtags", enteredHashtags);
    formData.append("category", snippetsData.category);
    formData.append("content", snippetsData.content);

    await createPost(formData);
  } catch (error) {
    console.log("error :>> ", error);
  }
};
</script>
