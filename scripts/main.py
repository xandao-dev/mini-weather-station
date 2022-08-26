import libs.physical_modules as mods
import libs.env as env
import libs.wifi as wifi
import libs.thingspeak as ts
from libs.constants import LOOP_INTERVAL
from time import sleep


def main():
    physical_modules = mods.setup()
    secrets = env.load("env.json")
    station = wifi.connect(secrets["wifi"]["ssid"], secrets["wifi"]["password"])
    while True:
        if station and station.isconnected():
            reads = mods.read_all_modules(physical_modules)
            print(
                f"Temperature: {reads['temperature']}°C",
                f", Humidity: {reads['humidity']}%",
                f", Rel. Light: {reads['light']}%",
            )
            ts.post(
                secrets["thingspeak"]["write_api_key"],
                field1=reads["temperature"],
                field2=reads["humidity"],
                field3=reads["light"],
            )
            sleep(LOOP_INTERVAL)
        else:
            station = wifi.reconnect(
                secrets["wifi"]["ssid"], secrets["wifi"]["password"], station, physical_modules["internal_led"]
            )


if __name__ == "__main__":
    main()
