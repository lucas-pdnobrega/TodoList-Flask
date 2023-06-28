<template>
    <div>
      <h1>Task List</h1>
      <form @submit.prevent="submitForm">
      <input type="text" placeholder="Search.." name="search" v-model="searchTitle">
      <button type="submit">Submit</button>
      </form>
        <div class="tasks-container" v-for="task in tasks" :key="task.id">
            <div class="task-card" key="task.id">
            <h2>{{ task.title }}</h2>
            <p>{{ task.description }}</p>
            <p>{{ task.due }}</p>
            <p>{{ task.done }}</p>
        </div>
        </div>
    </div>
  </template>
  
  <script>
  import api from '../api';
  
  export default {
    data() {
      return {
        tasks: [],
      };
    },
  
    mounted() {
      this.fetchTasks();
    },
  
    methods: {
      fetchTasks() {
        api.getTasks()
          .then(response => {
            this.tasks = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      },
      submitForm() {
        this.fetchTask(this.searchTitle);
        },

      fetchTask(title) {
        api.getTask(title)
          .then(response => {
            this.tasks = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      }
    },
  };
  </script>
  