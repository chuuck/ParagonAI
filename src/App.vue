<template>

  <div class="h-screen w-screen bg-[#F7F8FA] flex">

    <div class="w-3/12 bg-[#F7F8FA] p-6">
      <Header />
      <button type="button" @click="open_url_modal" class=" w-full rounded-lg mt-6 h-10 bg-[#F7F8FA] text-black border border-dashed hover:bg-[#EEEFF0] border-[#5825FC] px-2.5 py-1.5 text-sm font-semibold shadow-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#5825FC]">Add Knowledge</button>
      <KnowledgeBase class="mt-8"/>
    </div>


    <div class="w-9/12 bg-gradient-to-tl from-[#E9EBF9] to-white flex flex-col mt-4 ml-4 mr-4 rounded-t-3xl shadow-sm border-2">
        <!-- <Intro/> -->

        <UserPrompt />
        <AIResponsePrompt />
        
    
        <div class="flex-grow"></div>
        <ChatInput />
    </div>




  </div>
  

</template>

<script>
import Intro from './components/Intro.vue'
import ChatInput from './components/ChatInput.vue'
import Header from './components/Header.vue'
import KnowledgeBase from './components/KnowledgeBase.vue'
import AIResponsePrompt from './components/AIResponsePrompt.vue'
import UserPrompt from './components/UserPrompt.vue'
import URLModal from './components/URLModal.vue'

export default {
  components: {
    Intro,
    ChatInput,
    Header,
    KnowledgeBase,
    AIResponsePrompt,
    UserPrompt,
    URLModal
  },
  methods: {
    open_url_modal() {
      document.getElementById('hs-basic-modal').classList.remove('hidden')
      document.getElementById('hs-basic-modal').classList.add('opacity-100')
    }
  },
}
</script>

