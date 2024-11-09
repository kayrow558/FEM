<template>
    <div class="min-h-screen bg-white p-6 flex flex-col items-center justify-center">
      <h1 class="text-2xl font-semibold mb-4">Qual perfil deseja investigar?</h1>
      <form @submit.prevent="submitForm" class="flex flex-col items-center space-y-4 w-full">
        <input
          v-model="username"
          type="text"
          placeholder="Digite seu nome de usuário"
          class="inputUsername border rounded p-2 mb-6"
          required
        />
        <button
          type="submit"
          class="bg-red-500 hover:bg-red-600 text-white py-6 px-32 rounded-lg font-semibold"
          :disabled="loading"
        >
          <span v-if="loading">Aguarde esse processo demora cerca de 5 minutos...</span>
          <span v-else>Enviar</span>
        </button>
        <!-- Mensagem de erro -->
        <p v-if="errorMessage" class="text-red-500 mt-2">{{ errorMessage }}</p>
      </form>
      <!-- Indicador de carregamento -->
      <div v-if="loading" class="mt-4">
        <svg class="animate-spin h-5 w-5 text-red-500" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path>
        </svg>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  
  const username = ref('');
  const loading = ref(false);
  const errorMessage = ref('');
 
  
  async function submitForm() {
    loading.value = true;
    errorMessage.value = '';
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/download', {
        username: username.value,
      });
      console.log('Resposta do servidor:', response.data);
    } catch (error) {
      errorMessage.value = 'Não foi possível investigar esse perfil, confira se está correto e/ou se não é privado.';
      console.error('Erro ao enviar o formulário:', error);
    } finally {
      loading.value = false;
    }
  }
  </script>
  
  <style scoped>
  /* Adicione estilos específicos aqui, se necessário */
  .animate-spin {
    animation: spin 1s linear infinite;
  }
  
  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

  .inputUsername {
    outline: none;
    border: 2px solid tomato;
    box-shadow: 0px 5px 10px 3px black;
    font-size: 22px;
    font-weight: 600;
  }
  </style>
  