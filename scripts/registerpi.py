import paho.mqtt.client as mqtt
import subprocess

# register.py script 
#1.Connect to the broker on the common 'register' topic
#2.Publish a new pi message with the mac address
#3.Subsequent communication will take place through a new topic=macaddress

# print result code on connecting to the broker, subscribe 

RELAY_PIN=14

def on_connect(client, userdata, rc):
    	print("Connected with result code "+str(rc))
        # reconnect then subscriptions will be renewed.
    	macaddress = open('/sys/class/net/eth0/address').read()
	register(str(macaddress))
	client.subscribe(str(macaddress))

#Process the message 
#If msg=turnon, turnon the water pump
#If msg=turnoff, turnoff the water pump 
def on_message(client, userdata, msg):
		if(msg.payload=='ON'):
			print(msg.topic+" "+str(msg.payload))
			subprocess.call(['gpio','export',RELAY_PIN,'out'])
		elif(msg.payload=='OFF')
			print(msg.topic+" "str(msg.payload))
			subprocess.call(['gpio','export',RELAY_PIN,'in'])
		
# Notify the broker that a new pi wants to connect
# First time communicate through the common topic 'register'
def register(macaddress)
	mqtt.publish("register/",macaddress)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect("test.mosquitto.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

