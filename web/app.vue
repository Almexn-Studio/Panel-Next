<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated>
    <q-toolbar class="bg-white h-16 text-black">
      <q-btn flat round dense icon="menu" />
      <q-toolbar-title>
        Panel Next
      </q-toolbar-title>
     </q-toolbar>
    </q-header>

     <q-page-container class="px-3">
      <q-page class="py-6">
        <NuxtRouteAnnouncer />
        <NuxtPage />
      </q-page>
     </q-page-container>

   </q-layout>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

</script>

