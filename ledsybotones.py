import tm1638
from machine import Pin
from utime import sleep

tm = tm1638.TM1638(stb=Pin(13), clk=Pin(14), dio=Pin(15))

while True:
    pressed = tm.keys()  # Leer botones presionados
    for i in range(8):
        if ((pressed >> i) & 1):
            tm.led(i, True)  # Encender el LED correspondiente
        else:
            tm.led(i, False)  # Apagar el LED si no está presionado
    sleep(0.1)

