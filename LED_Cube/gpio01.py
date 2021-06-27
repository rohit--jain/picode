# First GPIO Programming Guide for GPIO
import RPi.GPIO as GPIO
from time import sleep

GRID = [7,11,35,37,12,13,31,33,15,16,23,29,18,19,21,22]
LAYER = [40,38,36,32]

def main():
    
    GPIO.setmode(GPIO.BOARD)

    key = input("Testing Each LED. Press Any Key To Continue...")
    for i in range(0,15):
        GPIO.output(GRID[i],True)
        sleep(1)
        print("Starting LED on Pin Number: "+ str(GRID[i]))
        GPIO.output(GRID[i],False)
        sleep(1)
    
    key = input("Now testing Layers. Press Any Key To Continue...")
    for i in range (0,3):
        GPIO.output(LAYER[i],True)
        sleep(2)
        print("Starting LAYER on Pin Number: "+ str(LAYER[i]))
        GPIO.output(LAYER[i],False)
        sleep(1)
    print("Testing Complete")



if __name__ == "__main__":main()