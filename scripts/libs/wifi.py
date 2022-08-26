from network import WLAN, STA_IF
from time import sleep
from machine import reset
from libs.physical_modules import blink
from libs.constants import WIFI_CONNECT_INTERVAL, WIFI_RECONNECT_INTERVAL, WIFI_MAX_CONNECT_ATTEMPTS, WIFI_MAX_RECONNECT_ATTEMPTS

def connect(ssid, password):
    attempts = 0
    station = WLAN(STA_IF)
    if not station.isconnected():
        print(f"Selected network, SSID: {ssid}")
        station.active(True)
        station.connect(ssid, password)

        print("Connecting...", end="")
        while not station.isconnected() and attempts < WIFI_MAX_CONNECT_ATTEMPTS:
            print(".", end="")
            attempts += 1
            sleep(WIFI_CONNECT_INTERVAL)
        print("")
    if station.isconnected():
        print("Network connected, config: ", station.ifconfig())
        return station
    print("Could not connect to network")
    station.active(False)
    return station


def reconnect(ssid, password, station, led):
    attempts = 0
    while not station.isconnected():
        if attempts >= WIFI_MAX_RECONNECT_ATTEMPTS:
            print("Could not reconnect to WiFi, restarting...")
            reset()
        print("Wifi connection lost, trying to reconnect...")
        blink(led, 5)
        station = connect(ssid, password)
        attempts += 1
        sleep(WIFI_RECONNECT_INTERVAL)

    return station