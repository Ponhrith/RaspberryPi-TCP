import RPi.GPIO as GPIO
import time
from datetime import datetime
from gpiozero import LED
import socket
import Adafruit_DHT

HOST = "172.16.0.160"
PORT = 1060
addr = (HOST, PORT)
max_size = 1024
FORMAT = "utf-8"

RelayPin = 27
Sensor = 4
DHTsensor = Adafruit_DHT.DHT11
pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RelayPin,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(Sensor,GPIO.IN)

print("Starting the client at: ", datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)
print("Client connected to the server at: ", datetime.now())


def command():
    for i in range(0, 5):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        time.sleep(1)
        humidity, temperature = Adafruit_DHT.read_retry(DHTsensor, pin)
        if humidity is not None and temperature is not None:
            humidityDetect = 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity)
            print(humidityDetect)
            with open("/home/pi/Documents/Report.txt", "a") as f:
                f.write(humidityDetect)
        else:
            print('Failed to retrieve data from sensor')
        if GPIO.input(Sensor) == 1:
            detect = "\nWater Detected  " + str(current_time)
            GPIO.output(RelayPin,GPIO.LOW)
            print(detect)
            with open("/home/pi/Documents/Report.txt", "a") as f:
                f.write(detect)
        elif GPIO.input(Sensor) == 0:
            not_detected = "\nWater Not Detected " + str(current_time)
            print(not_detected)
            with open("/home/pi/Documents/Report.txt", "a") as f:
                f.write(not_detected)
            GPIO.output(RelayPin,GPIO.HIGH)
    GPIO.cleanup()

command()

with open("/home/pi/Documents/Report.txt", "rb") as f:
    data = f.read()

client.send("Report.txt".encode(FORMAT))
msg = client.recv(max_size).decode(FORMAT)
print(f"Server: {msg}")

client.send(data)
msg = client.recv(max_size).decode(FORMAT)
print(f"Server: {msg}")

client.close()



