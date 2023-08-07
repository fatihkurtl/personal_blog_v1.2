import { useStorePinia } from "~/stores/myStore";

export const deleteData = async (id) => {
  const useStore = useStorePinia();
  const route = useRoute();
  try {
    const { baseURL } = useUtils();
    const requestOptions = {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await $fetch(
      `${baseURL()}${
        route.name == "auth-snippets-posts"
          ? `/api/delete/snippets/${id}`
          : `/api/delete/posts/${id}`
      }`,
      requestOptions
    );

    if (response.info == true) {
      console.log("response :>> ", response);
      useStore.statusDelete(true);
    } else {
      console.log("error :>> ", response);
    }
  } catch (error) {
    console.log("error :>> ", error);
  }
  return { deleteData };
};
