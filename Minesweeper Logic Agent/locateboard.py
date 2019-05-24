import pyautogui
from time import sleep


def get_blanks(smile, blank):
    isonscreen = None
    i = 0
    while isonscreen == None:   # makes sure the board is on the main screen
        isonscreen = pyautogui.locateOnScreen(smile, grayscale=False, confidence=.5)
        i += 1
        if i > 1:
            print("\nBoard Not Found -- Please Bring Into View")
        if i > 10:
            print("\nCould Not Find Board -- Aborting...")
            sleep(3)
            quit()
        sleep(3)

    [gameLocX, gameLocY, _, _] = pyautogui.locateOnScreen(smile, grayscale=False, confidence=.5)

   # [scanXStart, scanYStart] = [gameLocX - 90, gameLocY + 20]  # scan over the game board
   # [scanXEnd, scanYEnd] = [scanXStart + 220, scanYStart + 270]
    # unnecessary for first scan? ie: get larger boards without effort.
    Blanks = pyautogui.locateAllOnScreen(blank, grayscale=True)
    squares = list(Blanks)
    return squares
