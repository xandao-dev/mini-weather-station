import time
import urequests
import libs.physical_modules as mods
import libs.wifi as wifi
import libs.env as env


def main():
    physical_modules = mods.setup()
    secrets = env.load("env.json")
    station = wifi.connect(secrets["wifi"]["ssid"], secrets["wifi"]["password"])

    if station.isconnected():
        print("Connected!")
    else:
        print("Disconnected!")
    # response = urequests.get("https://xandao.dev/")
    # print(response.text)
    loop(physical_modules)


def loop(physical_modules):
    dht_sensor = physical_modules["dthSensor"]
    light_relay = physical_modules["lightRelay"]
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
