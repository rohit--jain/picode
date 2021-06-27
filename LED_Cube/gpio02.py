# Second GPIO Programming Guide for LED Cube
import RPi.GPIO as GPIO

def main():
    grid_value= input("Please Enter The Pin Number: \n[7,11,35,37,12,13,31,33,15,16,23,29,18,19,21,22]:")
    layer_value= input("Please Enter The Layer Number [40,38,36,32]: ")
    grid_number = int(grid_value)
    layer_number = int(layer_value)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(grid_number, GPIO.OUT)
    GPIO.setup(layer_number, GPIO.OUT)
    GPIO.output(layer_number,1)
    GPIO.output(grid_number,1)
    key_value = input("press space & enter to finish...")
    GPIO.output(grid_number,0)
    GPIO.output(layer_number,0)
    GPIO.cleanup()
    print("Done")

if __name__ == "__main__":main()