from locateboard import *
from update_board import *
import pyautogui


def play(tiles, board, boardholder, gameLocX, gameLocY):
    i = 0
    scanXStart = board[0][0].left - 5
    scanYStart = board[0][0].top - 10
    scanXEnd = board[len(board) - 2][len(board[0]) - 1].left + board[len(board) - 2][len(board[0]) - 1].width + 5
    scanYEnd = board[len(board) - 2][len(board[0]) - 1].top + board[len(board) - 2][len(board[0]) - 1].height + 10
    noend = True
    previous = ""
    while noend:
        blanks = list(pyautogui.locateAllOnScreen(tiles[1], grayscale=True, region=(scanXStart, scanYStart, scanXEnd, scanYEnd)))
        holder = update(tiles, board, boardholder, gameLocX, gameLocY)
        bomb = getleastlikely(blanks, holder)

        if previous is bomb:
            blanks.remove(bomb)
            bomb = getleastlikely(blanks, holder)
        previous = bomb
        update(tiles, board, boardholder, gameLocX, gameLocY)
        if bomb.flagged == True:
            continue
        pyautogui.click(x=bomb.left + 10, y=bomb.top + 10)

        i += 1
        if i == 20:
            noend = False
