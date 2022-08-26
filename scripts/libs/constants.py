from micropython import const

LOOP_INTERVAL = const(600)  # seconds
WIFI_CONNECT_INTERVAL = const(1)  # seconds
WIFI_RECONNECT_INTERVAL = const(30)  # seconds
WIFI_MAX_CONNECT_ATTEMPTS = const(30)
WIFI_MAX_RECONNECT_ATTEMPTS = const(10)

DHT_SENSOR_PIN = const(4)  # Pin 4 is D2 on Wemos D1 Mini
INTERNAL_LED_PIN = const(2)  # Pin 2 is D4 on Wemos D1 Mini
LDR_ADC = const(0)  # ADC 0 is A0 on Wemos D1 Mini
