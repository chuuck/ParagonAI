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

      <button
        type="button"
        @click="select_knowledge"
        class="w-full flex justify-center items-center rounded-lg mt-6 h-10 bg-[#5825FC] text-white border hover:bg-indigo-700 px-2.5 py-1.5 text-sm font-semibold shadow-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#5825FC] gap-x-1.5">
        {{ select_button_text}}
      </button>

 
      <div class="mt-2 overflow-y-auto max-h-[calc(100vh-200px)] mb-4 pb-4">
        <KnowledgeBase
          v-for="(item, index) in knowledge"
          :key="index"
          :title="item.title"
          :url="item.url"
          :state="item.is_checked"
          :select_mode="select_mode"
          @delete-knowledge="deleteKnowledge"
          @ticked="onKnowledgeTicked"
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
import axios from 'axios';


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
      select_mode: false,
      select_button_text: "Select Knowledge",
      knowledge: [
        // {
        //   title: 'Ask questions and find insights',
        //   url: 'https://www.google.com',
        //   is_checked: false,
        // },
        // {
        //   title: 'Learning Vue.js',
        //   url: 'https://vuejs.org',
        //   is_checked: false,
        // },
        // {
        //   title: 'Vue 3 Documentation',
        //   url: 'https://v3.vuejs.org',
        //   is_checked: true,
        // },
        // {
        //   title: 'Tailwind CSS Guide',
        //   url: 'https://tailwindcss.com',
        //   is_checked: false,
        // },
      ],
      chat: [
      ],
    };
  },
  created() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/get_knowledge_list",
        headers: { "Content-Type": "application/json" },
      }).then((response) => {
        var urls = response.data.urls;

        for (let i = 0; i < urls.length; i++) {
          this.knowledge.push({
            title: urls[i],
            url: urls[i],
            is_checked: false,
          });
        }
        
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    select_knowledge(){
      this.select_mode = !this.select_mode;

      if (this.select_mode) {
        this.select_button_text = "Select All";
      }else{
        this.select_button_text = "Select Knowledge";
      }
    },
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

      var bodyFormData = new FormData();
      bodyFormData.append('url', knowledge.url);

      axios({
        method: "post",
        url: "http://127.0.0.1:8000/add_knowledge",
        data: bodyFormData,
        headers: { "Content-Type": "application/json" },
      }).then((response) => {
        console.log(response);
      }).catch(function (response) {
        console.log(response);
      });

      console.log(knowledge)
      this.knowledge.push(knowledge)
      
    },
    deleteKnowledge(title) {

      for (let i = 0; i < this.knowledge.length; i++) {
        if (this.knowledge[i].title === title) {

          var bodyFormData = new FormData();
          bodyFormData.append('url', this.knowledge[i].url);

          axios({
            method: "post",
            url: "http://127.0.0.1:8000/remove_knowledge",
            data: bodyFormData,
            headers: { "Content-Type": "application/json" },
          }).then((response) => {
            this.knowledge.push(knowledge)
          }).catch(function (response) {
            console.log(response);
          });

          this.knowledge.splice(i, 1);
          break;
        }
      }
    },
    onSubmitQuery(query) {

      this.is_info_showing = false;
      this.is_chat_showing = true;

      if (this.select_mode) {
        var checked_urls = this.knowledge.filter((item) => item.is_checked).map((item) => item.url);

      }else{
        var checked_urls = this.knowledge.map((item) => item.url);
        console.log("Checked URLs")
        console.log(checked_urls)
      }

      var bodyFormData = new FormData();
      bodyFormData.append('query', query);
      bodyFormData.append('url', checked_urls);

      this.chat.push({
        type: 'user',
        message: query,
        time: this.getFormattedTime(),
      });

      axios({
        method: "post",
        url: "http://127.0.0.1:8000/rag_query",
        data: bodyFormData,
        headers: { "Content-Type": "application/json" },
        }).then((response) => {

          this.chat.push({
            type: 'ai',
            message: response.data.result,
            time: this.getFormattedTime(),
          });

          console.log(response)
        }).catch(function (response) {
          console.log(response);
      });

    },
    onKnowledgeTicked(isChecked, url) {

      for (let i = 0; i < this.knowledge.length; i++) {
        if (this.knowledge[i].url === url) {
          this.knowledge[i].is_checked = isChecked;
          break;
        }
      }
    },
  },
};
</script>
