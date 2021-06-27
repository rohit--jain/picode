# Second GPIO Programming Guide for LED Cube
import RPi.GPIO as GPIO
from time import sleep

def main():
    pin_number= input("Please Enter The Pin Number:")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_number, GPIO.OUT)
    GPIO.output(pin_number,True)
    sleep(1)
    GPIO.output(pin_number,False)
    GPIO.cleanup()
    print("Done")

if __name__ == "__main__":main()