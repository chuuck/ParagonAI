<template>
    <div class="flex flex-col items-center flex-grow h-screen">

        <div class="flex flex-col items-center flex-grow justify-center">

            <div class="flex justify-center items-center bg-[#5825FC] h-24 w-24 rounded-[30px] mt-24">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.2" stroke="#E8E8E8" class="size-14">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25" />
                </svg>
            </div>

            <h1 class="text-[#A69B9F] font-semibold mt-8 text-5xl">Hello there! 👋</h1>
            <h1 class="text-[#524A4F] font-semibold mt-1 text-5xl">Can I help you with anything?</h1>

            <p class="text-[#7B85A2] font-light text-center mt-4 text-lg tracking-wide">
                Ready to assist you with anything you need, from answering <br> questions to providing recommendations. Let's get started!
            </p>
        </div>

        <div class="mb-4">
            <InfoBlocks />
        </div>

    </div>
</template>


<script>
import InfoBlocks from './InfoBlocks.vue'

export default{
    components: {
        InfoBlocks
    }
}
</script>

<style>

</style>
