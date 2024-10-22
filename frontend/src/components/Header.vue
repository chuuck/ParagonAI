<template>
  <div class="flex items-center justify-between space-x-4 mt-6">
    <div class="flex items-center">
      <div class="flex h-12 w-12 bg-[#5825FC] justify-center items-center rounded-2xl">

        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="icon icon-tabler icon-tabler-flare"
          width="26"
          height="26"
          viewBox="0 0 24 24"
          stroke-width="1"
          stroke="white"
          fill="none"
          stroke-linecap="round"
          stroke-linejoin="round"
          :class="{ 'spin-animation': isSpinning }"
        >
          <path stroke="none" d="M0 0h24v24H0z" fill="none" />
          <path d="M12 3l3 6l6 3l-6 3l-3 6l-3 -6l-6 -3l6 -3z" />
        </svg>
      </div>

      <h2 class="text-xl font-medium ml-4">
        Pa<span style="color: #5825FC;">rag</span>on.ai
      </h2>
    </div>

    <div class="flex items-center justify-center cursor-pointer">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon icon-tabler icon-tabler-layout-sidebar"
        width="20"
        height="20"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="#2c3e50"
        fill="none"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none" />
        <path d="M4 4m0 2a2 2 0 0 1 2 -2h12a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2z" />
        <path d="M9 4l0 16" />
      </svg>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isSpinning: false,
    };
  },
};
</script>

<style scoped>

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.spin-animation {
  animation: spin 2s linear infinite; 
}
</style>
