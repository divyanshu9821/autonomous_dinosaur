'''
    this program mimic the keyboard actions using the library 'pyautogui' and play the game automatically without user.

    start the dinosaurs game by entering 'chrome://dino' in google chrome and 
    firstly set range according to screen using draw function select the pixels to look upon
    then run this program in background
    
 '''
import time # mainly to delay the execution of program
from PIL import ImageGrab # pillow -> image library
import pyautogui # perform keyboard functions

time.sleep(2)

# this function help to identify the place where to put the marker for check
# def draw():
#     image = ImageGrab.grab().convert('L') # take screenshot convert to gray scale
#     data = image.load() # pixel values in terms of 2d matrix
#     for i in range(370,400): # x axis
#         for j in range(440,470): # y axis
#             data[i,j]=0 # 0 means black color
#     image.show() # show the screen shot after putting value 0 in rectangular block


# function to check backgroud because after some time game background change from light to dark or vice versa
def check_background(data): 
    for i in range(360,361): # range must be altered according to monitor 
        for j in range(600,601): # range must be altered according to monitor 
            if data[i,j]>127:
                return 1 #light
            else:
                return 0 #dark
    return            

# when background is light the obstacles like bird and tree appears dark
def dark_obstacle(data):
    for i in range(370,400): # range must be altered according to monitor 
        for j in range(440,470): # range must be altered according to monitor 
            if data[i,j]<100:
                pyautogui.press('up')
                return
    return            

# when background is dark obstacles like bird and trees appears light
def white_obstacle(data):
    for i in range (370,400): # range must be altered according to monitor 
        for j in range(440,470): # range must be altered according to monitor 
            if data[i,j]>=127:
                pyautogui.press('up')
                return  
    return                  

if __name__=="__main__":
    # draw()

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if check_background(data)==1:
            dark_obstacle(data)
        elif check_background(data)==0:
            white_obstacle(data)          
