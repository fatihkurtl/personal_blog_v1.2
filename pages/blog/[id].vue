<template>
  <div class="dark:bg-slate-800 bg-white">
    <section class="container mx-auto px-4 py-6 max-w-5xl">
      <div class="flex flex-wrap -mx-4 mt-4">
        <!-- Blog post details here -->
        <div class="w-full px-4 mb-6" v-for="post in posts" :key="post.id">
          <Hashtags :hashtags="post.hashtags" />
          <Title :title="post.title" />
          <div class="flex items-center justify-between mb-4">
            <div class="text-sm text-gray-600 dark:text-gray-400 flex space-x-4 mt-2">
              <div class="flex items-center justify-center">
                <img src="/blog/date.svg" alt="">
                <Date :date="post.create_at" />
              </div>
              <span class="mx-2 text-gray-600 dark:text-gray-400"> • </span>
              <div class="flex items-center">
                <img src="/blog/reading_time.svg" alt="">
                <ReadingTime :reading_time="post.reading_time" />
              </div>
              <span class="mx-2 text-gray-600 dark:text-gray-400"> • </span>
              <div class="flex items-center">
                <img src="/blog/views.svg" alt="">
                <Views />
              </div>
            </div>
          </div>
          <Content :renderedContent="renderedContent" />
          <ScrollBtn />
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, onUpdated } from "vue";
import MarkdownIt from "markdown-it";
import { useClipboard } from '@vueuse/core';
import Content from "~/components/blog/detail/Content.vue";
import Hashtags from "~/components/blog/detail/header/Hashtags.vue";
import Title from "~/components/blog/detail/header/Title.vue";
import Date from "~/components/blog/detail/header/Date.vue";
import ReadingTime from "~/components/blog/detail/header/ReadingTime.vue";
import Views from "~/components/blog/detail/header/Views.vue";

const { baseURL } = useUtils();

const route = useRoute();

const posts = ref([]);
const renderedContent = ref();

const getPost = async () => {
  try {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await $fetch(`${baseURL()}/api/posts/${route.params.id}`, requestOptions);
    console.log('response :>> ', response);
    const md = new MarkdownIt();

    if (response) {
      const markdownContent = response.content;
      renderedContent.value = md.render(markdownContent);
      posts.value.push(response);

      localStorage.setItem("posts", JSON.stringify(posts.value));
      localStorage.setItem("renderedContent", renderedContent.value);
    } else {
      console.log("Error: Invalid response data");
    }
  } catch (error) {
    console.log("Error: ", error);
  }
};

onMounted(() => {
  const storedPosts = localStorage.getItem("posts");
  const storedRenderedContent = localStorage.getItem("renderedContent");

  if (storedPosts && storedRenderedContent) {
    posts.value = JSON.parse(storedPosts);
    renderedContent.value = storedRenderedContent;
  } else {
    getPost();
  }
});

onBeforeUpdate(() => {
  localStorage.removeItem('posts');
});

onBeforeUnmount(() => {
  localStorage.removeItem("posts");
  localStorage.removeItem("renderedContent");
});

onUpdated(() => {
  var preList = document.getElementsByTagName('pre');
  preList = Array.prototype.slice.call(preList);

  preList.forEach(element => {
    var button = document.createElement('button');
    button.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><path fill="currentColor" d="M20 16V4H8v12h12m2 0a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V4c0-1.11.89-2 2-2h12a2 2 0 0 1 2 2v12m-6 4v2H4a2 2 0 0 1-2-2V7h2v13h12Z"/></svg>';
    button.style.position = 'absolute';
    button.style.top = '5px';
    button.style.right = '5px';
    button.style.padding = '2px 2px';
    button.style.background = '#212121';
    button.style.color = '#fff';
    button.style.border = '2px solid #fff';
    button.style.borderRadius = '4px';
    button.style.fontFamily = 'Arial, sans-serif';
    button.style.fontSize = '14px';
    button.style.cursor = 'pointer';
    element.style.position = 'relative';
    element.style.display = 'flex';
    element.style.paddingBottom = '30px';

    button.style.display = 'none';

    element.addEventListener('mouseenter', () => {
      button.style.display = 'block';
    });

    element.addEventListener('mouseleave', () => {
      button.style.display = 'none';
    });

    element.appendChild(button);

    const { text, copy, copied, isSupported } = useClipboard();

    button.addEventListener('click', () => {
      copy(element.innerText);
      button.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><path fill="currentColor" d="M4 7v14h14v2H4c-1.1 0-2-.9-2-2V7h2m8.8 8.35l-3.3-3.3l1.4-1.4l1.9 1.9l4.3-4.3l1.4 1.4l-5.7 5.7M20 3c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H8c-1.1 0-2-.9-2-2V5c0-1.1.9-2 2-2h3.18C11.6 1.84 12.7 1 14 1c1.3 0 2.4.84 2.82 2H20m-6 0c-.55 0-1 .45-1 1s.45 1 1 1s1-.45 1-1s-.45-1-1-1m-4 4V5H8v12h12V5h-2v2h-8Z"/></svg>';
      button.style.color = '#90EE90';
      button.style.border = '2px solid #90EE90';
      button.classList.add('clicked');
      setTimeout(() => {
        button.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24"><path fill="currentColor" d="M20 16V4H8v12h12m2 0a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V4c0-1.11.89-2 2-2h12a2 2 0 0 1 2 2v12m-6 4v2H4a2 2 0 0 1-2-2V7h2v13h12Z"/></svg>';
        button.style.color = '#fff';
        button.style.border = '2px solid #fff';
        button.classList.remove('clicked');
      }, 2000);
    });

    button.addEventListener('mouseenter', () => {
      if (!button.classList.contains('clicked')) {
        button.style.backgroundColor = '#212121';
        button.style.color = '#fff';
      }
    });

    button.addEventListener('mouseleave', () => {
      if (!button.classList.contains('clicked')) {
        button.style.backgroundColor = '#212121';
        button.style.color = '#fff';
      }
    });
  });
});
</script>