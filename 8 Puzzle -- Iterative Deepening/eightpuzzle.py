from myTree import *
import numpy as np


import random


def apply_action(board, action):

    deltas = np.array([[-1, 0, 1, 0], [0, 1, 0, -1]])
    action_2_index = {'up': 0, 'right': 1, 'down': 2, 'left': 3}
    posx, posy = np.where(np.isin(board, [0]))
    (x, y) = (posx[0], posy[0])
    (new_x, new_y) = (x + deltas[0, action_2_index[action]], y + deltas[1, action_2_index[action]])

    try:
        el = board[new_x, new_y]
        board[x, y] = el
        board[new_x, new_y] = 0
       # print(new_x, new_y)
       # print(board)
    except IndexError:
        pass
    return board


def mess_up(board, actions, moves):

    for iter in range(0, moves):
        board = apply_action(board, actions[random.randint(0, 3)])
    pass

### Impossible Board Checking ###
### Method Found Here: ###
### https://learnbycoding.wordpress.com/2014/12/25/how-to-check-if-an-instance-of-8-puzzle-is-solvable/ ###
def getCount(arr):
    invcount = 0
    i = 0
    while i < 9-1:
        j = i+1
        while j < 9:
            if arr[j] and arr[i] and arr[i] > arr[j]:
                invcount += 1
            j += 1
        i += 1
    return invcount


def makeFlatter(puz):
    bbb = []
    j = 0
    k = 0
    for i in range(9):
        bbb.append(puz[j][k])
        k += 1
        if k > 2:
            k = 0
            j += 1
    return bbb


def checkSolvable(puzzle, goal):
    flatpuz = makeFlatter(puzzle)
    invCount = getCount(flatpuz)
    if invCount % 2 == 0 or not np.array_equal(puzzle, goal):
        return True
    else:
        actions = ["up", "right", "down", "left"]
        mess_up(puzzle, actions, 12)
        return checkSolvable(puzzle, goal)


def main():
    goal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    messupboard = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    board = np.array([[-1, -1, -1, -1, -1], [-1, 1, 2, 3, -1], [-1, 4, 5, 6, -1], [-1, 7, 8, 0, -1], [-1, -1, -1, -1, -1]])
    actions = ["up", "right", "down", "left"]
    mess_up(messupboard, actions, 12)
    checkSolvable(messupboard, goal)
    for i in range(3):
        board[1][i+1] = messupboard[0][i]
        board[2][i+1] = messupboard[1][i]
        board[3][i+1] = messupboard[2][i]

    print("START BOARD:\n{}\n\n".format(messupboard))
    goal = np.array([[-1, -1, -1, -1, -1], [-1, 1, 2, 3, -1], [-1, 4, 5, 6, -1], [-1, 7, 8, 0, -1], [-1, -1, -1, -1, -1]])
    newtree = MyTree(board, goal, possibles=actions)
    return find_solution(newtree, goal)


if __name__ == "__main__":
    main()
