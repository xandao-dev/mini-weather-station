import network
import time


def connect(ssid, password):
    trials = 0
    max_trials = 10
    station = network.WLAN(network.STA_IF)
    if not station.isconnected():
        print(f"Selected network, SSID: {ssid}")
        station.active(True)
        station.connect(ssid, password)

        print("Connecting...")
        while not station.isconnected() and trials < max_trials:
            print(".", end="")
            trials += 1
            time.sleep(1)
        print("")
    if station.isconnected():
        print("Network connected, config: ", station.ifconfig())
        return station
    print("Could not connect to network")
    station.active(False)
    return None
