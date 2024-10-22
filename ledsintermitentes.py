import tm1638
from machine import Pin
from utime import sleep

tm = tm1638.TM1638(stb=Pin(13), clk=Pin(14), dio=Pin(15))

while True:
    # Encender LEDs de izquierda a derecha
    for i in range(8):
        tm.led(i, True)
        sleep(0.2)
    # Apagar LEDs de derecha a izquierda
    for i in range(7, -1, -1):
        tm.led(i, False)
        sleep(0.2)
