<template>
    <div class="h-fit w-4/6 ml-auto mr-auto bg-white rounded-3xl border-2 border-[#f1f1f3] shadow-sm flex">
        <div class="w-1/12 rounded-l-3xl flex justify-end">
            <div class="flex items-center justify-center w-10 h-10 rounded-full bg-[#5825FC] mt-8">
                <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-flare" width="18" height="18" viewBox="0 0 24 24" stroke-width="1" stroke="white" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                    <path d="M12 3l3 6l6 3l-6 3l-3 6l-3 -6l-6 -3l6 -3z" />
                </svg>
            </div> 
        </div>

        <div class="w-11/12 flex flex-col">
            <!-- Header Section -->
            <div class="p-4 rounded-tr-3xl flex items-center mt-6">
                <p class="font-medium mr-2">Paragon.ai</p>
                <div class="border-l border-gray-300 h-4 mx-2"></div>
                <p class="font-light text-gray-300">{{time}}</p>
            </div>

            <!-- Content Section -->
            <div class="flex-grow rounded-br-3xl ml-4 pb-4">
                <p class="mr-8">{{ai_text}}</p>
            </div>

            <div class="ml-4 mr-20 rounded-xl p-2 mb-6 pb-2">
                <hr class="border-gray-800 dark:border-white opacity-5">
                <h2 class="font-bold mt-4">Sources:</h2>
                <div class="pl-8 italic">
                    <ul>
                        <li v-for="url in formattedSources" :key="url">
                            <a :href="url" target="_blank" rel="noopener noreferrer" class="text-blue-500 underline">
                                {{ url }}
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'UserPrompt', 
    props: {
        ai_text: {
            type: String,
            required: true,
        },
        time: {
            type: String,
            required: true,
        },
        source: {
            type: Array,
            required: true,
        },
    },
    computed: {
        formattedSources() {
            return this.source.map(url => url.replace(/['"]+/g, '').trim());
        }
    }
}
</script>
