<template>
  <div>
    <h1>Body Indicator</h1>
    <div v-if="!loading" class="container">
      <div style="padding-right: 1.5rem;">
        <n-card title="Current Status">
          <template #header-extra>Last updated: {{ currentTime }}</template>
          <n-alert v-if="currentStatus === 'normal'" title="Normal" type="success">
            You are very healthy now. Keep it up.
          </n-alert>
          <n-alert v-if="currentStatus === 'attention'" title="Attention" type="warning">
            You may have potential health risks, it is recommended to see your family doctor!
          </n-alert>
          <n-alert v-if="currentStatus === 'danger'" title="Danger" type="error">
            You are in danger now, and we have called the emergency call for you!
          </n-alert>
          <template #action>
            <n-button type="primary" text @click="updateData">Refresh</n-button>
          </template>
        </n-card>
      </div>
      <div style="padding-left: 1.5rem;">
        <n-data-table :loading="loading" min-height=32 size="large" :columns="columns" :data="indicators" :pagination="pagination" />
      </div>
    </div>
  </div>
</template>

<script>
import { h, ref, onMounted, computed } from 'vue'
import { NCard, NAlert, NDataTable, NButton } from 'naive-ui'
import axios from 'axios'

Date.prototype.format = function(fmt) {
  const o = {
    "M+" : this.getMonth()+1,                 //月份
    "d+" : this.getDate(),                    //日
    "H+" : this.getHours(),                   //小时
    "m+" : this.getMinutes(),                 //分
    "s+" : this.getSeconds(),                 //秒
    "q+" : Math.floor((this.getMonth()+3)/3), //季度
    "S"  : this.getMilliseconds()             //毫秒
  };
  if(/(y+)/.test(fmt)) {
    fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));
  }
  for(let k in o) {
    if(new RegExp("("+ k +")").test(fmt)){
      fmt = fmt.replace(RegExp.$1, (RegExp.$1.length===1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
    }
  }
  return fmt;
}

function renderText(text, color) {
  return h("span", {
    class: color
  }, { default: () => text  })
}

const tableColumns = () => {
  return [
    {
      title: 'Time',
      key: 'time',
    },
    {
      title: 'Heart Rate',
      key: 'heart_rate',
    },
    {
      title: 'Blood Oxygen',
      key: 'blood_oxygen_levels',
    },
    {
      title: 'Heart Status',
      key: 'heart_status',
    },
    {
      title: 'Oxygen Status',
      key: 'oxygen_status',
    },
    {
      title: "Overall Status",
      key: "overall",
      render(row) {
        return renderText(row.body_status, "d-" + row.body_status)
      }
    }
  ]
}

export default {
  name: "BodyIndicator",
  components: {
    NCard,
    NAlert,
    NDataTable,
    NButton,
  },
  setup() {
    const currentTime = ref()
    const indicators = ref()
    const loading = ref(true)

    const getBodyStatusByUid = uid => {
      axios.get('/api/indicators', {
        params: {
          uid: uid,
        }
      }).then(res => {
        indicators.value = res.data
        loading.value = false
      })
    }

    const currentStatus = computed(() => {
      return indicators.value[0].body_status
    })

    const updateData = () => {
      currentTime.value = new Date().format("yyyy-MM-dd HH:mm:ss")
      getBodyStatusByUid("874a30cc-f4c5-11eb-9050-e0d4645ff956")
    }

    onMounted(() => {
      updateData()
      setInterval(() => {
        updateData()
      }, 30000)
    })

    return {
      currentTime,
      indicators,
      loading,
      currentStatus,
      columns: tableColumns(),
      updateData,
      pagination: {
        pageSize: 10,
      },
    }
  }
}
</script>

<style>
.d-normal {
  color: green;
}
.d-attention {
  color: yellow;
}
.d-danger {
  color: red;
}
</style>

<style scoped>
.container {
  display: grid;
  grid-template-columns: 50% 50%;
}
</style>