# Second GPIO Programming Guide for LED Cube
import RPi.GPIO as GPIO
from time import sleep

def main():
    pin_value= input("Please Enter The Pin Number:")
    pin_number = int(pin_value)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_number, GPIO.OUT)
    GPIO.output(pin_number,True)
    key_value = input("press space & enter to finish...")
    GPIO.output(pin_number,False)
    GPIO.cleanup()
    print("Done")

if __name__ == "__main__":main()