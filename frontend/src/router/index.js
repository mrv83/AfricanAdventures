import { createRouter, createWebHashHistory } from 'vue-router'
import Main from '../views/MainView.vue';
import NewGame from '../views/NewGameView.vue';
import LoadGame from '../views/LoadGameView.vue';
import Records from '../views/RecordsView.vue';
import Donuts from '../views/DonutsView.vue';
import Game from '../views/GameView.vue';

const routes = [
  { path: '/', component: Main },
  { path: '/new', component: NewGame },
  { path: '/load', component: LoadGame },
  { path: '/records', component: Records },
  { path: '/donuts', component: Donuts },
  { path: '/game', component: Game },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
