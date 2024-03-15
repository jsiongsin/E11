# setup an event trigger for detecting a pulse using the GPIO pin on the raspberry pi:
import time
import RPi.GPIO as GPIO

pulse_count = 0

# Setup 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# # In case the channel is not connected 
# channel = GPIO.wait_for_edge(17, GPIO.FALLING)
# if channel is None:
#     print('Timeout occurred')
# else:
#     print('Edge detected on channel', channel)

# Callback function to increment count
def pulse_detected():
    global pulse_count
    pulse_count += 1
    print(time.time())

# Add event detect for counting pulses
GPIO.add_event_detect(17, GPIO.FALLING, callback=pulse_detected)

# Count number of pulses in the last min 
try:
    while True:
        pulse_count = 0
        time.sleep(60)
        print(f'Pulses detected in the last minute: {pulse_count}')
finally:
    GPIO.cleanup()