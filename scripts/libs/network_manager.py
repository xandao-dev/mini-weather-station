import network
import time

def wifi_connect(ssid, password):
    trials = 0
    max_trials = 10
    station = network.WLAN(network.STA_IF)
    if not station.isconnected():
        print("connecting to network", end="")
        station.active(True)
        station.connect(ssid, password)

        while not station.isconnected() and trials < max_trials:
            print(".", end="")
            trials += 1
            time.sleep(1)
        print("")
    if station.isconnected():
        print("network connected, config:", station.ifconfig())
    return station
