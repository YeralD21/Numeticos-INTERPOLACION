import React, { useState } from 'react';
import { uploadFile } from '../services/api';  // Asegúrate de importar la función correcta

const FileUpload = () => {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (file) {
      try {
        const response = await uploadFile(file);  // Llama a la función uploadFile correctamente
        console.log('Respuesta del servidor:', response.data);
      } catch (error) {
        console.error('Error al subir el archivo:', error);
      }
    } else {
      console.log('No se ha seleccionado ningún archivo');
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
