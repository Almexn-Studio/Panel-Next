<template>
<div>
<q-card >
        <q-tabs
          v-model="tab"
          dense
          class="text-grey h-12"
          active-color="primary"
          indicator-color="primary"
          align="justify"
          narrow-indicator
        >
       <q-tab name="login" label="登录" />
       <q-tab name="register" label="注册" />
</q-tabs>
<q-separator />
<q-tab-panels v-model="tab" animated>
          <q-tab-panel name="login">
    <q-form
      @submit="onLogin"
      class="q-gutter-md"
    >
      <q-input
        filled
        type="name"
        v-model="username"
        label="用户名"
        lazy-rules
        :rules="[
          val => val !== null && val !== '' || '请输入用户名',
        ]"
       />

      <q-input
        filled
        type="password"
        v-model="password"
        label="密码"
        lazy-rules
        :rules="[
          val => val !== null && val !== '' || '请输入密码',
        ]"
      />

      <div class="row justify-end">
        <q-btn label="登录" type="submit" color="primary"/>
       </div>
    </q-form>
</q-tab-panel>

  <q-tab-panel name="register">
    <q-form
      @submit="onReg"
      class="q-gutter-md"
    >
      <q-input
        filled
        type="name"
        v-model="username"
        label="用户名"
        lazy-rules
        :rules="[
          val => val !== null && val !== '' || '请输入用户名',
        ]"
       />
       <q-input
        filled
        type="email"
        v-model="email"
        label="邮箱"
        lazy-rules
        :rules="[
          val => val !== null && val !== '' || '请输入邮箱',
        ]"
       />
      <q-input
        filled
        type="password"
        v-model="password"
        label="密码"
        lazy-rules
        :rules="[
          val => val !== null && val !== '' || '请输入密码',
        ]"
      />

      <div class="row justify-end">
        <q-btn label="注册" type="submit" color="primary"/>
       </div>
    </q-form>
</q-tab-panel>

  </q-tab-panels>
</q-card>
</div>
</template>

<script>
import { useQuasar } from 'quasar'
import { ref } from 'vue'

export default {
  setup () {
    const $q = useQuasar()

    const username = ref(null)
    const password = ref(null)
    const email = ref(null)
    useHead({title: 'Auth｜FuCube'})

    return {
      username,
      password,
      email,
      tab: ref('login'),
      onLogin () {
          $q.loading.show({
          message: 'Doing something. Please wait...',
          boxClass: 'bg-grey-2 text-grey-9',
          spinnerColor: 'primary'
        })
  
      },
      onReg () {
         $q.loading.show({
          message: 'Doing something. Please wait...',
          boxClass: 'bg-grey-2 text-grey-9',
          spinnerColor: 'primary'
        })
         
         useFetch('/api/user/register', {
           body: {
              email: email,
              username: username,
              password: password
           }
        
        })
      },
    }
  }
}
</script>
