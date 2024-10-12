import React, { useState } from 'react';
import { uploadFile } from '../services/api';

const FileUpload = ({ onUploadSuccess }) => {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    try {
      const response = await uploadFile(file);
      onUploadSuccess(response.data.x, response.data.y);
    } catch (error) {
      console.error('Error al subir el archivo:', error);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Subir archivo</button>
    </div>
  );
};

export default FileUpload;
