<template>
  <section class="bg-white dark:bg-gray-900">
    <div class="py-8 px-4 mx-auto max-w-2xl lg:py-16">
      <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">
        Add a new post
      </h2>
      <form @submit.prevent="onSubmit">
        <div class="grid gap-4 sm:grid-cols-3 sm:gap-6">
          <div class="sm:col-span-3">
            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Title of Post</label>
            <input type="text" name="title" id="title"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="Title" required="" v-model="postsData.title" />
          </div>
          <div class="sm:col-span-3">
            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Subject of Post</label>
            <input type="text" name="subject" id="subject"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="Subject" required="" v-model="postsData.subject" />
          </div>
          <div class="sm:col-span-3">
            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Photo of Post</label>
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
              placeholder="#hashtags" required="" v-model="postsData.hashtags" />
          </div>
          <div class="w-full">
            <label for="price" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Reading Time</label>
            <input type="number" name="readin_time" id="reading_time"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="5 mins read" required="" v-model="postsData.reading_time" />
          </div>
          <div>
            <label for="category" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Category of
              Post</label>
            <input type="text" name="category" id="category"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="category" required="" v-model="postsData.category" />
          </div>
          <div class="sm:col-span-3">
            <label for="content" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Content of
              Post</label>
            <textarea id="content" rows="24"
              class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="Your content here" v-model="postsData.content"></textarea>
          </div>
        </div>
        <Success v-if="useStore.getStatusAlarm" />
        <Warning v-if="useStore.getStatusWarning" />
        <AddPostButton />
      </form>
    </div>
  </section>
</template>

<script setup>
import { useStorePinia } from "~/stores/myStore";
import { createPost } from "~/composables/share";
import Success from "~/components/notification/Success.vue";
import Warning from "~/components/notification/Warning.vue";
import AddPostButton from "~/components/auth/blog/share/AddPostButton.vue";

definePageMeta({
  middleware: "auth",
});

const useStore = useStorePinia();

const route = useRoute();

const postsData = reactive({
  title: null,
  subject: null,
  file: null,
  hashtags: [],
  reading_time: null,
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
  postsData.file = files[0];
};

const onSubmit = async () => {
  const enteredHashtags = postsData.hashtags.split(",");
  postsData.hashtags = enteredHashtags;
  try {
    const formData = new FormData();
    formData.append("title", postsData.title);
    formData.append("subject", postsData.subject);
    formData.append("file", postsData.file);
    formData.append("reading_time", postsData.reading_time);
    formData.append("hashtags", enteredHashtags);
    formData.append("category", postsData.category);
    formData.append("content", postsData.content);

    await createPost(formData);
  } catch (error) {
    console.log("error :>> ", error);
  }
};
</script>
