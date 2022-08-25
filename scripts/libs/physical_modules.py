from dht import DHT11
from time import sleep
from machine import Pin, ADC, Signal
from libs.utils import intOrNone
from libs.constants import DHT_SENSOR_PIN, INTERNAL_LED_PIN, LDR_ADC


def setup():
    internal_led = Signal(INTERNAL_LED_PIN, Pin.OUT, invert=True)
    dth_sensor = DHT11(Pin(DHT_SENSOR_PIN))
    ldr_sensor = ADC(LDR_ADC)
    physical_modules = {"internal_led": internal_led, "dth_sensor": dth_sensor, "ldr_sensor": ldr_sensor}
    __set_initial_state(physical_modules)
    return physical_modules


def __set_initial_state(physical_modules):
    internal_led = physical_modules["internal_led"]
    internal_led.off()


def blink(led, times=1, delay=0.5):
    for _ in range(times):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)


def read_light(ldr_sensor):
    light = intOrNone(ldr_sensor.read())
    light_percentage = intOrNone((light / 1024) * 100)
    return light_percentage
