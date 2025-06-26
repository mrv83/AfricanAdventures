<template>
  <div class="new-game">
    <h1>Нова Гра</h1>
    <div>
      <label>Розмір мапи:</label>
      <select v-model="mapSize">
        <option v-for="size in mapSizes" :key="size.type" :value="size.type">{{ size.name }}</option>
      </select>
    </div>

    <div>
      <label>Ім'я персонажа:</label>
      <input type="text" v-model="personName" />
    </div>

    <div>
      <label>Персонаж:</label>
      <select v-model="personType">
        <option v-for="person in personTypes" :key="person.type" :value="person.type">{{ person.name }}</option>
      </select>
      <p>{{ personDescription }}</p>
    </div>

    <div>
      <label>Клас персонажа:</label>
      <select v-model="personClass">
        <option v-for="cls in classes" :key="cls.type" :value="cls.type">{{ cls.name }}</option>
      </select>
      <p>{{ classDescription }}</p>
    </div>

    <div>
      <label>Аватар:</label>
      <div class="avatar-selection">
        <img v-for="avatar in avatars" :key="avatar" :src="avatar" @click="selectAvatar(avatar)" :class="{ selected: avatar === selectedAvatar }" />
      </div>
    </div>

    <button @click="startGame">Почати гру</button>
    <button @click="goBack">Назад</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      mapSize: '',
      personName: '',
      personType: '',
      personClass: '',
      selectedAvatar: '',
      mapSizes: [],
      personTypes: [],
      classes: [],
      avatars: [],
      // personDescription: '',
      // classDescription: ''
    };
  },
  created() {
    axios.get('http://127.0.0.1:8000/get_settings')
      .then(response => {
        this.mapSizes = response.data.map_sizes;
        this.personTypes = response.data.person_types;
        this.classes = response.data.classes;
        this.avatars = response.data.avatars;
        this.mapSize = response.data.default_map_size;
        this.personType = response.data.default_person;
        this.personClass = response.data.default_class;
        this.selectedAvatar = this.avatars[0];
      });
  },
  computed: {
    personDescription() {
      const person = this.personTypes.find(p => p.type === this.personType);
      return person ? person.description : '';
    },
    classDescription() {
      const cls = this.classes.find(c => c.type === this.personClass);
      return cls ? cls.description : '';
    }
  },
  methods: {
    startGame() {
      const gameData = {
        map_size: this.mapSize,
        person_name: this.personName,
        person_type: this.personType,
        person_class: this.personClass,
        avatar: this.selectedAvatar
      };
      localStorage.setItem('game_data', JSON.stringify(gameData));
      localStorage.removeItem('game_id');
      this.$router.push('/game');
    },
    goBack() {
      this.$router.push('');
    },
    selectAvatar(avatar) {
      this.selectedAvatar = avatar;
    }
  }
};
</script>

<style scoped>
.avatar-selection img {
  width: 100px;
  height: 100px;
  margin: 5px;
  cursor: pointer;
  border: 2px solid transparent;
}

.avatar-selection img.selected {
  border-color: blue;
}
</style>

