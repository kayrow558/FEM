import { createRouter, createWebHistory } from 'vue-router';
import Visualizar from '../pages/Visualizar.vue';
import Download from '../pages/Download.vue'; // A nova página que você vai criar

const routes = [
  {
    path: '/',
    name: 'Visualizar',
    component: Visualizar,
  },
  {
    path: '/download',
    name: 'Download',
    component: Download, // Referência à nova página
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
