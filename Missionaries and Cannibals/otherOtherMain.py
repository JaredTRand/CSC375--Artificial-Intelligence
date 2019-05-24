import numpy as nump
import pdb
from newTree import *


def breadth_search():
    ################ SETTING VALUES ####################################################################################
    m = 3   # missionaries
    c = 3   # cannibals
    b = 2   # boat capacity
    print("MISSIONARIES AND CANNIBALS")
    if input("Use Default Values? (y/n) ") == 'n':
        m = int(input("Number of Missionaries(Default = 3): ") or 3)
        c = int(input("Number of Cannibals(Default = 3): ") or 3)
        b = int(input("Boat Capacity(Default = 2): ") or 2)
        print("M: {}   C: {}   B: {} \n".format(m, c, b))
    if b < 2:
        b = 2
        print("\n  Boat Cannot Have Capacity Smaller Than Two >:(\n  Default Applied, Capacity = {}\n".format(b))

    possible = nump.array([[0, 1, 1], [1, 0, 1], [1, 1, 1], [0, 2, 1], [2, 0, 1]])

    if b > 2:
        holder = []
        i = 3
        while i < b+1:
            holder.append(i)
            possible = nump.append(possible, [[0, i, 1], [i, 0, 1]], axis=0)
            if i % 2 == 0:
                possible = nump.append(possible, [[int(i/2), int(i/2), 1]], axis=0)
            i += 1
        j = len(holder)

        for p in range(j):
            x = holder[p]
            k = 1
            while k < int(j):
                x = x - 1
                y = k
                k += 1
                possible = nump.append(possible, [[x, y, 1], [y, x, 1]], axis=0)

        x = len(possible)   # This stuff is for removing repeat move sets
        i = 0
        while i < x-1:
            temp = possible[i]
            x = len(possible)
            k = 0
            while k < x-1:
                if (possible[k] == temp).all() and i != k:
                    possible = nump.delete(possible, k, 0)
                    x -= 1
                k += 1
            i += 1

    print("Possible Moves:\n {} \n".format(possible))
    ####################################################################################################################

                   # LEFTSIDE ||| RIGHTSIDE
    node = nump.array([m, c, 1,  0, 0, 0])
    goal = nump.array([0, 0, 0,  m, c, 1])

    mytree = MyTree(node, goal, possibles=possible)

    find_solution(mytree, goal)


breadth_search()
