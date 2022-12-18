import time
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController
import keyboard as keyInput
import PIL.ImageGrab

keyboard = Controller()
mouse = MouseController()

pause_button = "-"
unpause_button = "+"

cyanColor = (70, 202, 210)
option1 = 0
option2 = 40


def main():
    x = 100
    y = 0
    while True:
        if keyInput.is_pressed(pause_button):
            y = pause(y)
        rgb = PIL.ImageGrab.grab().load()[1280, 1155]
        if rgb != cyanColor:
            work(x, y)


def pause(y):
    while True:
        if keyInput.is_pressed(unpause_button):
            return y
        if keyInput.is_pressed("/"):
            return option1
        if keyInput.is_pressed("*"):
            return option2


def work(x, y):
    keyboard.press(Key.alt)
    time.sleep(0.1)
    mouse.press(Button.right)
    time.sleep(0.05)
    mouse.release(Button.right)
    time.sleep(0.1)
    mouse.move(x, y)  # 100, 40
    time.sleep(0.1)
    mouse.click(Button.left, 1)
    time.sleep(0.1)
    keyboard.release(Key.alt)
    time.sleep(1)


if __name__ == '__main__':
    time.sleep(1)
    print("Starting!")
    main()
