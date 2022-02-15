import paho.mqtt.client as mqtt
from datetime import datetime

TOPIC_NAME = "Cobanov"
BROKER_ADDRESS = "test.mosquitto.org"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC_NAME)


def on_message(client, userdata, message):
    publishtime = message.timestamp
    consume_time = datetime.utcnow()
    print(message.topic + " " + str(message.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_ADDRESS, 1883, 60)
client.loop_forever()
