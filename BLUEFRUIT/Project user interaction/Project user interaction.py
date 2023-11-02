//This is the code that I used to make my user interaction. The language is Python and I used MU as a code editor.
//It allows the user to interact with the program, by allowing the user to select what color wants to be displayed and in which neopixel.
//The values for the color run in a RGB scale.
//It allows the user to light up different neopixels and different colors each time.

from adafruit_circuitplayground import cp
while True:
    pix_num = int(input("which neopixel turn on? "))
    red = int(input("enter a value for red "))
    green = int(input("enter a value for green "))
    blue = int(input("enter a value for blue "))
    cp.pixels[pix_num] = (red, green, blue)
