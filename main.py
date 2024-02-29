import pyautogui, pygetwindow, time, random, sys, os, datetime, json, zipfile, requests, ctypes, string, subprocess
import pyscreeze
from pynput.keyboard import Key, Controller
from pynput import mouse
import keyboard

mouse_controller = mouse.Controller()

# RICHPRINT
keyboard_pynput = Controller()


def click_some_img(path):
    tb_1_btn = pyautogui.locateOnScreen(path,confidence=0.81)
    if not tb_1_btn == None:
        pyautogui.moveTo(tb_1_btn)
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()
        print("done")
    else:
        print("Not found on screen please make sure UI is visible")

def on_key_press(event):
    # print(event)
    if "end down" in str(event): #num1 without numlock
        print("ROB Key")
        click_some_img('images\\rob.PNG')
    elif "page down down" in str(event): #num3 without numlock
        print("Repair Key")
        click_some_img('images\\repair.PNG')
    elif "down down" in str(event): #num2 without numlock
        print("Respawn1 Key")
        click_some_img('images\\respawn1.PNG')



keyboard.on_press(on_key_press)

while True:
    time.sleep(0.1)