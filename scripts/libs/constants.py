from micropython import const

WIFI_WATCHER_INTERVAL = const(60000)  # milliseconds
LOOP_INTERVAL = const(300)  # seconds
MEM_CLEAN_INTERVAL = const(3600)  # seconds

DHT_SENSOR_PIN = const(4)  # Pin 4 is D2 on Wemos D1 Mini
INTERNAL_LED_PIN = const(2)  # Pin 2 is D4 on Wemos D1 Mini
LDR_ADC = const(0)  # ADC 0 is A0 on Wemos D1 Mini
