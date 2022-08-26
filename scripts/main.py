import libs.physical_modules as mods
import libs.env as env
import libs.wifi as wifi
import libs.thingspeak as ts
from libs.utils import int_or_none
from libs.constants import LOOP_INTERVAL
from time import sleep


def main():
    physical_modules = mods.setup()
    secrets = env.load("env.json")
    station = wifi.connect(secrets["wifi"]["ssid"], secrets["wifi"]["password"])
    loop(station, physical_modules, secrets["thingspeak"]["write_api_key"])


def loop(station, physical_modules, ts_write_api_key):
    dht_sensor = physical_modules["dth_sensor"]
    ldr_sensor = physical_modules["ldr_sensor"]
    internal_led = physical_modules["internal_led"]
    while True:
        wifi.watchdog(station, internal_led)
        dht_sensor.measure()  # min 2 seconds between measurements
        temperature = int_or_none(dht_sensor.temperature())
        humidity = int_or_none(dht_sensor.humidity())
        light = int_or_none(mods.read_light(ldr_sensor))
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Rel. Light: {light}%")
        ts.post(ts_write_api_key, field1=temperature, field2=humidity, field3=light)
        sleep(LOOP_INTERVAL)


if __name__ == "__main__":
    main()
