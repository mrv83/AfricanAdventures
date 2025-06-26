<template>
  <div class="load-game">
    <h1>Завантажити гру</h1>
    <ul>
      <li v-for="game in savedGames" :key="game.id" @click="loadGame(game.id)">
        {{ game.name }}
      </li>
    </ul>
    <button @click="goBack">Назад</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      savedGames: []
    };
  },
  created() {
    axios.get('http://127.0.0.1:8000/get_saved_games')
      .then(response => {
        this.savedGames = response.data.saved_games;
      });
  },
  methods: {
    loadGame(gameId) {
      localStorage.setItem('game_id', gameId);
      this.$router.push('/game');
    },
    goBack() {
      this.$router.push('');
    }
  }
};
</script>
