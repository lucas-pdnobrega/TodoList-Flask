<script setup>
import { RouterLink, RouterView } from 'vue-router'
import main from './assets/main.css'
import Task from './components/Task.vue'
import TaskList from './components/TaskList.vue';
</script>

<template>
  <div id="app">
    <TaskList />
  </div>
</template>