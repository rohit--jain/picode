# First GPIO Programming Guide for LED Cube
import RPi.GPIO as GPIO
from time import sleep

GRID = [7,11,35,37,12,13,31,33,15,16,23,29,18,19,21,22]
LAYER = [40,38,36,32]
VGRID = [37,33,29,22,35,31,23,21,11,13,16,19,7,12,15,18]

def reset(x):
        for i in range(0,15):
                GPIO.output(GRID[i],False)
def resetlayer(x):
        for i in range(0,3):
                GPIO.output(LAYER[i],False)

# Layers
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

# Individual LED
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)



def main():
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    for i in range(0,15):
        GPIO.setup(GRID[i], GPIO.OUT)
    for i in range (0,3):
        GPIO.setup(LAYER[i], GPIO.OUT)

    reset(GRID)
    resetlayer(LAYER)

    key = input("Testing Each LED. Press Any Key To Continue...")
    for i in range(0,15):
        GPIO.output(GRID[i],True)
        sleep(1)
        print("Starting LED on Pin Number: "+ str(GRID[i]))
        GPIO.output(GRID[i],False)
        sleep(1)
    
    reset(GRID)
    resetlayer(LAYER)
    
    key = input("Now testing Layers. Press Any Key To Continue...")
    for i in range (0,3):
        GPIO.output(LAYER[i],True)
        sleep(2)
        print("Starting LAYER on Pin Number: "+ str(LAYER[i]))
        GPIO.output(LAYER[i],False)
        sleep(1)
    
    GPIO.cleanup()
    print("Testing Complete")



if __name__ == "__main__":main()