import paho.mqtt.client as mqtt
import time
import datetime


import board
import adafruit_dht

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D17)
mqttBroker = "test.mosquitto.org"

client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

while True:
    try:
        timestamp = datetime.datetime.now()
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        payload = f"Temp: {temperature_f} F / {temperature_c} C    Humidity: {humidity}     Time {timestamp}"
        client.publish("Cobanov", payload)
        print(payload)

    except RuntimeError as error:  # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])

    time.sleep(1.0)
