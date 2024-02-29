import pyautogui, pygetwindow, time, random, sys, os, datetime, json, zipfile, requests, ctypes, string, subprocess
import pyscreeze
from pynput.keyboard import Key, Controller
from pynput import mouse
import keyboard

mouse_controller = mouse.Controller()

# RICHPRINT
keyboard_pynput = Controller()

def main1():
    tb_1_btn = pyautogui.locateOnScreen('images\\rob.PNG',confidence=0.81)
    if not tb_1_btn == None:
        pyautogui.moveTo(tb_1_btn)
        time.sleep(0.2)
        mouse_controller.click(mouse.Button.left, 2)
        keyboard_pynput.press(Key.enter)
        time.sleep(1)

def on_key_press(event):
    # print(event)
    if "end down" in str(event): #num1 without numlock
        print("ROB Key")
    elif "page down down" in str(event): #num3 without numlock
        print("Repair Key")
    elif "down down" in str(event): #num2 without numlock
        print("Respawn1 Key")


keyboard.on_press(on_key_press)

while True:
    time.sleep(0.1)