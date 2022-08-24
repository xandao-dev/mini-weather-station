import machine
import dht
from constants import DHT_SENSOR_PIN, LIGHT_RELAY_PIN


def setup():
    dth_sensor = dht.DHT11(machine.Pin(DHT_SENSOR_PIN))
    light_relay = machine.Pin(LIGHT_RELAY_PIN, machine.Pin.OUT)

    physical_modules = {"dthSensor": dth_sensor, "lightRelay": light_relay}
    return physical_modules
