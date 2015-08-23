import paho.mqtt.client as mqtt

# register.py script 
#1.Connect to the broker on the common 'register' topic
#2.Subscribe to that topic and publish a new pi message
#3.Process the subsequent message and write the new topic name to file

# print result code on connecting to the broker, subscribe 
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
    client.subscribe("register/")

#Process the message and write the new assigned topic name to file 
def on_message(client, userdata, msg):
	if(str(msg.payload).startswith("newtopic")):
		file=open('topicname.txt','w')
		file.write(msg.payload)
        	print(msg.topic+" "+str(msg.payload))
	
# Notify the broker that a new pi wants to connect
# Registration
def register()
	mqtt.publish("register/","newpi")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect("test.mosquitto.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

