import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import MethodSelector from './components/MethodSelector';
import Graph from './components/Graph';

function App() {
  const [x, setX] = useState([]);
  const [y, setY] = useState([]);
  const [xi, setXi] = useState([]);
  const [yi, setYi] = useState([]);

  const handleUploadSuccess = (xData, yData) => {
    setX(xData);
    setY(yData);
  };

  const handleInterpolationSuccess = (xiData, yiData) => {
    setXi(xiData);
    setYi(yiData);
  };

  return (
    <div className="App">
      <h1>Software de Interpolación y Ajuste de Curvas</h1>
      <FileUpload onUploadSuccess={handleUploadSuccess} />
      {x.length > 0 && (
        <MethodSelector x={x} y={y} onSuccess={handleInterpolationSuccess} />
      )}
      {xi.length > 0 && yi.length > 0 && (
        <Graph x={x} y={y} xi={xi} yi={yi} />
      )}
    </div>
  );
}

export default App;
