import { defineStore } from "pinia";
import { set } from "vue-demi";

export const useStorePinia = defineStore("myStore", {
  state: () => {
    return {
      auth: {
        admin: null,
      },
      status: {
        alarm: null,
        warning: null,
        delete: null,
      },
    };
  },
  actions: {
    authUser(admin) {
      this.auth.admin = admin;
    },
    statusAlarmFunc(status) {
      this.status.alarm = status;
      console.log('status :>> ', status);
      setTimeout(() => {
        this.status.alarm = null;
        window.location.reload();
      }, 3000);
    },
    statusWarningFunc(status) {
      this.status.warning = status;
      console.log('status :>> ', status);
      setTimeout(() => {
        this.status.warning = null;
      }, 3000);
    },
    statusDelete(status) {
      this.status.delete = status;
      console.log('status :>> ', status);
      setTimeout(() => {
        this.status.delete = null;
        window.location.reload();
      }, 1000);
    },
  },
  getters: {
    getAuth() {
      return this.auth.admin;
    },
    getStatusAlarm() {
      return this.status.alarm;
    },
    getStatusWarning() {
      return this.status.warning;
    },
    getStatusDelete() {
      return this.status.delete;
    },
  },
  // persist: true
  persist: {
    type: 'localstorage', // or 'sessionstorage'
    key: 'myStore',
    expire: 60 * 60 * 1000,
    paths: ['auth.admin']
  }
});