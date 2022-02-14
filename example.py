import paho.mqtt.client as mqtt
from random import randrange, uniform
import time


mqttBroker = "test.mosquitto.org"

client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

while True:
    randNumber = uniform(20.0, 21.0)
    payload = f"Temp: {randNumber}"
    client.publish(topic="Cobanov", payload=payload)
    print(payload)
    time.sleep(1)
