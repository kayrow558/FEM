<template>
  <div class="min-h-screen bg-white p-6 flex flex-col items-center justify-center">
    <div class="w-full max-w-lg mx-auto h-2 bg-white relative border border-gray-300 rounded">
        <div
          class="h-full bg-red-500 transition-all duration-300"
          :style="{ width: `${progressWidth}%` }"
        ></div>
      </div>
    <div v-if="progressBarStage==1" class="w-full max-w-2xl space-y-10 relative">
      <div class="text-center space-y-4">
        <div class="relative w-32 h-32 mx-auto">
          <div class="absolute inset-0 rounded-full">
            <img src="../assets/img/firstImage.png" class="">
          </div>
        </div>
        <h1 class="text-2xl font-semibold">
          Descubra em 1 minuto
          <br />
          quem ainda te ama e quem
          <br />
          te odeia
        </h1>
      </div>

      <div class="flex flex-col items-center">
        <span class="bg-[#9cc3f7] text-blue-800 px-4 py-1 rounded-full text-sm">
          Resultado imediato
        </span>
      </div>
      <button
      class="w-1/2 ml-40 bg-red-500 hover:bg-red-600 text-white py-4 rounded-lg text-lg font-semibold"
      @click="skipStageProgressBar"
      >
        Continuar
      </button>
    </div>

    <!-- PARTE 2 -->

    <div v-if="progressBarStage == 2" class="secondPart flex flex-col items-center">
      <div class="rounded-full text-center w-1/2 mt-8">
          <img src="../assets/img/firstImage.png" class="">
      </div>
      <h1 class="text-2xl font-semibold my-6">Qual perfil deseja investigar?</h1>
      <form @submit.prevent="submitForm" class="flex flex-col items-center space-y-4 w-full">
        <input
          v-model="username"
          :disabled="loading"
          type="text"
          placeholder="Digite seu nome de usuário"
          class="inputUsername border rounde px-8 text-left py-2 mb-6"
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

    <!-- PARTE 3 -->
     <div v-if="progressBarStage == 3" class="thirdPart w-full">
          <div class="profileImageAndInfo w-5/6 flex flex-col items-center ml-40 mt-6">
            <h1>Investigação Completa</h1>
            <img class="rounded-full w-52 h-52 mt-4">
            <p> {{ username }} </p>
            <h2 class="mt-4 font-medium text-lg"> Veja quem fala de você </h2>
            <span class="bg-[#ff8585] text-[#db3c3c] font-sans font-medium px-5 py-3 rounded-full mt-4">Essa prévia está disponível por tempo limitado.</span>
          </div>

          <!-- PARTE DOS PRINTS -->

          <Prints />

          <!-- PARTE DO BOTÃO RELATORIO COMPLETO -->
          <div class="btnRelatorio flex justify-center text-white">
            <button class="btnRelatorioCompleto flex items-center bg-red-400 py-6 px-20 rounded-3xl ml-20">
              <Icon icon="mdi:eye" class="mr-4" />
              Ver relatório completo
            </button>
          </div>
     </div>

  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { Icon } from '@iconify/vue';
import Prints from '../components/Prints.vue';




const progressWidth = ref(33.5);
const progressBarStage = ref(1)

// Função para incrementar o valor do progresso
function skipStageProgressBar() {
  if (progressWidth.value < 100) {
    progressWidth.value += 33.5;
  }
  if (progressWidth.value == 67) {
    progressBarStage.value = 2; // Ajustado para usar .value
  }
  if (progressWidth.value >= 100) {
    progressBarStage.value = 3; // Ajustado para usar .value
  }
}



const username = ref('');
const loading = ref(false);
const errorMessage = ref('');
const followers = ref([])
 
  
async function submitForm() {
  loading.value = true;
  errorMessage.value = '';
  try {
    const response = await axios.post('http://127.0.0.1:5000/api/download', {
      username: username.value,
    });
    console.log('Resposta do servidor:', response.data);
    followers.value = response.data.followers; // Armazena os seguidores na lista
    progressBarStage.value = 3; // Alterado para mudar a etapa após a resposta
  } catch (error) {
    errorMessage.value = 'Não foi possível investigar esse perfil, confira se está correto e/ou se não é privado.';
    console.error('Erro ao enviar o formulário:', error);
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped>
.cardItem {
  border: 1px solid #ccc;
}

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
    box-shadow: 0px 0px 20px 1px black;
    font-size: 18px;
    font-weight: 600;
  }

  .btnRelatorioCompleto {
    transition: .3s;
  }

  .btnRelatorioCompleto:hover {
    background-color: #c24747;
  }
</style>
