from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar CORS para manejar las políticas de origen
import pandas as pd

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir solicitudes desde localhost:3000

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No se ha enviado ningún archivo'})

    file = request.files['file']
    filename = file.filename

    # Detecta si el archivo es CSV o Excel
    if filename.endswith('.csv'):
        df = pd.read_csv(file)
    elif filename.endswith('.xlsx') or filename.endswith('.xls'):
        df = pd.read_excel(file)
    else:
        return jsonify({'error': 'Formato de archivo no soportado. Sube un archivo CSV o Excel.'})

    x = df['CodigoPeriodoComercial'].values  # Ajustar los nombres de columna si es necesario
    y = df['M_Total'].values

    return jsonify({'message': 'Archivo subido correctamente', 'x': x.tolist(), 'y': y.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
