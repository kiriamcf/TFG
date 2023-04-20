<script setup>
import { ref } from 'vue';

const prova = ref(0);
</script>

<template>
  <div class="h-[100vh] bg-main-gray">
    <section class="max-w-4xl mx-auto py-8">
      <div class="text-center flex flex-col gap-8 items-center">
        <h1
          class="text-9xl font-sans bg-clip-text text-transparent bg-gradient-to-r from-main-blue-dark to-main-green pb-2">
          Lyrically
        </h1>

        <h3 class="text-4xl text-main-white">
          Cover image generator for your song lyrics
        </h3>

        <button
          class="text-main-white font-normal px-8 py-3 text-2xl border-4 border-main-white w-fit uppercase hover:shadow-custom-button-white hover:font-medium transition-all duration-300">
          begin
        </button>
      </div>

      <!-- <div>
            <h3 class="text-center text-main-white text-2xl">Default learning models provided by...</h3>
            <div class="grid grid-cols-3 gap-8">
                <div class="rounded p-4 flex items-center justify-center border border-main-gray-soft">
                    <img src="/ico/StabilityAi_Logo.svg" alt="StabilityAi-Logo" class="max-w-[15rem]">
                </div>
                                                        <div class="rounded p-4 flex items-center justify-center border border-main-gray-sof">
                                                            <img src="/ico/CompVis_Logo.svg" alt="CompVis-Logo" class="max-w-[15rem]">
                                                                    </div>
                                                                    <div class="rounded p-4 flex items-center justify-center border border-main-gray-sof">
                                                                        <img src="/ico/Runway_Logo.svg" alt="Runway-Logo" class="max-w-[15rem]">
                                                                    </div>
                                                                </div>
                                                            </div> -->
    </section>
  </div>
</template>
