import axios from 'axios';

export const uploadFile = (file) => {
  const formData = new FormData();
  formData.append('file', file);

  return axios.post('http://localhost:5000/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
};

// Añade la función interpolate
export const interpolate = (x, y, method, xi, degree = null) => {
  const data = { x, y, method, xi, degree };
  return axios.post('http://localhost:5000/interpolate', data);
};
