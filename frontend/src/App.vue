<template>
  <div class="h-screen w-screen bg-[#F7F8FA] flex">
    <div class="w-[20%] bg-[#F7F8FA] p-6 flex flex-col h-full">
      <Header />

      <button
        type="button"
        @click="open_url_modal"
        class="w-full flex justify-center items-center rounded-lg mt-6 h-10 bg-[#F7F8FA] text-black border border-dashed hover:bg-[#EEEFF0] border-[#5825FC] px-2.5 py-1.5 text-sm font-semibold shadow-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#5825FC] gap-x-1.5">
        <PlusIcon class="h-5 w-5" aria-hidden="true" />
        Add Knowledge
      </button>
 
      <div class="mt-2 overflow-y-auto max-h-[calc(100vh-200px)] mb-4 pb-4">
        <KnowledgeBase
          v-for="(item, index) in knowledge"
          :key="index"
          :title="item.title"
          :url="item.url"
          @delete-knowledge="deleteKnowledge"
        />
      </div>
   
      <button
        type="button"
        @click="open_settings_modal"
        class="w-full flex justify-center items-center rounded-lg h-10 bg-[#5825FC] mt-auto text-white hover:bg-indigo-700 px-2.5 py-1.5 text-sm font-medium shadow-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-700 gap-x-1.5">
        <Cog6ToothIconOutline class="h-5 w-5" aria-hidden="true" />
        Settings
      </button>
    </div>

    <div class="w-[80%] bg-gradient-to-tl from-[#E9EBF9] to-white flex flex-col mt-4 mr-4 rounded-t-3xl shadow-sm border-2">
      <Intro v-if="is_info_showing"/>

      <div v-if="is_chat_showing" class="overflow-y-auto mt-4">
        <div v-for="(message, index) in chat" :key="index">
          <AIResponsePrompt v-if="message.type === 'ai'" :ai_text="message.message" :time="message.time"/>
          <UserPrompt v-else-if="message.type === 'user'" :user_text="message.message" :time="message.time"/>
        </div>
      </div>

      <URLModal :is-open="isModalOpen" @close-modal="isModalOpen = false" @addKnowledge="onAddingKnowledge" />
      <SettingsModal :is-open="isSettingsModalOpen" @close-modal="isSettingsModalOpen = false" />

      <div class="flex-grow"></div>

      <ChatInput @submit-query="onSubmitQuery" class="mt-4"/>

    </div>
  </div>
</template>


<script>

import Intro from './components/Intro.vue'
import ChatInput from './components/ChatInput.vue'
import Header from './components/Header.vue'
import KnowledgeBase from './components/KnowledgeBase.vue'
import URLModal from './components/URLModal.vue'
import SettingsModal from './components/SettingsModal.vue'
import { PlusIcon } from '@heroicons/vue/20/solid'
import { Cog6ToothIcon as Cog6ToothIconOutline } from '@heroicons/vue/24/outline'
import AIResponsePrompt from './components/AIResponsePrompt.vue'
import UserPrompt from './components/UserPrompt.vue'


export default {

  components: {
    Intro,
    ChatInput,
    Header,
    KnowledgeBase,
    URLModal,
    PlusIcon,
    Cog6ToothIconOutline,
    SettingsModal,
    AIResponsePrompt,
    UserPrompt
  },

  data() {
    return {
      isModalOpen: false,
      isSettingsModalOpen: false,
      is_info_showing: true,
      is_chat_showing: false,
      knowledge: [
        {
          title: 'Ask questions and find insights',
          url: 'https://www.google.com',
        },
        {
          title: 'Learning Vue.js',
          url: 'https://vuejs.org',
        },
        {
          title: 'Vue 3 Documentation',
          url: 'https://v3.vuejs.org',
        },
        {
          title: 'Tailwind CSS Guide',
          url: 'https://tailwindcss.com',
        },
      ],
      chat: [
        {
          type: 'ai',
          message: 'Hello! How can I help you today?',
          time: '2:45pm',
        },
        {
          type: 'user',
          message: 'What is the capital of France?',
          time: '2:46pm',
        },
        {
          type: 'ai',
          message: "The British Museum, one of the world's largest and most comprehensive museums, was established in 1753 with the acquisition of a significant collection of antiquities by Sir Hans Sloane. Initially housed in a private residence in Bloomsbury, London, the museum was opened to the public in 1759. Over the centuries, the museum's collection has grown exponentially, encompassing a vast array of artifacts from around the globe, including ancient Egyptian mummies, Greek sculptures, Roman mosaics, and treasures from the Far East. Today, the British Museum remains a cultural cornerstone, attracting millions of visitors each year and serving as a vital resource for scholars and the public alike.",
          time: '2:46pm',
        }
      ],
    };
  },
  methods: {
    getFormattedTime() {
      const now = new Date();
      let hours = now.getHours();
      let minutes = now.getMinutes();
      const ampm = hours >= 12 ? 'PM' : 'AM';

      hours = hours % 12;
      hours = hours ? hours : 12; 
    
      minutes = minutes < 10 ? '0' + minutes : minutes;

      return hours + ':' + minutes + ' ' + ampm;
  },
    open_url_modal() {
      this.isModalOpen = true;
    },
    open_settings_modal() {
      this.isSettingsModalOpen = true;
    },
    onAddingKnowledge(knowledge) {
      this.knowledge.push(knowledge)
    },
    deleteKnowledge(title) {

      for (let i = 0; i < this.knowledge.length; i++) {
        if (this.knowledge[i].title === title) {
          this.knowledge.splice(i, 1);
          break;
        }
      }
    },
    onSubmitQuery(query) {

      this.is_info_showing = false;
      this.is_chat_showing = true;

      this.chat.push({
        type: 'user',
        message: query,
        time: this.getFormattedTime(),
      });

      this.chat.push({
        type: 'ai',
        message: 'I am sorry, I do not have an answer to that question at the moment.',
        time: this.getFormattedTime(),
      });
    }
  },
};
</script>
