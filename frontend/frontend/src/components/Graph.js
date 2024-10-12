import React from 'react';
import { Line } from 'react-chartjs-2';

const Graph = ({ x, y, xi, yi }) => {
  const data = {
    labels: [...x, ...xi],  // Combina x y xi para tener todas las etiquetas
    datasets: [
      {
        label: 'Datos Originales',
        data: y,
        fill: false,
        borderColor: 'blue',
        tension: 0.1,
      },
      {
        label: 'Interpolación',
        data: [...Array(x.length).fill(null), ...yi],
        fill: false,
        borderColor: 'red',
        tension: 0.1,
      },
    ],
  };

  return <Line data={data} />;
};

export default Graph;
