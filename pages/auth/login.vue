<template>
  <section class="bg-gray-50 dark:bg-gray-900">
    <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <a href="#" class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
        <img class="w-8 h-8 mr-2 rounded-full"
          src="https://media.licdn.com/dms/image/C4D03AQGVVurtosXcNA/profile-displayphoto-shrink_800_800/0/1655636563242?e=1689206400&v=beta&t=kxsTWsfVwxB0HjyGpEjCZAZ4C3AIxH217qL0DxYv6wg"
          alt="logo" />
        Admin Panel
      </a>
      <div
        class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <Header />
          <form class="space-y-4 md:space-y-6" @submit.prevent="onSubmit">
            <div>
              <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>
              <input type="email" name="email" id="email"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="name@gmail.com" required="" v-model="loginData.email" />
            </div>
            <div>
              <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
              <input type="password" name="password" id="password" placeholder="••••••••"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                required="" v-model="loginData.password" />
            </div>
            <div class="flex items-center justify-between">
              <div class="flex items-start"></div>
            </div>
            <Button />
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useLogin } from "~/composables/login";
import Header from '../../components/auth/login/Header.vue';
import Button from '../../components/auth/login/Button.vue';

definePageMeta({
  middleware: "auth",
});

const loginData = reactive({
  email: "",
  password: "",
});

const onSubmit = async () => {
  await useLogin(loginData);
};
</script>
