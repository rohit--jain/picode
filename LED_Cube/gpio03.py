# Test GPIO 3

from time import sleep
import RPi.GPIO as GPIO

def main():
    
    leds = {
        "bottom":[[7,11,35,37],[12,13,31,33],[15,16,23,29],[18,19,21,22]],
        "layers":[40,38,36,32]
    }
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    
    for x in leds["bottom"]:
            for y in x:
                GPIO.setup(y, GPIO.OUT)
                GPIO.output(y, True)
                sleep(0.5)
    for z in leds["layers"]:
        GPIO.setup(z, GPIO.OUT)
        GPIO.output(z, True)
    
    key_value = input("Press [ENTER] Key to Finish...")
    GPIO.cleanup()