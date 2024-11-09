<template>
  <div class="Prints flex justify-center ml-20">
    <div class="flex flex-col w-1/3 my-16 bg-black text-white font-sans rounded-3xl">
      <header class="flex items-center justify-between px-4 py-2 bg-black rounded-full">
        <div class="flex items-center space-x-3">
          <Icon icon="rivet-icons:arrow-left" class="w-6 h-6" @click="goBack" />
          <img
            :src="profileImageSrc"
            alt="Profile Picture"
            class="w-10 h-10 rounded-full bg-white"
            @error="handleImageError"
          />
          <span class="font-semibold">{{ randomFollower?.name || 'Usuário' }}</span>
        </div>
        <div class="flex space-x-4">
          <Icon icon="ic:baseline-phone" class="text-white"/>
          <Icon icon="wpf:videocall" class="text-white"/>
        </div>
      </header>
      <main class="flex-1 overflow-y-auto p-4 space-y-2">
        <div class="flex flex-col-reverse">
          <img
            class="w-6 h-6 rounded-full bg-white"
            :src="profileImageSrc"
            alt="Profile Picture"
            @error="handleImageError"
          />
          <div class="max-w-[70%] ml-8 bg-[#262626] rounded-lg px-3 py-2 text-sm">
            <p>kkkkkkkkkk tu não sabe</p>
            <p>{{ username }} me disse, não fala que eu te contei</p>
            <div class="finallyMsg flex">
              <p>teve um dia que <br><span class="blur-sm">######################</span></br></p>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const username = ref('');
const randomFollower = ref({ username: '', name: '' });
const profileImageSrc = ref('');

// Função para lidar com erro de imagem
const handleImageError = (event) => {
  event.target.src = 'path/to/fallback-image.jpg';
};

// Função para retornar à página anterior
const goBack = () => {
  console.log('Retornar à página anterior');
};

// Função para buscar um seguidor aleatório
async function fetchRandomFollower() {
  try {
    const response = await axios.get(`http://127.0.0.1:5000/api/random_follower/${username.value}`);
    randomFollower.value = response.data;
    profileImageSrc.value = response.data.image_url;
  } catch (error) {
    console.error('Erro ao obter seguidor aleatório:', error);
  }
}

onMounted(() => {
  fetchRandomFollower();
});
</script>

<style scoped>
/* Custom scrollbar styles */
main::-webkit-scrollbar {
  width: 6px;
}

main::-webkit-scrollbar-track {
  background: #1f2937;
}

main::-webkit-scrollbar-thumb {
  background-color: #4b5563;
  border-radius: 20px;
}
</style>
