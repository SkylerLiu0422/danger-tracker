<template>
  <n-layout has-sider position="absolute" style="top: 64px; bottom: 64px;">
    <n-layout-sider
        bordered
        show-trigger
        collapse-mode="width"
        :collapsed-width="64"
        :collapsed="collapsed"
        :width="272"
        :native-scrollbar="false"
        @collapse="collapsed = true"
        @expand="collapsed = false">
      <n-menu
        :collapsed="collapsed"
        :collapsed-width="64"
        :collapsed-icon-size="22"
        :options="menuOptions"
        @update:value="handleMenuRouter"/>
    </n-layout-sider>
    <n-layout content-style="padding: 32px 24px 56px 56px;">
      <router-view />
    </n-layout>
  </n-layout>
</template>

<script>
import  { h, ref } from 'vue'
import { useRouter } from 'vue-router'

import { NLayout, NLayoutSider, NMenu, NIcon } from 'naive-ui'
import {
  BulbFilled as BodyIcon,
  AudioFilled as VoiceIcon,
} from '@vicons/antd'

function renderIcon (icon) {
  return () => h(NIcon, null, { default: () => h(icon) })
}

const menuOptions = [
  {
    label: 'Body Indicator',
    key: 'body-indicator',
    icon: renderIcon(BodyIcon)
  },
  {
    label: 'Voice Recognition DEMO',
    key: 'voice-recognition',
    icon: renderIcon(VoiceIcon)
  }
]

export default {
  components: {
    NLayout,
    NLayoutSider,
    NMenu,
  },
  setup() {
    const $router = useRouter()

    return {
      collapsed: ref(false),
      menuOptions,
      handleMenuRouter(key) {
        $router.push('/' + key)
      }
    }
  }
}
</script>

<style scoped>

</style>