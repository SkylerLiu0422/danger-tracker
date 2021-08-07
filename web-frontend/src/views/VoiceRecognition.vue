<template>
  <div>
    <h1>Voice Recognition (only for DEMO)</h1>
    <div class="container">
      <div style="padding-right: 1.5rem;">
        <n-card>
          <n-space vertical>
            <n-steps vertical :current="current" :status="currentStatus">
              <n-step
                title="Upload your voice file"
                description="Only supports wav、mp3、m4a、flv、mp4、wma、3gp、amr、aac、ogg-opus、flac format file" />
              <n-step
                title="Recognize your voice"
                description="The server is stepping up recognition!" />
            </n-steps>
          </n-space>
          <template #action>
            <n-upload action="/api/voice/upload" :on-before-upload="handleBeforeUpload" @finish="handleAfterUpload">
              <n-button>Upload</n-button>
            </n-upload>
          </template>
        </n-card>
      </div>
      <div style="padding-left: 1.5rem">
        <n-card title="Recognition Results">
          <n-skeleton text v-if="loading" :repeat="2" />
          <n-thing v-else-if="finished">
            <n-space vertical>
              <n-alert v-if="dangerStatus" title="Potential" type="warning">
                Exist potential life risk!
              </n-alert>
              <n-alert v-else title="Normal" type="success">
                No potential risks found!
              </n-alert>
              <n-thing style="font-size: 1.5rem">
                {{ speechResult }}
              </n-thing>
            </n-space>
          </n-thing>
          <n-empty v-else description="Wait for upload" />
        </n-card>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { ref } from 'vue'
import { NCard, NButton, NUpload, NSpace, NStep, NSteps, NSkeleton, NThing, NAlert, NEmpty } from 'naive-ui'

const danger_words = [
    "救", "死", "杀",
]

export default {
  name: "VoiceRecognition",
  components: {
    NCard,
    NButton,
    NUpload,
    NSpace,
    NStep,
    NSteps,
    NSkeleton,
    NThing,
    NAlert,
    NEmpty
  },
  setup() {
    const current = ref(1)
    const currentStatus = ref('wait')
    const loading = ref(false)
    const finished = ref(false)
    const speechResult = ref("")
    const dangerStatus = ref(false)

    const handleBeforeUpload = () => {
      finished.value = false
      current.value = 1
      currentStatus.value = "process"
    }

    const handleAfterUpload = ({ file, event }) => {
      let fileInfo = JSON.parse(event.target.response)
      current.value = 2
      currentStatus.value = "process"
      loading.value = true
      dangerStatus.value = false
      axios.get("/api/voice/recognize", {
        params: {
          filename: fileInfo.filename,
        }
      }).then(res => {
        let result = res.data
        loading.value = false
        if (result.status === 1) {
          currentStatus.value = "finish"
        } else {
          currentStatus.value = "error"
        }
        speechResult.value = result.data.split("]")[1].trim()
        for (let item of danger_words) {
          if (speechResult.value.indexOf(item) !== -1) {
            dangerStatus.value = true
          }
        }
        finished.value = true
      })
    }

    return {
      current,
      currentStatus,
      handleBeforeUpload,
      handleAfterUpload,
      loading,
      finished,
      speechResult,
      dangerStatus,
    }
  }
}
</script>

<style scoped>
.container {
  display: grid;
  grid-template-columns: 50% 50%;
}
</style>