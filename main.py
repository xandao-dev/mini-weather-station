import time
import machine
import dht

dthSensor = dht.DHT11(machine.Pin(4)) # Pin 4 is D2 on Wemos D1 Mini
lightRelay = machine.Pin(2, machine.Pin.OUT) # Pin 2 is D4 on Wemos D1 Mini

lightRelay.off()
isLightOn = False

while True:
	dthSensor.measure()
	print(f"Temperature: {dthSensor.temperature()}°C, Humidity: {dthSensor.humidity()}%")
	
	isProbablyDay = dthSensor.temperature() > 23 and dthSensor.humidity() > 40
	if isProbablyDay and not isLightOn:
		isLightOn = True
		lightRelay.on()
	elif not isProbablyDay and isLightOn:
		isLightOn = False
		lightRelay.off()

	time.sleep(2)