import pyautogui  # to take screenshot
import time  # to make a delay
import os  # to save the file in the path

path = ''


def auto_screenshot():  # auto screens function
    # save_path = asksaveasfilename()  # take the path form the user and save it in save_path
    time.sleep(2)  # delay for 2 second
    x = 1
    while x < 4:  # to take continuous screens
        pyautogui.screenshot(os.path.abspath(path) + str(x) + '.png')  # take the screen for the current screen and
        # save it in
        # the path that the user select
        x += 1
        time.sleep(2)


def one_screenshot():
    time.sleep(2)  # delay for 2 second
    screen_shot2 = pyautogui.screenshot()  # take a screen shot for current window
    # save_path2 = asksaveasfilename()  # take the path form the user and save it in save_path
    screen_shot2.save(os.path.abspath(path) + ".png")  # save the screen in the path that the user select


choice = 1
while choice:
    print("--------------choose your option-----------------------")
    print("1- Enter 1 to take one screen shot \n2- Enter 2 to take 3 screenshots continuously every 2 seconds\n"
          "3- Enter 0 to terminate the program")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        path = input('Enter your path: ')
        one_screenshot()
    elif choice == 2:
        path = input('Enter your path: ')
        auto_screenshot()
