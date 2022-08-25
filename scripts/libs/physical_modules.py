import dht
from machine import Pin, ADC, Signal
from libs.constants import DHT_SENSOR_PIN, INTERNAL_LED_PIN, LDR_ADC


def setup():
    internal_led = Signal(INTERNAL_LED_PIN, Pin.OUT, invert=True)
    dth_sensor = dht.DHT11(Pin(DHT_SENSOR_PIN))
    ldr_sensor = ADC(LDR_ADC)
    physical_modules = {
        "internal_led": internal_led,
        "dth_sensor": dth_sensor,
        "ldr_sensor": ldr_sensor
    }
    __set_initial_state(physical_modules)
    return physical_modules


def __set_initial_state(physical_modules):
    internal_led = physical_modules["internal_led"]
    internal_led.off()
