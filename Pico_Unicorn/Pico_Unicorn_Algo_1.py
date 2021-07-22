# Pico Unicorn Algo 1
# Date 19.07.2021
# Author @ Rohit Jain
# Email: rohit.jain.324@gmail.com

import picounicorn, utime, urandom

x_lim = 15
y_lim = 6

x_adj = 1
y_adj = 1

def main():
    
    picounicorn.init()

    red = [[0,0],[0,1],[0,2],[0,3],[0,4]]
    green = [[1,10],[2,10],[3,10],[4,10],[5,10]]
    blue = [[5,11],[5,12],[5,13],[5,14],[5,15]]

    while true:
        if picounicorn.is_pressed(picounicorn.BUTTON_A):
            x_adj = 1
        if picounicorn.is_pressed(picounicorn.BUTTON_B):
            x_adj = -1
        if picounicorn.is_pressed(picounicorn.BUTTON_X):
            y_adj = 1
        if picounicorn.is_pressed(picounicorn.BUTTON_Y):
            y_adj = -1
            


if __name__ == "__main__": main()