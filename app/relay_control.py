import subprocess

class Relay:
	@staticmethod	
	def turnOn(pinNumber):
		subprocess.call(['gpio','export',str(pinNumber),'out'])
		
	@staticmethod	
	def turnOff(pinNumber):
		subprocess.call(['gpio','export',str(pinNumber),'in'])
		
