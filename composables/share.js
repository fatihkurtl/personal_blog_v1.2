import { useStorePinia } from "~/stores/myStore";

export const createPost = async (formData) => {
  const useStore = useStorePinia();
  const route = useRoute();
  try {
    const { baseURL } = useUtils();
    const requestOptions = {
      method: "POST",
      body: formData,
    };

    const response = await $fetch(
      `${baseURL()}${
        route.name == "auth-snippets-share"
          ? "/api/create/snippets"
          : "/api/create/posts"
      }`,
      requestOptions
    );

    if (response.info == true) {
      console.log("Response:", response);
      useStore.statusAlarmFunc(true);
    } else {
      console.log("Error:", response);
      useStore.statusWarningFunc(false);
    }
  } catch (error) {
    console.log("Error:", error);
    useStore.statusWarningFunc(false);
  }
  return { createPost };
};
