import paho.mqtt.client as mqtt
import time
from datetime import datetime
import random


mqttBroker = "test.mosquitto.org"
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

while True:
    # payload = str(datetime.utcnow())
    device = "iCobanov"
    timestamp = datetime.utcnow()
    value = random.random()
    payload = "{},{},{}".format(device, timestamp, value)

    client.publish("Cobanov", payload)
    print(payload)
    time.sleep(2.0)
