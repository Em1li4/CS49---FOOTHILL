from adafruit_circuitplayground import cp
while True:
    pix_num = int(input("which neopixel turn on? "))
    red = int(input("enter a value for red "))
    green = int(input("enter a value for green "))
    blue = int(input("enter a value for blue "))
    cp.pixels[pix_num] = (red, green, blue)
