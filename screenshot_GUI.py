import pyautogui  # to take screenshot
import time  # to make a delay
import tkinter as tk    # to make GUI
from tkinter.filedialog import *    # to make GUI

root = tk.Tk()  # Creating an instance of Tk initializes this interpreter and creates the root window.
canvas1 = tk.Canvas(root, width=150, height=150)  # define the dimension of the window
canvas1.pack()


def auto_screenshot():  # auto screens function
    root.withdraw()  # hide the window
    save_path = asksaveasfilename()  # take the path form the user and save it in save_path
    time.sleep(2)  # delay for 2 second
    x = 1
    while x < 4:  # to take continuous screens
        pyautogui.screenshot(save_path + str(x) + '.png')  # take the screen for the current screen and save it in
        # the path that the user select
        x += 1
        time.sleep(2)

    root.deiconify()  # to appear the window again after hide from withdraw function


def one_screenshot():
    root.withdraw()  # hide the window
    save_path2 = asksaveasfilename()  # take the path form the user and save it in save_path
    time.sleep(2)  # delay for 2 second
    screen_shot2 = pyautogui.screenshot()  # take a screen shot for current window
    screen_shot2.save(save_path2 + ".png")  # save the screen in the path that the user select
    root.deiconify()  # to appear the window again after hide from withdraw function


# define button1 and its properties
myButton1 = tk.Button(text="auto screenshot", command=auto_screenshot, bg='blue', fg='white', font=5)
canvas1.create_window(75, 50, window=myButton1)
# define button1 and its properties
myButton2 = tk.Button(text="one screenshot", command=one_screenshot, bg='green', fg='white', font=5)
canvas1.create_window(75, 100, window=myButton2)

# infinite loop to continue appear the window for the user
root.mainloop()
