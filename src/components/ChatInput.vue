<template>
  <div class="flex items-center justify-center space-x-4 mb-6">
    <div class="flex items-center justify-center bg-[#5825FC] w-12 h-12 rounded-full shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="size-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="m18.375 12.739-7.693 7.693a4.5 4.5 0 0 1-6.364-6.364l10.94-10.94A3 3 0 1 1 19.5 7.372L8.552 18.32m.009-.01-.01.01m5.699-9.941-7.81 7.81a1.5 1.5 0 0 0 2.112 2.13" />
      </svg>
    </div>

    <div class="relative w-[750px]">
      <input 
        type="text" 
        class="shadow-sm py-3 px-4 pr-12 block w-full h-14 border-2 border-[#F0F2F5] rounded-full text-sm focus:border-[#5825FC] focus:ring-[#5825FC] disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:placeholder-neutral-500 dark:focus:ring-[#5825FC]" 
        placeholder="This is placeholder" 
        v-model="query"
        @keyup.enter="submit_query" 
      />
      
      <div class="absolute inset-y-0 right-4 flex items-center">
        <div class="flex items-center justify-center bg-[#5825FC] w-10 h-10 rounded-full cursor-pointer" @click="submit_query">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="w-5 h-5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5" />
          </svg>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: ''
    }
  },
  methods: {
    submit_query() {
      this.$emit('submit-query', this.query)
      this.query = ''
    }
  }
}
</script>

<style>

</style>
