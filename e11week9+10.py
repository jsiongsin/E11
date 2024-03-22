# setup an event trigger for detecting a pulse using the GPIO pin on the raspberry pi:
import sys
import csv
import time
import RPi.GPIO as GPIO

now = time.time()
start_time = time.time()
run_time = int(sys.argv[1])
interval = int(sys.argv[2])
filename = sys.argv[3]
file = open(filename,'w',newline='')
writer = csv.writer(file)

df = ["Time","Counts"]
writer.writerow(df)
pulse_count = 0

# Setup 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Callback function to increment count
def pulse_detected(self):
    global pulse_count
    pulse_count += 1
    print(time.time())

# Add event detect for counting pulses
GPIO.add_event_detect(17, GPIO.FALLING, callback=pulse_detected)

# Count number of pulses in the last interval
data = []
try:
    while (now-start_time) < run_time:
        now = time.time()
        time.sleep(interval)
        print(f'Pulses detected in the last {interval} sec: {pulse_count}')
        data = [now,pulse_count]
        writer.writerow(data)
        pulse_count = 0
finally:
    GPIO.cleanup()

