from network import WLAN, STA_IF
from time import sleep
from machine import reset
from libs.physical_modules import blink

def connect(ssid, password):
    attempts = 0
    max_attempts = 30
    station = WLAN(STA_IF)
    if not station.isconnected():
        print(f"Selected network, SSID: {ssid}")
        station.active(True)
        station.connect(ssid, password)

        print("Connecting...")
        while not station.isconnected() and attempts < max_attempts:
            print(".", end="")
            attempts += 1
            sleep(1)
        print("")
    if station.isconnected():
        print("Network connected, config: ", station.ifconfig())
        return station
    print("Could not connect to network")
    station.active(False)
    return None


def watchdog(station, led):
    if not station.isconnected():
        print("Wifi Disconnected, cleaning and restarting!")
        station.active(False)
        blink(led, 10)
        reset()