<template>
  <div class="h-screen w-screen bg-[#F7F8FA] flex">
    <div class="w-[20%] bg-[#F7F8FA] p-6 flex flex-col h-full">
      <Header />

      <button
        type="button"
        @click="open_url_modal"
        class="w-full flex justify-center items-center rounded-lg mt-6 h-10 bg-[#F7F8FA] text-black border border-dashed hover:bg-[#EEEFF0] border-[#5825FC] px-2.5 py-1.5 text-sm font-semibold shadow-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#5825FC] gap-x-1.5"
      >
        <PlusIcon class="h-5 w-5" aria-hidden="true" />
        Add Knowledge
      </button>

      <button
        type="button"
        @click="select_knowledge"
        class="w-full flex justify-center items-center rounded-lg mt-6 h-10 bg-[#5825FC] text-white border hover:bg-indigo-700 px-2.5 py-1.5 text-sm font-semibold shadow-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#5825FC] gap-x-1.5"
      >
        {{ select_button_text }}
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
        class="w-full flex justify-center items-center rounded-lg h-10 bg-[#5825FC] mt-auto text-white hover:bg-indigo-700 px-2.5 py-1.5 text-sm font-medium shadow-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-700 gap-x-1.5"
      >
        <Cog6ToothIconOutline class="h-5 w-5" aria-hidden="true" />
        Settings
      </button>
    </div>

    <div class="w-[80%] bg-gradient-to-tl from-[#E9EBF9] to-white flex flex-col mt-4 mr-4 rounded-t-3xl shadow-sm border-2">
      <Intro v-if="is_info_showing" />

      <div v-if="is_chat_showing" class="overflow-y-auto mt-4">
        <div v-for="(message, index) in chat" :key="index">
          <AIResponsePrompt v-if="message.type === 'ai'" :ai_text="message.message" :time="message.time" :source="message.source" />
          <UserPrompt v-else-if="message.type === 'user'" :user_text="message.message" :time="message.time" />
        </div>
      </div>

      <URLModal :is-open="isModalOpen" @close-modal="isModalOpen = false" @addKnowledge="onAddingKnowledge" />
      <SettingsModal :is-open="isSettingsModalOpen" @close-modal="isSettingsModalOpen = false" />

      <div class="flex-grow"></div>

      <ChatInput @submit-query="onSubmitQuery" class="mt-4" />
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
      knowledge: [],
      chat: [],
    };
  },
  created() {
    // Get the knowledge list from the backend
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/get_knowledge_list",
      headers: { "Content-Type": "application/json" },
    }).then((response) => {
      var kb_list = response.data.knowledge_list;

      console.log(response)
      for (let i = 0; i < kb_list.length; i++) {
    
        this.knowledge.push({
          title: kb_list[i].title,
          url: kb_list[i].source,
          is_checked: false,
        });
      }
    }).catch((error) => {
      console.log(error);
    });
  },
  methods: {

    // Formats model response into text and sources
    extractSource(text) {

      let result = {
        textContent: "",
        source: []
      };

      const sourceMatch = text.match(/Source:\s*\{([^}]+)\}/);
      
      if (sourceMatch) {
        result.source = sourceMatch[1].split(',').map(url => url.trim());
        result.textContent = text.replace(sourceMatch[0], '').trim();
      } else {
        result.textContent = text;
      }

      return result;
    },

    // Function that activates the select mode or select all mode
    select_knowledge(){
      this.select_mode = !this.select_mode;

      if (this.select_mode) {
        this.select_button_text = "Select All";
      }else{
        this.select_button_text = "Select Knowledge";
      }
    },

    // Get formatted current time
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

    // Open URL modal
    open_url_modal() {
      this.isModalOpen = true;
    },

    // Open settings modal where API key can be added
    open_settings_modal() {
      this.isSettingsModalOpen = true;
    },

    // Add knowledge to the knowledge base
    onAddingKnowledge(knowledge) {

      axios({
        method: "post",
        url: "http://127.0.0.1:8000/add_knowledge",
        data: [knowledge],
        headers: { "Content-Type": "application/json" },
      }).then((response) => {
        console.log(response);
      }).catch(function (response) {
        console.log(response);
      });

      knowledge.is_checked = false;
      this.knowledge.push(knowledge)
      
    },

    // Delete knowledge from the knowledge base
    deleteKnowledge(title) {
      for (let i = 0; i < this.knowledge.length; i++) {
        if (this.knowledge[i].title === title) {
          var payload = {
            urls: [this.knowledge[i].url],
          }
          
          console.log(payload)
          axios({
            method: "post",
            url: "http://127.0.0.1:8000/remove_knowledge",
            data: payload,
            headers: { "Content-Type": "application/json" },
          }).then((response) => {
            console.log(response);
          }).catch(function (response) {
            console.log(response);
          });

          this.knowledge.splice(i, 1);
          break;
        }
      }
    },

    // Submit query to the RAG model
    onSubmitQuery(query) {

      this.is_info_showing = false;
      this.is_chat_showing = true;

      // Get the checked URLs or selects all of them
      if (this.select_mode) {
        var checked_urls = this.knowledge.filter((item) => item.is_checked).map((item) => item.url);

      }else{
        var checked_urls = this.knowledge.map((item) => item.url);
        console.log("Checked URLs")
        console.log(checked_urls)
      }

      // Prepare the payload
      var payload = {
        query: query,
        urls: checked_urls,
      }

      this.chat.push({
        type: 'user',
        message: query,
        time: this.getFormattedTime(),
      });

      axios({
        method: "post",
        url: "http://127.0.0.1:8000/rag_query",
        data: payload,
        headers: { "Content-Type": "application/json" },
        }).then((response) => {

          
          var formattedResponse = this.extractSource(response.data.result);
          console.log(formattedResponse)
          // Add the response to the chat
          this.chat.push({
            type: 'ai',
            message: formattedResponse.textContent,
            time: this.getFormattedTime(),
            source: formattedResponse.source,
          });

        }).catch(function (response) {
          console.log(response);
      });

    },

    // Updates when the knowledge is ticked for use in the RAG model
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
