import { useStorePinia } from "~/stores/myStore";

export const useLogin = async (data) => {
  const useStore = useStorePinia();
  const router = useRouter();
  const { baseURL } = useUtils();

  try {
    await $fetch(`${baseURL()}/api/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: data.email,
        password: data.password,
      }),
    }).then((res) => {
      if (res.info == true) {
        setTimeout(() => {
          router.push({ path: "/auth/blog/posts" });
        }, 2000);
        useStore.authUser(res.info);
      }
    });
  } catch (err) {
    err ? useStore.authUser(false) : router.push({ path: "/admin" });
    setTimeout(() => {
      useStore.authUser(null);
    }, 5000);
  }

  return { useLogin };
};
