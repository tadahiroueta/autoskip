from pyautogui import *
from time import sleep
from os import listdir
from os.path import isfile, join

path = './everfi-april/'
imageList = [f for f in listdir(path) if isfile(join(path, f)) and f[-2:] == 'pg']
purple = (197, 29, 86)

def isMouseAtRight():
    currentMouseX, currentMouseY = position()
    if currentMouseX < 200: return True
    return False


def clickOnColor(color):
    s = screenshot()
    for x in range(200, s.width, 5):
        for y in range(0, s.height, 5):
            if s.getpixel((x, y)) == color:
                click(x, y)
                moveTo(1769, 250)
                print("clicking on color")
                return True
    return False


def clickOnImage(image):
    location = locateOnScreen(image, confidence=0.7)
    if location and 200 < location.left:
        centerPosition = center(location)
        click(centerPosition)
        print("clicking on", image)
        return True
    return False


def main():
    sleep(2)
    while True:
        if isMouseAtRight():
            return
        if not clickOnColor(purple):
            for eachImage in imageList:
                if clickOnImage(path + eachImage):
                    break
        sleep(0.5)


if __name__ == '__main__':
    main()
