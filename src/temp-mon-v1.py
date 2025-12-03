#!/usr/bin/env python3
import glob
import time

w1_base_dir = '/sys/bus/w1/devices/'
w1_device_folder = glob.glob(w1_base_dir + '28*')[0]
w1_device_temperature_file = w1_device_folder + '/temperature'
scrape_rate_secs = 5
duration_secs = 30

def print_w1_files():
  print(f"{w1_base_dir}")
  print(f"{w1_device_folder}")
  print(f"{w1_device_temperature_file}")

def mon_temp_v1(temp_file, scrape_rate, duration_secs):
  print(f"Using temperature file:        {temp_file}")
  print(f"Temperature scrape rate:       {scrape_rate} seconds")
  print(f"Temperature monitor Duration:  {duration_secs} seconds")

  start_time = time.time()
  num_temperature_readings = 0
  while time.time() - start_time < duration_secs:
    print("Current temp: xx")
    num_temperature_readings += 1
    time.sleep(scrape_rate)

  print(f"Temperature monitor complete: Total temperature readings: {num_temperature_readings}")


mon_temp_v1(w1_device_temperature_file, scrape_rate_secs, duration_secs)
