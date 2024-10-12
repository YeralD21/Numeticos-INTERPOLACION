import axios from 'axios';

const API_URL = 'http://localhost:5000';

export const uploadFile = (file) => {
  const formData = new FormData();
  formData.append('file', file);

  return axios.post(`${API_URL}/upload`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
};

export const interpolate = (x, y, method, xi, degree = null) => {
  const data = { x, y, method, xi, degree };
  return axios.post(`${API_URL}/interpolate`, data);
};
