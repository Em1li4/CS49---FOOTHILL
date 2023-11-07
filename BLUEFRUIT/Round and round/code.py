from adafruit_circuitplayground import cp
import time

COLOR = (0, 0, 255)

index = 0
cp.pixels[index] = COLOR
while True:
    if cp.button_a and cp.button_b:
        cp.play_tone(440, 2)
    elif cp.button_a:
        remainder = index % 10
        cp.pixels[remainder] = 0
        index += 1
        remainder = index % 10
        cp.pixels[remainder] = COLOR
    elif cp.button_b:
        remainder = index % 10
        cp.pixels[remainder] = 0
        index -= 1
        remainder = index % 10
        cp.pixels[remainder] = COLOR
    time.sleep(.25)











