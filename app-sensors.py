from flask import Flask, jsonify

import Adafruit_BMP.BMP085 as BMP085
import Adafruit_DHT

sensor_bmp = BMP085.BMP085()

app = Flask(__name__)


@app.route('/api/pressure')
def get_pressure():
    pressure = sensor_bmp.read_pressure() / 100
    return jsonify({
        'sensor': 'BMP180',
        'unit': 'hPa',
        'pressure': round(pressure, 2)
    })


@app.route('/api/temperature')
def get_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
    return jsonify({
        'sensor': 'DHT22',
        'unit': 'Celsius',
        'temperature': round(temperature, 2)
    })


@app.route('/api/humidity')
def get_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
    return jsonify({
        'sensor': 'DHT22',
        'unit': 'Percent',
        'humidity': round(humidity, 2)
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
