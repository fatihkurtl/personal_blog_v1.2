import { useStorePinia } from "~/stores/myStore";

export const updatePost = async (formData, id) => {
  const useStore = useStorePinia();
  const route = useRoute();
  const { baseURL } = useUtils();
  try {
    const requestOptions = {
      method: "PUT",
      body: formData,
    };

    const response = await $fetch(`${baseURL()}${route.name == 'auth-snippets-edit-id' ? `/api/update/snippets/${id}` : `/api/update/posts/${id}` }`, requestOptions);

    if (response.info == true) {
      useStore.statusAlarmFunc(true);
      if (route.name == 'auth-snippets-edit-id') {
        localStorage.removeItem('snippets');
      } else {
        localStorage.removeItem('posts');
      }
    } else {
      useStore.statusWarningFunc(false);
    }
  } catch (error) {
    console.log("error :>> ", error);
    useStore.statusWarningFunc(false);
  }
  return { updatePost };
};
