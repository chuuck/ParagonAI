<template>
  <TransitionRoot as="template" :show="isOpen">
    <Dialog class="relative z-10" @close="closeModal">
      <TransitionChild
        as="template"
        enter="ease-out duration-300"
        enter-from="opacity-0"
        enter-to="opacity-100"
        leave="ease-in duration-200"
        leave-from="opacity-100"
        leave-to="opacity-0"
      >
        <div class="fixed inset-0 bg-gray-900 bg-opacity-50 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div class="flex min-h-full items-center justify-center p-4 text-center sm:p-0">
          <TransitionChild
            as="template"
            enter="ease-out duration-300"
            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enter-to="opacity-100 translate-y-0 sm:scale-100"
            leave="ease-in duration-200"
            leave-from="opacity-100 translate-y-0 sm:scale-100"
            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
          >
            <DialogPanel
              class="relative transform overflow-hidden rounded-xl bg-white text-left shadow-2xl transition-all sm:my-8 sm:w-full sm:max-w-lg"
            >
            
              <div class="px-6 py-5 sm:p-6">
                <div class="sm:flex sm:items-start">
                  <div class="text-center sm:ml-4 sm:mt-0 sm:text-left w-full">
                    <DialogTitle
                      as="h3"
                      class="text-lg font-bold leading-6 text-gray-800"
                    >
                      Enter OpenAI API Key
                    </DialogTitle>
                    <div class="mt-4 w-full">
                      <label
                        class="block text-sm font-medium text-gray-700 mb-2"
                        >API Key</label
                      >
                      <input
                        type="text"
                        id="key"
                        class="py-3 shadow-sm px-4 block w-full border border-gray-300 rounded-lg text-sm focus:border-blue-600 focus:ring focus:ring-blue-600 focus:ring-opacity-50"
                        placeholder="sk-..."
                        v-model="api_key"
                      />
                    </div>
                  </div>
                </div>
              </div>

              <div
                class="bg-gray-50 px-6 py-4 flex justify-end space-x-3 sm:space-x-4"
              >
                <button
                  type="button"
                  class="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                  @click="addKey"
                >
                  Add
                </button>
                <button
                  type="button"
                  class="inline-flex justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                  @click="closeModal"
                >
                  Cancel
                </button>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script>
import { ref } from 'vue';
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue';
import axios from 'axios';

export default {
  props: {
    isOpen: {
      type: Boolean,
      required: true,
    },
  },
  components: {
    Dialog,
    DialogPanel,
    DialogTitle,
    TransitionChild,
    TransitionRoot,
  },
  data() {
    return {
      api_key: '',
    };
  },
  methods: {
    closeModal() {
      this.$emit('close-modal');
    },
    addKey() {
      var bodyFormData = new FormData();
      bodyFormData.append('api_key', this.api_key);

      axios({
        method: "post",
        url: "http://127.0.0.1:8000/set_openai_api_key",
        data: bodyFormData,
        headers: { "Content-Type": "application/json" },
      }).then((response) => {
        this.closeModal();
      }).catch(function (response) {
        console.log(response);
      });

    },
  },
};
</script>
