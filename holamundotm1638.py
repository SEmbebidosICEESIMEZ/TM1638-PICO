import tm1638  
from machine import Pin
from utime import sleep

tm = tm1638.TM1638(stb=Pin(13), clk=Pin(14), dio=Pin(15))

while True:
    tm.show('  HELLO  ')
    sleep(1)
    tm.show(' WORLD ')
    sleep(1)

