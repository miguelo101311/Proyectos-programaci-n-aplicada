from machine import Pin
import time

# Definir los pines donde están conectados los LEDs
# (puedes cambiar estos números según tu conexión en la ESP32)
led_pins = [2, 4, 5, 18, 19, 21, 22, 23]

# Crear lista de objetos Pin
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

while True:
    # Encender los LEDs uno por uno
    for led in leds:
        led.value(1)   # Enciende LED
        time.sleep(0.1)
        led.value(0)   # Apaga LED
    
    