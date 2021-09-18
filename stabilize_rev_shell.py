import pyautogui
import time


def dumb_to_smart():
    lines = input("No. of lines your terminal has: ") #Command to determine number of lines = tput lines
    columns = input("No. of columns your terminal has: ") #Command to determine number of columns = tput cols

    print("[!] Take your cursor to the terminal in which the nc session is running")

    time.sleep(3)

    print("Initializing Script...")

    pyautogui.write("/usr/bin/script -qc /bin/bash /dev/null")
    pyautogui.press("enter")
    time.sleep(1)

    with pyautogui.hold("ctrl"):
        pyautogui.press("z")

    pyautogui.write("stty raw -echo")
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.write("fg")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.write("export TERM=xterm")
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.write(f"stty cols {columns} rows {lines}")
    pyautogui.press("enter")

    exit()

dumb_to_smart()
