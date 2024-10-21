<template>
    <div class="h-fit w-4/6 ml-auto mr-auto flex">
        <div class=" w-fill rounded-l-3xl flex justify-end">
            <div class="w-10 h-10 rounded-full mt-8">
                <span class="inline-block h-10 w-10 overflow-hidden rounded-full bg-gray-100">
                    <svg class="h-full w-full text-gray-300" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M24 20.993V24H0v-2.996A14.977 14.977 0 0112.004 15c4.904 0 9.26 2.354 11.996 5.993zM16.002 8.999a4 4 0 11-8 0 4 4 0 018 0z" />
                    </svg>
                </span>
            </div> 
        
        </div>

        <div class="w-11/12 flex flex-col">
            <!-- Header Section -->
            <div class="p-4 rounded-tr-3xl flex items-center mt-6">
                <p class="font-medium mr-2">User</p>
                <div class="border-l border-gray-300 h-4 mx-2"></div>
                <p class="font-light text-gray-300">{{time}}</p>
            </div>

            <!-- Content Section -->
            <div class="flex-grow rounded-br-3xl ml-4 pb-8">
                <p class="mr-6">{{user_text}}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'UserPrompt', 
    props: {
        user_text: {
            type: String,
            required: true,
        },
        time: {
            type: String,
            required: true,
        },
    },
}
</script>