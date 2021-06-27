# Second GPIO Programming Guide for LED Cube
import RPi.GPIO as GPIO
from time import sleep

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7,True)
    sleep(1)
    GPIO.output(7,False)
    GPIO.cleanup()
    print("Done")
    
if __name__ == "__main":main()