# Second GPIO Programming Guide for LED Cube
import RPi.GPIO as GPIO

def main():
    pin_value= input("Please Enter The Pin Number:")
    pin_number = int(pin_value)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_number, GPIO.OUT)
    GPIO.output(pin_number,1)
    key_value = input("press space & enter to finish...")
    GPIO.output(pin_number,0)
    GPIO.cleanup()
    print("Done")

if __name__ == "__main__":main()