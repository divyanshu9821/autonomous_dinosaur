# Auto Dinosaur

This is created, when i was exploring internet for something fun, that day i found a python library "pyautogui" that can perform keyboard function but this project need much more than a library. :)<br>

It uses two python libraries "pyautogui" and "PIL" (pillow).<br>
* "pyautogui" perfroms keyboard functions like jump or duck.<br>
* "PIL" is image library that is capturing screen.

This python program runs in background when google chrome dinosaur game window is in focus and performs function like jump automatically.

## Instructions:

1. open google chrome and write '__chrome://dino__', this opens dino game.

1. adjust the ranges in your program:-
    1. uncomment the __draw()__ function and comment rest of the functions (because we only need this function now to adjust the range).

    1. enter ranges in __draw()__ blindly but not more than monitor's resolution.

    1. run the program (it will show the screen shot with a  black spot on it according to range you have entered).

    1. perform 2.2 and 2.3 step until you get the black spot on desired pixels (basically black spot should appear just after the dinosour, when the tree or bird hit that spot our dino jumps).~~phew!~~

1. Now enter these ranges in that accquire through __draw()__ function in __dark_obstacle()__ and __white_obstacle()__ function.

1. comment __draw()__ function and uncomment all other function.

1. make sure that __check_background()__ function also has range that must be differ from range acquired (because this will only check the background in game because after some time the background of game dark and obstacles become light)

1. now you can beat your friend's highscore without touching the keyboard.

## Few things to note:-
* donot resize the chrome windows because program still look the same spot on screen and after resizing or shifting that spot does not hit by tree or bird

* you cannot do anything on your computer for now. 

* to stop this program move your mouse pointer to the top right corner of your screen.
