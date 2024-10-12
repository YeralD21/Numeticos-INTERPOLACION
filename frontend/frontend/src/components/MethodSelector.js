import React, { useState } from 'react';
import { interpolate } from '../services/api';

const MethodSelector = ({ x, y }) => {
  const [method, setMethod] = useState('lagrange');
  const [xi, setXi] = useState('');
  const [result, setResult] = useState(null);
  const [degree, setDegree] = useState(2);  // Por defecto para polinomios

  const handleInterpolate = async () => {
    const xiArray = xi.split(',').map(Number);  // Convertir a números
    try {
      const response = await interpolate(x, y, method, xiArray, degree);
      setResult(response.data);
    } catch (error) {
      console.error('Error en la interpolación:', error);
    }
  };

  return (
    <div>
      <select value={method} onChange={(e) => setMethod(e.target.value)}>
        <option value="lagrange">Lagrange</option>
        <option value="newton">Diferencias Divididas de Newton</option>
        <option value="least_squares_linear">Mínimos Cuadrados (Lineal)</option>
        <option value="least_squares_polynomial">Mínimos Cuadrados (Polinomial)</option>
        <option value="spline">Spline Cúbico</option>
      </select>
      {method === 'least_squares_polynomial' && (
        <input
          type="number"
          value={degree}
          onChange={(e) => setDegree(Number(e.target.value))}
          placeholder="Grado del polinomio"
        />
      )}
      <input
        type="text"
        value={xi}
        onChange={(e) => setXi(e.target.value)}
        placeholder="Valores de xi (separados por comas)"
      />
      <button onClick={handleInterpolate}>Interpolar</button>

      {result && (
        <div>
          <h3>Resultados:</h3>
          <p>xi: {result.xi.join(', ')}</p>
          <p>yi: {result.yi.join(', ')}</p>
        </div>
      )}
    </div>
  );
};

export default MethodSelector;
