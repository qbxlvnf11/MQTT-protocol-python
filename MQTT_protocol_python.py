# ---- Param ----
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)

parser.add_argument('--host', required=True)
parser.add_argument('--port', type=int, required=True)
parser.add_argument('--topic', required=True)
parser.add_argument('--message', required=True)

args = parser.parse_args()

host = args.host
port = args.port
topic = args.topic
message = args.message

print('host:',host)
print('port:',port)
print('topic:',topic)
print('message:',message)
# ----------------

# ---- Import ----
# Install: pip install paho-mqtt
import paho.mqtt.client as mqtt
import time
import json
# ----------------

# ---- Creating Publisher & Subscriber ----
Subscriber = mqtt.Client('Subscriber')
Publisher = mqtt.Client('Publisher')
# ----------------

# ---- Set Collback Function ----
def on_message(client, userdata, message):
	print('message:',str(message.payload.decode("utf-8")))
	print('message topic:',message.topic)

# Receiving message when publisher sends message to broker
Subscriber.on_message=on_message
# ----------------

# ---- Connecting to Broker ----
Subscriber.connect(host=host, port=port)
print("connecting Subscriber to broker")
Publisher.connect(host=host, port=port)
print("connecting publisher to broker")
# ----------------

# ---- Subscribing ----
Subscriber.loop_start()
Subscriber.subscribe("/"+topic)
print("subscribing...")
# ----------------

# ---- Publishing ----
for i in range(10):
	print('i:',i)
	print("publishing...")
	Publisher.publish("/"+topic, message)
	if i == 5:
		# Stop subscribing
		print('stop subscribing')
		Subscriber.loop_stop()
	time.sleep(2)
# ----------------