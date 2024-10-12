from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Ruta para subir archivos (modificada para aceptar CSV)
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No se ha enviado ningún archivo'})
    
    file = request.files['file']
    filename = file.filename

    # Identifica si el archivo es CSV o Excel
    if filename.endswith('.csv'):
        # Lee el archivo CSV
        df = pd.read_csv(file)
    elif filename.endswith('.xlsx') or filename.endswith('.xls'):
        # Lee el archivo Excel
        df = pd.read_excel(file)
    else:
        return jsonify({'error': 'Formato de archivo no soportado. Sube un archivo CSV o Excel.'})

    # Supongamos que las columnas de interés son las dos primeras
    x = df['CodigoPeriodoComercial'].values
    y = df['M_Total'].values

    return jsonify({'message': 'Archivo subido correctamente', 'x': x.tolist(), 'y': y.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
