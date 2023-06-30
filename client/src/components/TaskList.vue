<template>
  <div class="container">
    <h1>Task List</h1>
    <form @submit.prevent>
        <div class="input-group mb-3">
          <input type="text" class="form-control" placeholder="Search or insert the task title..." aria-label="Search" aria-describedby="basic-addon2" v-model="searchTitle">
          <div class="input-group-append">
            <button class="btn btn-outline-primary" type="submit" @click="submitForm">Search</button>
            <button class="btn btn-outline-secondary" type="submit" @click="createTask">Create</button>
          </div>
      </div>
    </form>
      <div class="tasks-container">

          <div class="card" style="width: 18rem;" v-for="task in tasks" :key="task.id">

            <div v-if="!task.editing" class="card-body">
              <h5 class="card-title">{{ task.title }}</h5>
              <p class="card-text">{{ task.description }}</p>
              <p class="card-text">{{ task.due }}</p>
              
              <p class="card-text">{{ task.done }}</p>
              <button @click="editTask(task)" type="button" class="btn btn-secondary">Edit</button>
              <button @click="removeTask(task)" type="button" class="btn btn-danger">Remove</button>
            </div>
            
            <div v-else class="card-body">
              <form @submit.prevent="editTask(task)">
                <div class="form-group">
                  <label for="formGroupExampleInput2">Title</label>
                  <input type="text" class="form-control" placeholder="Type your title here.." v-model="task.title">
                </div>
                <div class="form-group">
                  <label for="formGroupExampleInput2">Description</label>
                  <textarea class="form-control" placeholder="Type your description here.." rows="2" v-model="task.description"></textarea>
                </div>
                <div class="form-group">
                  <label for="formGroupExampleInput2">Due</label>
                  <input type="text" class="form-control" placeholder="YYYY/MM/DD" v-model="task.due">
                </div>
                <div class="form-check">
                  <label class="form-check-label" for="checkDone">Done</label>
                  <input type="checkbox" class="form-check-input" id="checkDone" v-model="task.done">
                </div>
                <button @click="editTask(task)" type="button" class="btn btn-secondary">Submit</button>
                <button @click="removeTask(task)" type="button" class="btn btn-danger">Remove</button>
              </form>
            </div>
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
      async createTask() {
        await api.createTask(this.searchTitle)
        .then(this.fetchTasks())
      },
      async fetchTasks() {
        await api.getTasks()
          .then(response => {
            this.tasks = response.data.map(task => ({
            ...task,
            id: task.id,
            editing: false,
            title: task.title,
            description: task.description,
            due: task.due,
            done: task.done,
          }))
          })
          .catch(error => {
            console.error(error);
          });
      },

      async fetchTask(title) {
        await api.getTask(title)
          .then(response => {
            this.tasks = response.data.map(task => ({
              task,
              id: task.id,
              editing: false,
              title: task.title,
              description: task.description,
              due: task.due,
              done: task.done
            }))
          })
          .catch(error => {
            console.error(error);
          });
      },
      async submitForm() {
        if (this.searchTitle) {
          await this.fetchTask(this.searchTitle);
        } else {
          await this.fetchTasks()
        }
        },
      async removeTask(task) {
        await api.deleteTask(task)
        .then(this.fetchTasks())
      },
      async editTask(task) {
        if (task.editing) {
          await api.updateTask(task)
          .then(this.fetchTasks())
          task.editing = false
        } else {
          task.editing = true
        }
        
      }
    },
  };
  </script>
  