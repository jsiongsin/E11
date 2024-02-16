import sys 
import random
import time
import csv

start_time = time.time()
run_time = 30

filename = "data.csv"
file = open(filename, "w", newline='')
writer = csv.writer(file)

meta_data = ["Time", "Data"]
writer.writerow(meta_data)

now = time.time()
while (now-start_time) < run_time:
    time.sleep(1)
    data = random.random()
    now = time.time()
    data_list = [now, data]
    writer.writerow(data_list)