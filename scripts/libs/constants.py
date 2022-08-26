from micropython import const

LOOP_INTERVAL = const(30)  # seconds

DHT_SENSOR_PIN = const(4)  # Pin 4 is D2 on Wemos D1 Mini
INTERNAL_LED_PIN = const(2)  # Pin 2 is D4 on Wemos D1 Mini
LDR_ADC = const(0)  # ADC 0 is A0 on Wemos D1 Mini
