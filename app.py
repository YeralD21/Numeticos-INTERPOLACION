from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from scipy.optimize import curve_fit
from scipy.interpolate import CubicSpline

app = Flask(__name__)

# Métodos de integración e interpolación
def metodo_trapecios(x, y):
    n = len(x)
    area = 0.0
    for i in range(1, n):
        area += (x[i] - x[i-1]) * (y[i] + y[i-1]) / 2.0
    return area

def metodo_simpson(x, y):
    if len(x) % 2 == 0:
        x = x[:-1]
        y = y[:-1]
    
    n = len(x) - 1
    h = (x[-1] - x[0]) / n
    suma = y[0] + y[-1]

    for i in range(1, n, 2):
        suma += 4 * y[i]
    for i in range(2, n-1, 2):
        suma += 2 * y[i]

    return (h / 3) * suma

def log_regression(x, y):
    def model(x, a, b):
        return a + b * np.log(x)
    
    params, _ = curve_fit(model, x[x > 0], y[x > 0])
    return params, model

def metodo_regresion_polinomica(x, y, grado=3):
    # Ajustar un polinomio de grado n
    coeficientes = np.polyfit(x, y, grado)
    polinomio = np.poly1d(coeficientes)
    return polinomio, coeficientes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    method = request.form['method']  # Obtener el método seleccionado

    if file:
        # Leer el archivo Excel con las columnas 'X' (Consumo) y 'Y' (Importe)
        df = pd.read_excel(file)

        # Asumimos que las columnas son 'X' para Consumo y 'Y' para Importe
        x = df['X'].values  # Consumo en KWh
        y = df['Y'].values  # Importe en S/

        # Elegir el método de integración o interpolación
        if method == 'trapecios':
            area = metodo_trapecios(x, y)
        elif method == 'simpson':
            try:
                area = metodo_simpson(x, y)
            except ValueError as e:
                return jsonify({'error': str(e)})
        elif method == 'logaritmica':
            # Realizar la regresión logarítmica
            params, model = log_regression(x, y)
            a, b = params
            area = f'Regresión Logarítmica: y = {a:.4f} + {b:.4f} * log(x)'

            # Generar la curva de ajuste
            x_fit = np.linspace(min(x), max(x), 1000)
            y_fit = model(x_fit, a, b)
        elif method == 'regresion_polinomica':
            # Aplicar la regresión polinómica
            polinomio, coeficientes = metodo_regresion_polinomica(x, y, grado=3)

            # Generar la curva de ajuste
            x_fit = np.linspace(min(x), max(x), 1000)
            y_fit = polinomio(x_fit)

            # Devolver la fórmula del polinomio
            area = f'Polinomio: {np.poly1d(coeficientes)}'
        else:
            return jsonify({'error': 'Método no reconocido'})

        # Crear una gráfica
        plt.figure(figsize=(10,6))
        plt.plot(x, y, label='Datos Originales', color='blue')
        
        if method in ['logaritmica', 'regresion_polinomica']:
            plt.plot(x_fit, y_fit, label=f'{method.replace("_", " ").title()}', color='red')

        plt.fill_between(x, y, color='skyblue', alpha=0.4)
        plt.title(f'Relación entre Consumo y Importe ({method.capitalize()})')
        plt.xlabel('Consumo (KWh)')
        plt.ylabel('Importe (S/)')
        plt.legend()

        # Guardar la imagen en formato base64 para enviarla al frontend
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')

        # Responder con los resultados
        return jsonify({
            'area': area,  # Para este caso, area devolverá la fórmula del polinomio ajustado o el valor del área
            'plot': plot_url
        })


if __name__ == '__main__':
    app.run(debug=True)
