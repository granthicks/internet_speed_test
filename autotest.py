import speedtest
import datetime
from os.path import exists
import csv

# This script will check the current upload and download speed and save
# the results to a csv file called output.csv

# Getting the current time of the speed test
current_time = datetime.datetime.now()

speed = speedtest.Speedtest()

# Testing the download speed and saving to the variable dl_speed
print("Checking download speed...")
dl_speed = float('{:.2f}'.format(speed.download()/1024/1024))

# Testing the upload speed and saving to the variable ul_speed
print("Checking upload speed...")
ul_speed = float('{:.2f}'.format(speed.upload()/1024/1024))

# Printing results to terminal
print(f'The current time is {current_time}')
print(f"Download speed: {dl_speed}Mb/s")
print(f"Upload speed: {ul_speed}Mb/s")

# Creating a list for the new row to print to the output file
new_row = [current_time, dl_speed, ul_speed]

# Saving results to output.csv file, creating it if it does not already exist
file_exist = exists('output.csv')
print(f"Does the file exist? {file_exist}")
if not file_exist:
    print("Creating output file...")
    # Creating header list
    header = ["time", "download_speed", "upload_speed"]
    with open("output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(new_row)
    print("File created!")
else:
    with open("output.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(new_row)
    print("Output list updated!")
