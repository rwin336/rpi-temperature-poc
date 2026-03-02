#!/usr/bin/python3

import glob
import time
from prometheus_client import Gauge
from flask import Flask, Response
from prometheus_client import Counter, Gauge, start_http_server, generate_latest

content_type = str('text/plain; version=0.0.4; charset=utf-8')

w1_base_dir = '/sys/bus/w1/devices/'
w1_device_folder = glob.glob(w1_base_dir + '28*')[0]
w1_device_id = w1_device_folder.split('/')[-1]
w1_device_temperature_file = w1_device_folder + '/temperature'

def print_w1_files():
  print(f"{w1_base_dir}")
  print(f"{w1_device_folder}")
  print(f"{w1_device_temperature_file}")

def read_temp(temp_file):
  temp_c = 0
  temp_f = 0
  with open(temp_file, 'r') as file:
    first_line = file.readline().strip()
    temp_c = int(first_line) / 1000
  temp_f = (temp_c * 1.8) + 32 
  return {"celcius": temp_c, "fahrenheit": temp_f}


app = Flask(__name__)


PROBE_TEMPERATURE_C = Gauge('current_temperature_c',
                       'the current probe temperature in Celcius.')

PROBE_TEMPERATURE_F = Gauge('current_temerature_f',
                       'the current probe temperature in Fahrenheit.')


@app.route('/metrics')
def metrics():
    metrics = read_temp(w1_device_temperature_file)
    PROBE_TEMPERATURE_C.set(metrics['celcius'])
    PROBE_TEMPERATURE_F.set(metrics['fahrenheit'])
    return Response(generate_latest(), mimetype=content_type)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

