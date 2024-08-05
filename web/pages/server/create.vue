<template>
<q-stepper
      v-model="step"
      vertical
      color="primary"
      animated
    >
      <q-step
        :name="1"
        title="选择实例类别"
        icon="settings"
        :done="step > 1"
      >

    <a-space wrap>
        <q-field outlined stack-label>
        <template v-slot:prepend>
          <q-avatar>
            <img src="https://api.simpfun.cn/static/images/minecraft.png">
          </q-avatar>
        </template>
        <template v-slot:control>
          <div class="self-center full-width no-outline" tabindex="0">
          <strong>Minecraft JE</strong>
          </div>
        </template>
      </q-field>
      
       <q-field outlined stack-label>
        <template v-slot:prepend>
          <q-avatar>
            <img src="https://api.simpfun.cn/static/images/minecraft/bedrock.png">
          </q-avatar>
        </template>
        <template v-slot:control>
          <div class="self-center full-width no-outline" tabindex="0">
          <strong>Minecraft BE</strong>
          </div>
        </template>
      </q-field>
   </a-space>

        <q-stepper-navigation>
          <q-btn @click="step = 2" color="primary" label="下一步" />
        </q-stepper-navigation>
      </q-step>

      <q-step
        :name="2"
        title="选择实例服务端"
        icon="hourglass_bottom"
        :done="step > 2"
      >
        An ad group contains one or more ads which target a shared set of keywords.

        <q-stepper-navigation>
          <q-btn @click="step = 4" color="primary" label="Continue" />
          <q-btn flat @click="step = 1" color="primary" label="Back" class="q-ml-sm" />
        </q-stepper-navigation>
      </q-step>

    
    </q-stepper>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

useHead({title: "创建实例｜FuCube"})
const step = ref(1)
</script>
