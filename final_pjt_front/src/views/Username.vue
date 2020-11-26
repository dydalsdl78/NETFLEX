<template>
  <div @click="moveMypage">{{ this.username }} 님 반갑습니다!</div>
</template>

<script>
// 이파일 안쓰는듯요
import axios from "axios";

export default {
  name: "Username",
  data: function () {
    return {
      username: "",
    };
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("jwt");
      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },
    getUsername: function () {
      const config = this.setToken();
      axios
        .get("http://127.0.0.1:8000/accounts/username/", config)
        .then((res) => {
          console.log(res.data);
          this.username = res.data.username;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    moveMypage: function () {
      this.$router.push({ name: "Mypage" });
      console.log("??");
    },
  },
  created() {
    this.getUsername();
  },
};
</script>

<style>
</style>