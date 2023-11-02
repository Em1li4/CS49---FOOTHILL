# This is the code i used to solve the handwashing timer. 
# It lights up all the lights in a lapse of 20 seconds, allowing the user to pick a color for the lights. We are using RGB values for the lights.
# If the user doesn't pick a color in the available range,  a backup color will be selected by default. 
# At the end, it plays the jingle bell song to let the user know the time is done.


from adafruit_circuitplayground import cp
import time

BACKUP_COLOR = (100, 0, 200)

red = int(input("value for red (0-255)"))
green = int(input("value for green (0-255)"))
blue = int(input("value for blue (0-255)"))

if red < 0 or red > 255:
    COLOR = BACKUP_COLOR
elif green < 0 or green > 255:
    COLOR = BACKUP_COLOR
elif blue < 0 or blue > 255:
    COLOR = BACKUP_COLOR
else:
    COLOR = (red, green, blue)

NUM_PIXELS = 10
CANCELCOLOR = (0, 0, 0)

for index in range(NUM_PIXELS):
    cp.pixels[index] = COLOR
    time.sleep(2)

for index in range(NUM_PIXELS):
    cp.pixels[index] = CANCELCOLOR

for hertz in [329.63, 329.63, 329.63, 0, 329.63, 329.63, 329.63, 0, 329.63, 392.00, 523.25, 587.33, 0, 659.26, 0, 698.46, 698.46, 698.46, 698.46, 698.46, 659.26, 659.26, 659.26, 659.26, 587.33, 587.33, 659.26, 587.33, 392.00]:
    cp.play_tone(hertz,0.5)
