from dht import DHT11
from time import sleep
from machine import Pin, ADC, Signal
from libs.constants import DHT_SENSOR_PIN, INTERNAL_LED_PIN, LDR_ADC
from libs.utils import int_or_none

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
    light = ldr_sensor.read()
    light_percentage = (light / 1024) * 100
    return light_percentage


def read_all_modules(physical_modules):
    dht_sensor = physical_modules["dth_sensor"]
    ldr_sensor = physical_modules["ldr_sensor"]
    dht_sensor.measure()  # min 2 seconds between measurements
    temperature = int_or_none(dht_sensor.temperature())
    humidity = int_or_none(dht_sensor.humidity())
    light = int_or_none(read_light(ldr_sensor))
    reads = {
        "temperature": temperature,
        "humidity": humidity,
        "light": light
    }
    return reads