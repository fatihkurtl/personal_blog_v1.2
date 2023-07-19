import { useStorePinia } from "~/stores/myStore";

export default defineNuxtRouteMiddleware((to, from) => {
  const useStore = useStorePinia();
  if (
    !useStore.getAuth &&
    to.fullPath.includes("auth") &&
    to.fullPath !== "/auth/login"
  ) {
    return navigateTo("/auth/login");
  }
  if (useStore.getAuth && !to.fullPath.includes("auth")) {
    return navigateTo("/auth/blog/posts");
  }
  return;
});
