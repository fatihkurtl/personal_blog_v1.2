import { useStorePinia } from "~/stores/myStore";

export const updatePost = async (formData, id) => {
  const useStore = useStorePinia();
  const route = useRoute();
  const { baseURL } = useUtils();
  try {
    const apiURL = `${baseURL()}/api/update/posts/${id}`;

    const requestOptions = {
      method: "PUT",
      body: formData,
    };

    const response = await $fetch(`${baseURL()}${route.name == 'auth-snippets-edit-id' ? `/api/update/snippets/${id}` : `/api/update/posts/${id}` }`, requestOptions);

    if (response.info == true) {
      console.log("response :>> ", response);
      useStore.statusAlarmFunc(true);
      if (route.name == 'auth-snippets-edit-id') {
        localStorage.removeItem('snippets');
      } else {
        localStorage.removeItem('posts');
      }
    } else {
      console.log("error :>> ", response);
      useStore.statusWarningFunc(false);
    }
  } catch (error) {
    console.log("error :>> ", error);
    useStore.statusWarningFunc(false);
  }
  return { updatePost };
};
