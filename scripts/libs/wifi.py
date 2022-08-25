from network import WLAN, STA_IF
from time import sleep
from machine import Timer, reset
from libs.constants import WIFI_WATCHER_INTERVAL
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
    def check_connection():
        if not station.isconnected():
            print("WWD: Wifi Disconnected, cleaning and restarting!")
            blink(led, 10)
            clean_then_restart()

    def clean_then_restart():
        watcher.deinit()
        station.active(False)
        reset()

    watcher = Timer(-1)
    watcher.init(period=WIFI_WATCHER_INTERVAL, mode=Timer.PERIODIC, callback=check_connection)
