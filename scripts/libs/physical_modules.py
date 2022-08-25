import machine
import dht
from libs.constants import DHT_SENSOR_PIN


def setup():
    dth_sensor = dht.DHT11(machine.Pin(DHT_SENSOR_PIN))
    physical_modules = {"dthSensor": dth_sensor}
    return physical_modules
