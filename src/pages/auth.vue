<template>
  <v-card class="mx-auto pa-8 pb-8"
      elevation="8"
      max-width="448"
      rounded="lg">
    <v-form validate-on="submit lazy" @submit.prevent="submit">
      <v-text-field
        v-model="email"
        density="compact"
        placeholder="Email address"
        prepend-inner-icon="mdi-email-outline"
        variant="outlined"
      ></v-text-field>
      <v-text-field
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="visible ? 'text' : 'password'"
        density="compact"
        placeholder="Enter your password"
        prepend-inner-icon="mdi-lock-outline"
        variant="outlined"
        @click:append-inner="visible = !visible"
      ></v-text-field>

        <v-btn
        :loading="loading"
        type="submit"
        class="mb-8"
        color="blue"
        size="large"
        variant="tonal"
        block
      >
        一键登录/注册
      </v-btn>
    </v-form>
  </v-card>
  

</template>

<script>
  export default {
    data: vm => ({
      email: '',
      password: '',
      visible: false,
      disable: false,
      loading: false,
    }),
    methods: {
      async submit (event) {
        this.loading = true
        this.disable = true
        
        await axios.post('/123' , { //后端注册接口
          email: this.email,
          password: this.password
        })
       .then(function (response) {
          
        })
       .catch(function (error) {
        console.log(error);
         });
      }
    }
  }
</script>

<route lang="yaml">
meta:
  layout: auth
</route>