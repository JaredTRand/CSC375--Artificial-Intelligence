import numpy as np
import time

class Node:
    def __init__(self, name, data):
        self.name = name
        self.children = []
        self.parent = []
        self.data = data
        self.end = False

    def data(self):
        return self.data

    def parent(self):
        return self.parent

    def ended(self):
        return self.end

    def new_child(self, name):
        self.children.append(name)


class MyTree:
    level = 0
    level_nodes = []
    n = 0

    def __init__(self, root, goal, possibles):
        self.root = root
        self.goal = goal
        self.possibles = possibles
        self.nodes = {}
        self.rootnode = Node("{}-{}(ROOT)".format(self.level, self.n), root)
        self.level_nodes.append(self.rootnode)

    def generate_child(self, parent, data, doreturn=True):
        possibles = self.possibles

        cur = np.array(parent.data)
        noodle = Node("{}-{}".format(self.level, self.n), 0)  # names the node as the level and child num
        self.n += 1

        ######## MATHS ###############################################
        middle = int(len(cur) / 2) - 1
        boatleft = False
        if cur[middle] == 1:  # checks which side the boat is on
            boatleft = True

        uselessness = np.array([1])

        j = 0
        i = 0
        for i in range(middle+1):
            if boatleft is True:                             # data = [0 1 1], "moves" the 2nd and 3rd to 5th and 6th
                cur[i] = cur[i] - data[j]                    # cur = [3 3 1 0 0 0] This iterates through the first 3 and last 3
                cur[middle+i+1] = cur[middle+i+1] + data[j]  # cur = [3 2 0 0 1 1]
            else:                                            # This counts as moving 1 cannibal in the boat
                cur[i] = cur[i] + data[j]
                cur[middle+i+1] = cur[middle+i+1] - data[j]

            if self.level >= 2:
                uselessness = parent.parent.data
            if cur[i] <= -1 or cur[middle+i] <= -1 \
                    or np.array_equal(uselessness, cur): # checks if the move is illegal or unecessary
                noodle.end = True                        # If it is, it ends the node
                noodle.name = "ENDED"
                self.n -= 1
                break
            j += 1
            if j >= 3:
                j = 0
        ##############################################################

        noodle.data = cur           # Adds data to the new node,
        parent.new_child(noodle)    # Adds new node as child to its parent node
        noodle.parent = parent      # Adds parent to new node

        if cur[0] > 0 and cur[3] > 0:               # Checks if the missonaries is > 0
            if cur[0] < cur[1] or cur[3] < cur[4]:  # Before checking if number of cannibals is greater
                noodle.end = True                   # If the cannibals are greater, it's not a viable option
                noodle.name = "ENDED"
                self.n -= 1

        if doreturn is True:
            return noodle

    # Generates an entire level of nodes based off the previous level's nodes and the amount of possible moves
    def generate_level(self):
        self.level += 1
        self.n = 0
        newlevelnodes = []

        i = 0
        for i in range(len(self.level_nodes)):  # For each node in the level
            if self.level_nodes[i].end is True:  # If the node isn't ended, it makes new children for it
                break                           # otherwise it skips it
            j = 0
            for j in range(len(self.possibles)):    # makes a new child node for each possible move
                node = self.generate_child(self.level_nodes[i], self.possibles[j])

                if node.end is False:
                    newlevelnodes.append(node)

        self.level_nodes = newlevelnodes
        print("GENERATED LEVEL {} ({} NODES)".format(self.level, len(self.level_nodes)))

    # Prints the path of the current node up to the root node
    def print_path(self, currpos):
        print("\n\nPATH:")
        path = []
        for i in range(self.level+1):
            path.insert(0, currpos)
            currpos = currpos.parent

        for i in range(len(path)):
            mcb = path[i].data
            print("\n{}\n"
                  "M {} ||| {}\n"
                  "C {} ||| {}\n"
                  "B {} ||| {}"
                  "".format(path[i].name, mcb[0], mcb[3], mcb[1], mcb[4], mcb[2], mcb[5]))


# finds the solution to the Missionaries and Cannibals problem
def find_solution(mytree, goal):
    this = False
    start = time.time()
    while this is False:
        for i in range(len(mytree.level_nodes)):
            if np.array_equal(mytree.level_nodes[i].data, goal):
                end = time.time()
                print("\n::: SOLUTION FOUND IN {:.2f}s :::\n"
                      "::: NODE {}      :::".format(end-start, mytree.level_nodes[i].name), end='')
                mytree.print_path(mytree.level_nodes[i])

                if input("Find Next Solution?(y/n)") == 'y':
                    start = time.time()
                    break
                else:
                    this = True
                    return mytree.level_nodes[i]

        mytree.generate_level()
        if mytree.level >= 60:    # Just to catch it if it explodes for some reason
            print("\n:: OVERFLOWED :: \nGIVEN INPUTS MOST LIKELY IMPOSSIBLE TO SOLVE\nPLEASE TRY AGAIN")
            print(input("\n:: Press Enter To Exit ::\n") or "")
            quit()                  # Shouldn't happen unless given impossible inputs
