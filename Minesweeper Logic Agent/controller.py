from locateboard import *
from square import *
from update_board import *
from play import *


typeofmines = input("What Online Minesweeper Are You Using?\n1. Minesweeper.online\n2. Minesweeperonline.com\n\n")
# smile, blank, one, two, three, four, empty
if typeofmines == 2:
    tiles = ['img/minesweeperonline.com/smile2.png', 'img/minesweeperonline.com/blank.png', 'img/minesweeperonline.com/one.png',
             'img/minesweeperonline.com/two.png', 'img/minesweeperonline.com/three.png', 'img/minesweeperonline.com/four.png',
             'img/minesweeperonline.com/empty.png', 'img/minesweeperonline.com/flag.png', 'img/minesweeperonline.com/bomb.png']
else:
    tiles = ['img/minesweeper.online/smile1.png', 'img/minesweeper.online/blank1.png', 'img/minesweeper.online/one1.png',
             'img/minesweeper.online/two1.png', 'img/minesweeper.online/three1.png', 'img/minesweeper.online/four1.png',
             'img/minesweeper.online/empty1.png', 'img/minesweeper.online/flag.png', 'img/minesweeper.online/bomb.png']

board = get_blanks(tiles[0], tiles[1])
squares = []
for i in range(len(board)):
    me = Square(board[i][0], board[i][1], board[i][2], board[i][3], name='S{}'.format(i + 1))
    squares.append(me)
boardholder = {}

# ## This parts a bit of a mess, but it creates the surroundings################################################
boardss = [[]]
b = []
start = 0
left = squares[0].left
right = 0
for i in range(len(squares)):
    if squares[i].left == left and i != 0:
        boardss.insert(start, b)
        b = []
        start += 1
    b.append(squares[i])
    s = str(squares[i].left) + str(squares[i].top)  # creates a dict of all the squares with the key as their
    boardholder[s] = squares[i]                     # left + top coords (this makes for easier updating)
boardss.insert(start, b)
b = []

for i in range(len(boardss)-2):  # -2 because it creates an empty bottom layer that doesnt matter all that much
    for j in range(len(boardss[i])-1):
        if i > 0: # if not top layer
            if j > 0:
                boardss[i][j].surroundings[0][0] = boardss[i - 1][j - 1]  # topleft
            boardss[i][j].surroundings[0][1] = boardss[i - 1][j]  # top
            if j < len(boardss[i])-1:
                boardss[i][j].surroundings[0][2] = boardss[i - 1][j + 1]  # topright
        if j > 0:
            boardss[i][j].surroundings[0][3] = boardss[i][j - 1]  # left
        if j < len(boardss[i])-1:
            boardss[i][j].surroundings[0][4] = boardss[i][j + 1]  # right
        if i < len(boardss)-2:  # if not bottom layer
            if j > 0:
                boardss[i][j].surroundings[0][5] = boardss[i + 1][j - 1]  # bottomleft
            boardss[i][j].surroundings[0][6] = boardss[i + 1][j]  # bottom
            if j < len(boardss[i])-1:
                boardss[i][j].surroundings[0][7] = boardss[i + 1][j + 1]  # bottomright
#####################################################################

[gameLocX, gameLocY, _, _] = pyautogui.locateOnScreen(tiles[0], grayscale=False, confidence=.5)

# originally (tiles, squares, ... (in case it mattered)
update(tiles, boardss, boardholder, gameLocX, gameLocY)
pyautogui.click(x=squares[0].left + 10, y=squares[0].top + 10)  # Slaps the four corners, opens up a lot of the board
update(tiles, boardss, boardholder, gameLocX, gameLocY)
if boardss[0][len(boardss[0])-1].flagged is False:
    pyautogui.click(x=boardss[0][len(boardss[0])-1].left + 10, y=boardss[0][len(boardss[0])-1].top + 10)
update(tiles, boardss, boardholder, gameLocX, gameLocY)
if boardss[len(boardss)-2][0].flagged is False:
    pyautogui.click(x=boardss[len(boardss)-2][0].left + 10, y=boardss[len(boardss)-2][0].top + 10)
update(tiles, boardss, boardholder, gameLocX, gameLocY)
if boardss[len(boardss)-2][len(boardss[0])-1].flagged is False:
    pyautogui.click(x=boardss[len(boardss)-2][len(boardss[0])-1].left + 10, y=boardss[len(boardss)-2][len(boardss[0])-1].top + 10)
update(tiles, boardss, boardholder, gameLocX, gameLocY)
update(tiles, boardss, boardholder, gameLocX, gameLocY)
play(tiles, boardss, boardholder, gameLocX, gameLocY)
