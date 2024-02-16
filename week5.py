import sys 
import time
import board
import csv
import adafruit_bme680

print(sys.argv)
start_time = time.time()
run_time = 300
run_time = int(sys.argv[1])

filename = "data_week5.csv"
filename = sys.argv[2]
file = open(filename, "w", newline='')
writer = csv.writer(file)

meta_data = ["Time", "Temperature", "Gas", "Humidity", "Pressure", "Altitude", "PM1.0", "PM2.5", "PM10"]
writer.writerow(meta_data)

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

temperature_offset = -5

#Week 4 imports 
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)
reset_pin = None
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)
aqdata = pm25.read()

data_list = []
now = time.time()
while (now-start_time) < run_time:
    time.sleep(1)
    now = time.time()
    data_list = [now, (bme680.temperature + temperature_offset), bme680.gas, bme680.relative_humidity, bme680.pressure, bme680.altitude, aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"]]
    writer.writerow(data_list)