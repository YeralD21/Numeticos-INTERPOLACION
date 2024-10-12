from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from models.interpolation_methods import lagrange_interpolation, newton_divided_diff, least_squares_linear, least_squares_polynomial, cubic_spline_interpolation

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No se ha enviado ningún archivo'})
    
    file = request.files['file']
    df = pd.read_excel(file)  # Leer el archivo Excel
    
    # Supongamos que las columnas de interés son las dos primeras
    x = df.iloc[:, 0].values
    y = df.iloc[:, 1].values

    return jsonify({'message': 'Archivo subido correctamente', 'x': x.tolist(), 'y': y.tolist()})

@app.route('/interpolate', methods=['POST'])
def interpolate():
    data = request.get_json()
    x = np.array(data['x'])
    y = np.array(data['y'])
    method = data['method']
    xi = np.array(data['xi'])

    if method == 'lagrange':
        yi = [lagrange_interpolation(x, y, point) for point in xi]
    elif method == 'newton':
        yi = [newton_divided_diff(x, y, point) for point in xi]
    elif method == 'least_squares_linear':
        model = least_squares_linear(x, y)
        yi = model(xi)
    elif method == 'least_squares_polynomial':
        degree = data.get('degree', 2)  # Grado del polinomio (default: 2)
        model = least_squares_polynomial(x, y, degree)
        yi = model(xi)
    elif method == 'spline':
        yi = cubic_spline_interpolation(x, y, xi)
    else:
        return jsonify({'error': 'Método de interpolación no válido'})

    return jsonify({'xi': xi.tolist(), 'yi': yi.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
