import time
from operator import itemgetter
import network
import machine
import dht


def main():
    physics_modules = initialize_modules()
    connect_to_wifi()
    loop(physics_modules)


def initialize_modules():
    dth_sensor = dht.DHT11(machine.Pin(4))  # Pin 4 is D2 on Wemos D1 Mini
    light_relay = machine.Pin(2, machine.Pin.OUT)  # Pin 2 is D4 on Wemos D1 Mini

    physical_modules = {"dthSensor": dth_sensor, "lightRelay": light_relay}
    return physical_modules


def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('', '')


def loop(physics_modules):
    dht_sensor, light_relay = itemgetter("dht_sensor", "light_relay")(physics_modules)
    isLightOn = False
    while True:
        dht_sensor.measure()  # min 2 seconds between measurements
        print(f"Temperature: {dht_sensor.temperature()}°C, Humidity: {dht_sensor.humidity()}%")

        isProbablyDay = dht_sensor.temperature() > 23 and dht_sensor.humidity() > 40
        if isProbablyDay and not isLightOn:
            isLightOn = True
            light_relay.on()
        elif not isProbablyDay and isLightOn:
            isLightOn = False
            light_relay.off()

        time.sleep(2)


if __name__ == "__main__":
    main()
