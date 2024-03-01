import pyautogui, time, json, keyboard, pygame
from pynput.keyboard import Key, Controller
from pynput import mouse

pygame.init()
pygame.joystick.init()

mouse_controller = mouse.Controller()


# RICHPRINT
keyboard_pynput = Controller()

with open("config.json","r") as f:
    config = json.load(f)

def click_some_img(path):
    if not path == "":
        try:
            tb_1_btn = pyautogui.locateOnScreen(path,confidence=0.81)
            if not tb_1_btn == None:
                pyautogui.moveTo(tb_1_btn)
                pyautogui.mouseDown()
                time.sleep(0.1)
                pyautogui.mouseUp()
                print("done")
            else:
                print("Not found on screen please make sure UI is visible")
        except Exception as err_n:
            print("Err - maybe Not found on screen try replacing the images with snipping tool")
            print(err_n)

def on_key_press(event):
    if config["debug"]:
        print(event)

    if "end down" in str(event): #num1
        print(config["num1"]["label"] + " init")
        click_some_img(config["num1"]["path"])
    elif "page down down" in str(event): #num3
        print(config["num3"]["label"] + " init")
        click_some_img(config["num3"]["path"])
    elif "down down" in str(event): #num2
        print(config["num3"]["label"] + " init")
        click_some_img(config["num3"]["path"])
    elif "left" in str(event): #num4
        print(config["num4"]["label"] + " init")
        click_some_img(config["num4"]["path"])
    elif "clear" in str(event): #num5
        print(config["num5"]["label"] + " init")
        click_some_img(config["num5"]["path"])
    elif "right" in str(event): #num6
        print(config["num6"]["label"] + " init")
        click_some_img(config["num6"]["path"])



keyboard.on_press(on_key_press)


if config["external_joy"]["use_external_joy"]:
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("No joystick detected.")
        exit()

    joystick = pygame.joystick.Joystick(config["external_joy"]["joystick_nr"])
    joystick.init()

    print(f"Joystick Name: {joystick.get_name()}")
    print(f"Number of Buttons: {joystick.get_numbuttons()}")

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            button_states = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]
            if config["external_joy"]["detect_key_mode"]:
                print("Button States:", button_states)
                time.sleep(0.1) # Optional: Add a delay to avoid excessive printing
            else:
                for button_hotkey_now in config["external_joy"]["key_config"]:
                    if button_states[button_hotkey_now["button"]] == 1: #if button with that number is pressed
                        print(str(button_hotkey_now["label"]) + " init [" + str(button_hotkey_now["button"]) + "]")
                        click_some_img(button_hotkey_now["path"])
    except KeyboardInterrupt:
        pygame.quit()
        print("\nExiting.")
else:
    while True:
        time.sleep(0.1)