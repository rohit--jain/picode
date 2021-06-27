# First GPIO Programming Guide for GPIO

from gpiozero import LED
from time import sleep

GRID = [7,11,35,37,12,13,31,33,15,16,23,29,18,19,21,22]
LAYER = [40,38,36,32]

def main():
    key = input("Testing Each LED. Press Any Key To Continue...")
    for i in range(0,15):
        led = LED(GRID[i])
        led.on()
        sleep(1)
        print("Starting LED on Pin Number: "+ str(GRID[i]))
        led.off()
        sleep(1)
    key = input("Now testing Layers. Press Any Key To Continue...")
    for i in range (0,3):
        led = LED(LAYER[i])
        led.on()
        sleep(2)
        print("Starting LAYER on Pin Number: "+ str(LAYER[i]))
        led.off()
        sleep(1)
    print("Testing Complete")



if __name__ == "__main__":main()