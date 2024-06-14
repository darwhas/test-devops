from flask import Flask, render_template, request
import os
import requests



app = Flask(__name__)

@app.route('/')
def index():
    ciudades = ["Bogotá", "Miami", "Londres", "Tokio"]
    return render_template('index.html', ciudades=ciudades)

@app.route('/comparacion', methods=['POST'])
def comparacion():
    ciudad_1 = request.form['ciudad_1']
    ciudad_2 = request.form['ciudad_2']
    ciudad_3 = request.form['ciudad_3']

    latitud_1, longitud_1 = obtener_coordenadas(ciudad_1)
    latitud_2, longitud_2 = obtener_coordenadas(ciudad_2)
    latitud_3, longitud_3 = obtener_coordenadas(ciudad_3)

    temperatura_1 = obtener_temperatura(latitud_1, longitud_1)
    temperatura_2 = obtener_temperatura(latitud_2, longitud_2)
    temperatura_3 = obtener_temperatura(latitud_3, longitud_3)

    return render_template('comparacion.html', ciudad_1=ciudad_1, ciudad_2=ciudad_2, ciudad_3=ciudad_3, temperatura_1=temperatura_1, temperatura_2=temperatura_2, temperatura_3=temperatura_3 )

def obtener_coordenadas(ciudad):
    # Aquí podrías utilizar un servicio de geocodificación para obtener las coordenadas
    # Por simplicidad, este ejemplo simplemente devuelve valores fijos para las coordenadas
    if ciudad == "Bogotá":
        return (4.71, -74.07)  # Latitud y longitud de Bogotá, Colombia
    elif ciudad == "Miami":
        return (25.76, -80.19)  # Latitud y longitud de Miami, Florida, EE. UU.
    elif ciudad == "Londres":
        return (51.51, -0.13)  # Latitud y longitud de Londres, Reino Unido
    elif ciudad == "Tokio":
        return (35.68, 139.76)  # Latitud y longitud de Tokio, Japón

def obtener_temperatura(latitud, longitud):
    api_key ="7a956e62d611cbb09f14f717f62d88bb"
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitud}&lon={longitud}&appid={api_key}&units=metric"
    respuesta = requests.get(url)
    datos = respuesta.json()
    temperatura_actual = datos["current"]["temp"]
    return temperatura_actual

if __name__ == '__main__':
    app.run(debug=True)