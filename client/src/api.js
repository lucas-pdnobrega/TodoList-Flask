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

  createTask(task) {
    return apiClient.post('/tasks', task);
  },

  updateTask(title) {
    return apiClient.put(`/task?title=${title}`)
  },

  deleteTask(title) {
    return apiClient.delete(`task?title=${title}`)
  }

  // Add other methods as per your API endpoints
};
