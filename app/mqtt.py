import paho.mqtt.client as mqtt


#destinationQueue=macaddress
def publish(destinationQueue,action):
	mqtt.publish('\\'+ destinationQueue,action) 
