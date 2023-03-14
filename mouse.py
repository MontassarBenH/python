import pyautogui
import time

# set duration to 0.1 to move the cursor quickly
pyautogui.PAUSE = 0.1

# loop indefinitely
while True:
    # move the cursor 1 pixel up
    pyautogui.moveRel(0, -1)
    
    # wait for 5 seconds
    time.sleep(5)
    
    # move the cursor 1 pixel down
    pyautogui.moveRel(0, 1)
    
    # wait for 5 seconds
    time.sleep(5)
