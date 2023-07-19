<template>
  <section class="bg-white dark:bg-gray-900">
    <div class="py-8 px-4 mx-auto max-w-2xl lg:py-16">
      <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">
        Edit post
      </h2>
      <form @submit.prevent="submit" v-for="post in posts" :key="post.id">
        <div class="grid gap-4 sm:grid-cols-3 sm:gap-6">
          <div class="sm:col-span-3">
            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Title of Post</label>
            <input type="text" name="title" id="title"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="Title" required="" :value="post.title" @input="updateTitle($event.target.value)" />
          </div>
          <div class="sm:col-span-3">
            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Subject of
              Snippet</label>
            <input type="text" name="subject" id="subject"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="Subject" required="" :value="post.subject" @input="updateSubject($event.target.value)" />
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
              placeholder="#hashtags" required="" :value="post.hashtags" @input="updateHashtags($event.target.value)" />
          </div>
          <div class="w-full">
            <label for="price" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Reading Time</label>
            <input type="number" name="readin_time" id="reading_time"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="5 mins read" required="" :value="post.reading_time"
              @input="updateReadingTime($event.target.value)" />
          </div>
          <div>
            <label for="category" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Post
              Category</label>
            <input type="category" name="category" id="category"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="Category" required="" :value="post.category" @input="updateCategory($event.target.value)" />
          </div>
          <div class="sm:col-span-3">
            <label for="description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Posts
              Content</label>
            <textarea id="description" rows="24"
              class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
              placeholder="Your description here" :value="post.content"
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
import { ref, onMounted } from "vue";
import { updatePost } from "~/composables/update";
import Success from "~/components/notification/Success.vue";
import Warning from "~/components/notification/Warning.vue";
import UpdateButton from '~/components/auth/blog/edit/UpdateButton.vue';

definePageMeta({
  middleware: "auth",
});

const { baseURL } = useUtils();
const useStore = useStorePinia();
const route = useRoute();

// console.log("route name :>> ", route.name);
// console.log("post name :>> ", route.query.post);
// console.log("post id :>> ", route.params.id);

const postsData = reactive({
  title: null,
  subject: null,
  file: null,
  reading_time: null,
  content: null,
  category: null,
  hashtags: [],
});

const updateTitle = (e) => {
  postsData.title = e;
};

const updateSubject = (e) => {
  postsData.subject = e;
};

const updateHashtags = (e) => {
  postsData.hashtags = e;
};

const updateReadingTime = (e) => {
  postsData.reading_time = e;
};

const updateCategory = (e) => {
  postsData.category = e;
};

const updateContent = (e) => {
  postsData.content = e;
};

const posts = ref([]);

const getPost = async () => {
  try {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        // Authorization: `Token ${useStore.getAuth}`,
      },
    };

    const response = await $fetch(`${baseURL()}/api/posts/${route.params.id}`, requestOptions);

    if (response) {
      console.log("Response:", response);
      posts.value.push(response);

      // localStorage.setItem('posts', JSON.stringify(posts.value));
      // useStore.statusAlarmFunc(true);
      console.log("posts.value :>> ", posts.value);
      // useStore.statusAlarmFunc(true);
    } else {
      console.log("Error:", response);
      // useStore.statusWarningFunc(false);
    }
  } catch (error) {
    console.log("error :>> ", error);
    // useStore.statusWarningFunc(false);
  }
};

onMounted(() => {
  const editedPost = localStorage.getItem('posts');
  if (editedPost) {
    posts.value[0] = null;
    posts.value = JSON.parse(editedPost);
  }
  else {
    getPost();
  }
});

onBeforeUpdate(() => {
  localStorage.removeItem('posts');
});

onBeforeUnmount(() => {
  localStorage.removeItem('posts');
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

const submit = async () => {
  try {
    const formData = new FormData();
    formData.append("title", postsData.title);
    formData.append("subject", postsData.subject);
    formData.append("file", postsData.file);
    formData.append("reading_time", postsData.reading_time);
    formData.append("hashtags", postsData.hashtags);
    formData.append("category", postsData.category);
    formData.append("content", postsData.content);

    await updatePost(formData, route.params.id);
    localStorage.setItem('posts', JSON.stringify(posts.value));
  } catch (error) {
    console.log("error :>> ", error);
  }
};
</script>
