import time
import libs.physical_modules as mods
import libs.env as env
import libs.wifi as wifi
import libs.thingspeak as ts
from libs.utils import intOrNone


def main():
    physical_modules = mods.setup()
    secrets = env.load("env.json")
    station = wifi.connect(secrets["wifi"]["ssid"], secrets["wifi"]["password"])

    if station.isconnected():
        loop(physical_modules, secrets["thingspeak"]["write_api_key"])
    else:
        print("Disconnected!")


def loop(physical_modules, ts_write_api_key):
    dht_sensor = physical_modules["dthSensor"]
    while True:
        dht_sensor.measure()  # min 2 seconds between measurements
        temperature = intOrNone(dht_sensor.temperature())
        humidity = intOrNone(dht_sensor.humidity())
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
        ts.post(ts_write_api_key, field1=temperature, field2=humidity)
        time.sleep(30)



if __name__ == "__main__":
    main()
