<template>
  <div class="container">
    <main>
      <div class="py-5 text-center centered">
        <img class="d-block mx-auto mb-4 favicon-icon" src="/icon.svg" alt="VK" />
        <div>
          <p class="lead">Вставьте ссылку на видео в форму ниже</p>
          <div class="lead center-form">
            <input
              type="text"
              class="form-control"
              v-model="link_video"
              autocomplete="off"
              placeholder="Например, https://vk.com/vk?z=video-22822305_456241782%2Fvideos-22822305%2Fpl_-22822305_-2"
              title="Например, https://vk.com/vk?z=video-22822305_456241782%2Fvideos-22822305%2Fpl_-22822305_-2"
            />
            <button
              class="w-100 btn btn-primary btn-lg"
              type="submit"
              style="margin-top: 10px"
              @click="getLinkVideo"
            >
              Вставить
            </button>
            <div v-show="link.length !== 0">
              <p class="lead"></p>
              <div class="lead center-video">
                <!-- <video class="center-video" controls="controls" style="margin-bottom: 10px">
              <source :src="link['video']" type="video/mp4" />
              Тег video не поддерживается вашим браузером.
            </video> -->
                <p class="lead">{{ link["title"] }}</p>
                <a class="w-100 btn btn-primary btn-lg center-video" :href="link['video']"
                  >Скачайте видео</a
                >
              </div>
            </div>
            <div v-show="loading===true" class="spinner-border mt-5" role="status">
            </div>
            <div class=" mt-5 text-danger lead" v-show="error_video != ''">
             <p>{{error_video.detail}}</p>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data: () => ({
    loading: false,
    link: '',
    link_video: '',
    error_video: ''
  }),
  methods: {
    getLinkVideo () {
      this.loading = true
      axios
        .get(
          '/link_vk?user_agent=' + navigator.userAgent + '&link=' +
            this.link_video
        )
        .then((response) => {
          this.loading = false
          this.link = response.data
        })
        .catch((error) => {
          this.loading = false
          this.error_video = error.response.data
        })
    }
  }
}
</script>
