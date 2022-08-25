import machine
import dht
from libs.constants import DHT_SENSOR_PIN, INTERNAL_LED_PIN, LDR_ADC


def setup():
    internal_led = machine.Signal(INTERNAL_LED_PIN, machine.Pin.OUT, invert=True)
    dth_sensor = dht.DHT11(machine.Pin(DHT_SENSOR_PIN))
    ldr_sensor = machine.ADC(LDR_ADC)
    physical_modules = {"internal_led": internal_led, "dth_sensor": dth_sensor, "ldr_sensor": ldr_sensor}
    __set_initial_state(physical_modules)
    return physical_modules


def __set_initial_state(physical_modules):
    internal_led = physical_modules["internal_led"]
    internal_led.off()
