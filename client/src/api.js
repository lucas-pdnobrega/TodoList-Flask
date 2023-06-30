import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:5000',
  // Add any headers or configurations you need
  headers: {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS"
  }
});

export default {
  // Define your API methods here
  getTasks() {
    return apiClient.get('/tasks');
  },

  getTask(title) {
    return apiClient.get(`/task?title=${title}`)
  },

  createTask(title) {
    return apiClient.post('/task', {
      "title" : title,
      "description" : false,
      "due" : false
    });
  },

  updateTask(task) {
    return apiClient.put(`/task?id=${task.id}`, {
      "title" : task.title,
      "description" : task.description,
      "due" : task.due,
      "done" : task.done
    })
  },

  deleteTask(task) {
    return apiClient.delete(`task?id=${task.id}`)
  }

  // Add other methods as per your API endpoints
};
