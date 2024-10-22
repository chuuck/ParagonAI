<template>

    <div class="flex h-16 w-fullmr-4  bg-white rounded-lg shadow-sm hover:border-[#e5e6e7] border-2 border-[#F7F8FA] cursor-pointer mt-4">
            <div class="w-1/5 flex items-center justify-center">
                <input type="checkbox" class="accent-[#5825FC] transform scale-125">
            </div>

            <div class="w-3/5 flex flex-col  justify-center text-sm font-medium">
                <h1 class="text-[#464646] text-sm font-medium truncate w-44">{{title}}</h1>
                <p class="text-xs text-[#A09A9E] truncate w-44">{{url}}</p>
            </div>

            <div class="flex items-center justify-center w-1/5">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="black" class="size-6 hover:stroke-red-600" @click="deleteKnowledge">
                    <path stroke-linecap="round" stroke-linejoin="round" d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" />
                </svg>
            </div>
    </div>
    
</template>

<script>

export default {
    name: 'KnowledgeBase',
    props: {
        title: {
            type: String,
            required: true,
        },
        url: {
            type: String,
            required: true,
        },
    },
    methods: {
        deleteKnowledge() {
            this.$emit('delete-knowledge', this.title);
        },
    },
}
</script>

<style>

</style>