import libs.physical_modules as mods
import libs.env as env
import libs.wifi as wifi
import libs.thingspeak as ts
from libs.utils import int_or_none
from libs.constants import LOOP_INTERVAL, WIFI_RECONNECT_INTERVAL
from time import sleep
from machine import reset


def main():
    physical_modules = mods.setup()
    dht_sensor = physical_modules["dth_sensor"]
    ldr_sensor = physical_modules["ldr_sensor"]
    internal_led = physical_modules["internal_led"]
    secrets = env.load("env.json")
    station = wifi.connect(secrets["wifi"]["ssid"], secrets["wifi"]["password"])
    reconnect_attempts = 0
    reconnect_max_attempts = 10
    while True:
        if station and station.isconnected():
            dht_sensor.measure()  # min 2 seconds between measurements
            temperature = int_or_none(dht_sensor.temperature())
            humidity = int_or_none(dht_sensor.humidity())
            light = int_or_none(mods.read_light(ldr_sensor))
            print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Rel. Light: {light}%")
            ts.post(secrets["thingspeak"]["write_api_key"], field1=temperature, field2=humidity, field3=light)
            sleep(LOOP_INTERVAL)
        else:
            if reconnect_attempts >= reconnect_max_attempts:
                print("Could not reconnect to WiFi, restarting...")
                reset()
            print("Wifi connection lost, trying to reconnect...")
            mods.blink(internal_led, 5)
            station = wifi.connect(secrets["wifi"]["ssid"], secrets["wifi"]["password"])
            reconnect_attempts += 1
            if station and station.isconnected():
                reconnect_attempts = 0
            sleep(WIFI_RECONNECT_INTERVAL)


if __name__ == "__main__":
    main()
