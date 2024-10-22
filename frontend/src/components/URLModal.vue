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
              <!-- Modal Content -->
              <div class="px-6 py-5 sm:p-6">
                <div class="sm:flex sm:items-start">
                  <div class="text-center sm:ml-4 sm:mt-0 sm:text-left w-full">
                    <DialogTitle
                      as="h3"
                      class="text-lg font-bold leading-6 text-gray-800"
                    >
                      Add Knowledge
                    </DialogTitle>
                    <div class="mt-4 w-full">
                      <label
                        for="title"
                        class="block text-sm font-medium text-gray-700 mb-2"
                        >Knowledge Title</label
                      >
                      <input
                        type="text"
                        id="title"
                        class="py-3 shadow-sm px-4 block w-full border border-gray-300 rounded-lg text-sm focus:border-blue-600 focus:ring focus:ring-blue-600 focus:ring-opacity-50"
                        placeholder="E.g., Benefits of Remote Work"
                        v-model="title"
                      />
                    </div>
                    <div class="mt-4 w-full">
                      <label
                        for="url"
                        class="block text-sm font-medium text-gray-700 mb-2"
                        >Resource URL</label
                      >
                      <input
                        type="text"
                        id="url"
                        class="py-3 shadow-sm px-4 block w-full border border-gray-300 rounded-lg text-sm focus:border-blue-600 focus:ring focus:ring-blue-600 focus:ring-opacity-50"
                        placeholder="https://example.com/article"
                        v-model="url"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <!-- Modal Buttons -->
              <div
                class="bg-gray-50 px-6 py-4 flex justify-end space-x-3 sm:space-x-4"
              >
                <button
                  type="button"
                  class="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                  @click="addKnowledge"
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
      title: '',
      url: '',
    };
  },
  methods: {
    closeModal() {
      this.$emit('close-modal');
    },
    addKnowledge() {
      console.log('Adding knowledge');

      this.$emit('addKnowledge', {
        title: this.title,
        url: this.url,
      });

      this.$emit('close-modal');

      this.title = '';
      this.url = '';
    },
  },
};
</script>
