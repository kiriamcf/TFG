<script setup>
import { reactive, ref } from 'vue';
import { Motion, Presence } from 'motion/vue';
import IcoChevronDown from './components/IcoChevronDown.vue';
import IcoLoading from './components/IcoLoading.vue';
import IcoPlus from './components/IcoPlus.vue';

const options = reactive({
  begin: false,
  choseAlbum: false,
  choseSong: false,
  album: {
    songAmount: 1,
    activeSong: 1,
    openGenre: false,
    invalidData: false,
  },
  song: {
    openGenre: false,
    invalidData: false,
  },
  processing: false,
  canShowImage: false,
  image: null,
});

const formDataSong = reactive({
  songName: null,
  genre: null,
  artist: null,
  lyrics: null,
  resolution: null,
});

const formDataAlbum = reactive({
  albumName: null,
  genre: null,
  artist: null,
  resolution: null,
  songs: [
    {
      songName: null,
      lyrics: null,
    },
  ],
});

function setGenreSong(selectedGenre) {
  formDataSong.genre = selectedGenre;
  options.song.openGenre = false;
}

function setGenreAlbum(selectedGenre) {
  formDataAlbum.genre = selectedGenre;
  options.album.openGenre = false;
}

async function submitFormSong() {
  if (options.processing) {
    return;
  }

  if (
    formDataSong.genre === null ||
    formDataSong.artist == null ||
    formDataSong.songName == null ||
    formDataSong.lyrics == null ||
    formDataSong.resolution == null
  ) {
    options.song.invalidData = true;
    return;
  }

  options.processing = true;
  options.song.invalidData = false;

  let res = await axios
    .post('/api/song-script', formDataSong)
    .catch(() => console.log('Something went wrong'));

  options.processing = false;
  options.canShowImage = true;

  let image = res.data.url;

  options.image = image;
}

function handleType(type) {
  if (type == 'song') {
    (options.choseSong = true), (options.choseAlbum = false);
  } else {
    (options.choseSong = false), (options.choseAlbum = true);
  }
}

function handleAddSongToAlbum() {
  options.album.songAmount = options.album.songAmount + 1;

  formDataAlbum.songs.push({
    songName: null,
    lyrics: null,
  });
}

async function submitFormAlbum() {
  if (options.processing) {
    return;
  }

  if (
    formDataAlbum.genre === null ||
    formDataAlbum.artist == null ||
    formDataAlbum.albumName == null ||
    formDataAlbum.resolution == null ||
    (formDataAlbum.songs.length == 1 &&
      (formDataAlbum.songs[0].songName == null ||
        formDataAlbum.songs[0].lyrics == null))
  ) {
    options.album.invalidData = true;
    return;
  }

  options.processing = true;
  options.album.invalidData = false;

  let res = await axios
    .post('/api/album-script', formDataAlbum)
    .catch(() => console.log('Something went wrong'));

  options.processing = false;
  options.canShowImage = true;

  let image = res.data.url;

  options.image = image;
}
</script>

<template>
  <div class="min-h-[100vh] bg-main-black">
    <section class="max-w-4xl mx-auto py-8">
      <div class="text-center flex flex-col gap-8 items-center">
        <h1
          class="text-9xl font-sans bg-clip-text text-transparent bg-gradient-to-r from-main-blue-dark to-main-green pb-2">
          Lyrically
        </h1>

        <Presence>
          <Motion
            v-show="!options.begin"
            :animate="{ opacity: 1, scale: 1 }"
            :exit="{ opacity: 0, scale: 0.6 }">
            <h3 class="text-4xl text-main-white">
              Cover image generator for your song lyrics
            </h3>
          </Motion>
        </Presence>

        <Presence>
          <Motion
            v-show="!options.begin"
            :animate="{ opacity: 1, scale: 1 }"
            :exit="{ opacity: 0, scale: 0.6 }">
            <p class="text-gray-400">
              Explore endless variations until you find the image that better
              suits your song
            </p>
          </Motion>
        </Presence>

        <Presence>
          <Motion
            v-show="!options.begin"
            :animate="{ opacity: 1, scale: 1 }"
            :exit="{ opacity: 0, scale: 0.6 }">
            <button
              class="text-gray-400 px-4 py-2 border border-gray-400 rounded text-xl hover:text-main-white hover:border-main-white transition-colors"
              @click="options.begin = true">
              Begin
            </button>
          </Motion>
        </Presence>

        <Presence class="w-full">
          <Motion
            v-if="options.begin"
            :initial="{ opacity: 0, scale: 0 }"
            :animate="{ opacity: 1, scale: 1, transition: { delay: 0.5 } }">
            <div class="flex gap-4 max-w-lg mx-auto">
              <button
                type="submit"
                class="text-main-black bg-main-white px-4 py-3 rounded hover:text-main-white hover:bg-main-pink transition-colors duration-300 w-full"
                :class="{
                  '!text-main-white !bg-main-pink': options.choseAlbum,
                }"
                @click.prevent="handleType('album')">
                Album
              </button>
              <button
                type="submit"
                class="text-main-black bg-main-white px-4 py-3 rounded hover:text-main-white hover:bg-main-pink transition-colors duration-300 w-full"
                :class="{
                  '!text-main-white !bg-main-pink': options.choseSong,
                }"
                @click.prevent="handleType('song')">
                Single
              </button>
            </div>
          </Motion>
        </Presence>

        <Presence class="w-full">
          <Motion
            v-if="options.choseSong"
            :initial="{ opacity: 0, scale: 0 }"
            :animate="{ opacity: 1, scale: 1, transition: { duration: 1 } }"
            :exit="{ opacity: 0, scale: 0.6 }">
            <form
              class="flex flex-col items-center gap-4 max-w-lg mx-auto rounded-lg bg-secondary-black p-8 shadow-2xl">
              <div class="relative w-1/2">
                <!-- trigger button -->
                <button
                  type="button"
                  @click="options.song.openGenre = !options.song.openGenre"
                  class="flex w-full items-center justify-between rounded p-2 bg-main-gray text-gray-400 shadow-lg">
                  <span>{{
                    formDataSong.genre == null
                      ? 'Choose music genre'
                      : formDataSong.genre
                  }}</span>
                  <span
                    class="text-2xl w-5 h-5 grid place-content-center text-gray-400"
                    ><IcoChevronDown
                  /></span>
                </button>

                <!-- list items -->
                <ul
                  class="z-2 absolute mt-2 w-full rounded bg-main-gray shadow-2xl divide-y divide-gray-500"
                  v-show="options.song.openGenre">
                  <li
                    class="cursor-pointer select-none p-2 bg-main-gray rounded-t text-gray-400 hover:bg-gray-600"
                    @click="setGenreSong('Metal')">
                    Metal
                  </li>
                  <li
                    class="cursor-pointer select-none p-2 bg-main-gray text-gray-400 hover:bg-gray-600"
                    @click="setGenreSong('Rock')">
                    Rock
                  </li>
                  <li
                    class="cursor-pointer select-none p-2 bg-main-gray rounded-b text-gray-400 hover:bg-gray-600"
                    @click="setGenreSong('Pop')">
                    Pop
                  </li>
                </ul>
              </div>

              <input
                type="text"
                required
                placeholder="Artist..."
                v-model="formDataSong.artist"
                class="w-full p-2 rounded outline-none bg-main-gray text-gray-400 placeholder:text-gray-400 shadow-lg" />

              <input
                type="text"
                required
                placeholder="Song name..."
                v-model="formDataSong.songName"
                class="w-full p-2 rounded outline-none bg-main-gray text-gray-400 placeholder:text-gray-400 shadow-lg" />

              <textarea
                name="lyrics"
                required
                id="lyrics"
                cols="30"
                rows="10"
                placeholder="Copy and paste the song lyrics here..."
                v-model="formDataSong.lyrics"
                class="block w-full p-2 transition bg-main-gray text-gray-400 placeholder:text-gray-400 rounded shadow-lg focus:outline-none disabled:opacity-50 disabled:cursor-not-allowed resize-none" />

              <div class="flex gap-4 justify-left items-center w-full">
                <h3 class="text-gray-400">Resolution:</h3>
                <button
                  class="text-gray-400 px-4 py-2 border border-gray-400 rounded hover:text-main-white hover:border-main-white transition-colors"
                  :class="{
                    '!text-main-white !border-main-white':
                      formDataSong.resolution == '512',
                  }"
                  @click.prevent="formDataSong.resolution = 512">
                  512x512
                </button>
                <button
                  class="text-gray-400 px-4 py-2 border border-gray-400 rounded hover:text-main-white hover:border-main-white transition-colors"
                  :class="{
                    '!text-main-white !border-main-white':
                      formDataSong.resolution == '728',
                  }"
                  @click.prevent="formDataSong.resolution = 728">
                  768x768
                </button>
              </div>

              <div
                class="w-full rounded bg-red-600 text-main-white px-4 py-2"
                v-if="options.album.invalidData">
                Please fill all of the fields correctly
              </div>

              <button
                type="submit"
                class="text-main-black bg-main-white px-4 py-3 rounded hover:text-main-white hover:bg-main-pink transition-colors duration-300 w-full"
                @click.prevent="submitFormSong">
                Submit
              </button>
            </form>
          </Motion>
        </Presence>

        <Presence class="w-full">
          <Motion
            v-if="options.choseAlbum"
            :initial="{ opacity: 0, scale: 0 }"
            :animate="{ opacity: 1, scale: 1, transition: { duration: 1 } }"
            :exit="{ opacity: 0, scale: 0.6 }">
            <form
              class="flex flex-col items-center gap-4 rounded-lg bg-secondary-black p-8 shadow-2xl">
              <div class="relative w-1/2">
                <!-- trigger button -->
                <button
                  type="button"
                  @click="options.album.openGenre = !options.album.openGenre"
                  class="flex w-full items-center justify-between rounded p-2 bg-main-gray text-gray-400 shadow-lg">
                  <span>{{
                    formDataAlbum.genre == null
                      ? 'Choose music genre'
                      : formDataAlbum.genre
                  }}</span>
                  <span
                    class="text-2xl w-5 h-5 grid place-content-center text-gray-400"
                    ><IcoChevronDown
                  /></span>
                </button>

                <!-- list items -->
                <ul
                  class="z-2 absolute mt-2 w-full rounded bg-main-gray shadow-2xl divide-y divide-gray-500"
                  v-show="options.album.openGenre">
                  <li
                    class="cursor-pointer select-none p-2 bg-main-gray rounded-t text-gray-400 hover:bg-gray-600"
                    @click="setGenreAlbum('Metal')">
                    Metal
                  </li>
                  <li
                    class="cursor-pointer select-none p-2 bg-main-gray text-gray-400 hover:bg-gray-600"
                    @click="setGenreAlbum('Rock')">
                    Rock
                  </li>
                  <li
                    class="cursor-pointer select-none p-2 bg-main-gray rounded-b text-gray-400 hover:bg-gray-600"
                    @click="setGenreAlbum('Pop')">
                    Pop
                  </li>
                </ul>
              </div>

              <input
                type="text"
                required
                placeholder="Artist..."
                v-model="formDataAlbum.artist"
                class="w-full p-2 rounded outline-none bg-main-gray text-gray-400 placeholder:text-gray-400 shadow-lg" />

              <input
                type="text"
                required
                placeholder="Album name..."
                v-model="formDataAlbum.albumName"
                class="w-full p-2 rounded outline-none bg-main-gray text-gray-400 placeholder:text-gray-400 shadow-lg" />

              <div class="flex gap-4 justify-left items-center w-full">
                <h3 class="text-gray-400">Resolution:</h3>
                <button
                  class="text-gray-400 px-4 py-2 border border-gray-400 rounded hover:text-main-white hover:border-main-white transition-colors"
                  :class="{
                    '!text-main-white !border-main-white':
                      formDataAlbum.resolution == '512',
                  }"
                  @click.prevent="formDataAlbum.resolution = 512">
                  512x512
                </button>
                <button
                  class="text-gray-400 px-4 py-2 border border-gray-400 rounded hover:text-main-white hover:border-main-white transition-colors"
                  :class="{
                    '!text-main-white !border-main-white':
                      formDataAlbum.resolution == '728',
                  }"
                  @click.prevent="formDataAlbum.resolution = 728">
                  768x768
                </button>
              </div>

              <div class="flex justify-between items-center w-full">
                <div class="flex gap-2 w-full flex-wrap">
                  <button
                    v-for="index in options.album.songAmount"
                    :key="index"
                    type="button"
                    class="text-gray-400 text-xl select-none hover:text-main-white hover:border-main-white transition-colors"
                    :class="{
                      '!text-main-pink': options.album.activeSong == index,
                    }"
                    @click.prevent="options.album.activeSong = index">
                    {{ index }}
                  </button>
                </div>
                <button
                  @click.prevent="handleAddSongToAlbum"
                  type="button"
                  class="flex gap-2 whitespace-nowrap items-center text-gray-400 px-4 py-2 border border-gray-400 rounded text-xl hover:text-main-white hover:border-main-white transition-colors">
                  Add song
                  <IcoPlus class="text-white flex-none cursor-pointer" />
                </button>
              </div>

              <input
                type="text"
                required
                placeholder="Song name..."
                v-model="
                  formDataAlbum.songs[options.album.activeSong - 1].songName
                "
                class="w-full p-2 rounded outline-none bg-main-gray text-gray-400 placeholder:text-gray-400 shadow-lg" />

              <textarea
                name="lyrics"
                required
                id="lyrics"
                cols="30"
                rows="10"
                v-model="
                  formDataAlbum.songs[options.album.activeSong - 1].lyrics
                "
                placeholder="Copy and paste the song lyrics here..."
                class="block w-full p-2 transition bg-main-gray text-gray-400 placeholder:text-gray-400 rounded shadow-lg focus:outline-none disabled:opacity-50 disabled:cursor-not-allowed resize-none" />

              <button
                type="submit"
                class="text-main-black bg-main-white px-4 py-3 rounded hover:text-main-white hover:bg-main-pink transition-colors duration-300 w-full"
                @click.prevent="submitFormAlbum">
                Submit
              </button>
            </form>
          </Motion>
        </Presence>

        <div class="mt-4" v-if="options.processing">
          <h3 class="text-xl text-main-white">Generating...</h3>
          <IcoLoading class="mx-auto" />
        </div>

        <div
          v-if="options.canShowImage"
          class="max-w-md mx-auto mt-8 flex flex-col gap-4">
          <img :src="options.image" alt="Generated Image" />
          <a
            class="text-main-black cursor-pointer bg-main-white px-4 py-3 rounded hover:text-main-white hover:bg-main-pink transition-colors duration-300"
            :href="options.image"
            download>
            Download
          </a>
        </div>
      </div>
    </section>
  </div>
</template>
