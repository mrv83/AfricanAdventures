<template>
  <div class="main">
    <div class="center">
      <button @click="goTo('/new')">Почати нову гру</button>
      <button @click="goTo('/load')">Завантажити гру</button>
      <button @click="goTo('/records')">Рекорди</button>
      <button @click="goTo('/donuts')">Донат</button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goTo(path) {
      this.$router.push(path);
    }
  }
}
</script>

<style>
.main {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}
.center {
  text-align: center;
}
button {
  margin: 10px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>
