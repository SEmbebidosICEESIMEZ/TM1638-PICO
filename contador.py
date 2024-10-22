import tm1638
from machine import Pin
from utime import sleep

tm = tm1638.TM1638(stb=Pin(13), clk=Pin(14), dio=Pin(15))

counter = 0

while True:
    tm.number(counter)
    counter += 1
    sleep(1)
