import pyautogui
import keyboard

with open('script.txt', 'r') as file:
    script = file.read()
    pyautogui.hotkey('alt', 'tab')
    for word in script.split():
        pyautogui.write(word)
        pyautogui.press('enter')
        if keyboard.is_pressed('esc'):
            break
