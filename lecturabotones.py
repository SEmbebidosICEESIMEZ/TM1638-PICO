import tm1638
from machine import Pin
from utime import sleep

tm = tm1638.TM1638(stb=Pin(13), clk=Pin(14), dio=Pin(15))

while True:
    pressed = tm.keys()  # Leer los botones
    for i in range(8):
        if ((pressed >> i) & 1):
            tm.number(i + 1)  # Mostrar el número del botón presionado
    sleep(0.1)

