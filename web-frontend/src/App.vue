<template>
  <n-loading-bar-provider>
    <n-config-provider :theme="darkTheme">
      <n-layout position="absolute">
        <n-layout-header bordered class="c-header">
          <c-header />
        </n-layout-header>
        <router-view />
        <n-layout-footer bordered position="absolute" class="c-footer">
          <c-footer />
        </n-layout-footer>
      </n-layout>
    </n-config-provider>
  </n-loading-bar-provider>
</template>

<script>
import { NLayout, NLayoutSider, NLayoutHeader, NLayoutFooter, NConfigProvider, darkTheme, NLoadingBarProvider } from 'naive-ui'

import CHeader from '@/components/CHeader/index.vue'
import CFooter from '@/components/CFooter/index.vue'

export default {
  components: {
    NLayout,
    NLayoutSider,
    NLayoutHeader,
    NLayoutFooter,
    NConfigProvider,
    NLoadingBarProvider,
    CHeader,
    CFooter,
  },
  setup() {
    return {
      darkTheme
    }
  }
}
</script>

<style>
.c-header,
.c-footer {
  height: 64px;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
  align-items: center;
}
.c-footer {
  justify-content: center;
}
</style>
