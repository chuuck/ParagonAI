<template>
    <div class="flex flex-col items-center flex-grow h-screen">

        <div class="flex flex-col items-center flex-grow justify-center">

            <div class="flex justify-center items-center bg-[#5825FC] h-24 w-24 rounded-[30px] mt-24">
                <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-flare" width="48" height="48" viewBox="0 0 24 24" stroke-width="1" stroke="white" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                    <path d="M12 3l3 6l6 3l-6 3l-3 6l-3 -6l-6 -3l6 -3z" />
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
