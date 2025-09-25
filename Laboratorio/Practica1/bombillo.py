from machine import Pin
import time


led_pins = [2, 4, 5, 18, 19, 21, 22, 23]


leds = [Pin(pin, Pin.OUT) for pin in led_pins]

while True:
    
    for led in leds:
        led.value(1)   # Enciende LED
        time.sleep(0.1)
        led.value(0)   # Apaga LED
    

    
