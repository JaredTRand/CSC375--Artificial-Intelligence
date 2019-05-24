import numpy as np
import time


class Node:
    def __init__(self, name, data):
        self.name = name
        self.children = []
        self.parent = []
        self.data = data
        self.end = False

        self.position = self.getPos()  # defaults
        self.left = self.getLeft()
        self.right = self.getRight()
        self.up = self.getUp()
        self.down = self.getDown()

    def new_child(self, name):
        self.children.append(name)

    def getPos(self):
        aa = str(np.where(self.data == 0))
        res = []
        i = 0
        for each in aa:
            if each == '[':
                res.append(int(aa[i + 1]))
            i += 1
        return res

    def swap(self, element):
        mypos = self.getPos()
        aa = str(np.where(self.data == element))
        res = []
        i = 0
        for each in aa:
            if each == '[':
                res.append(int(aa[i + 1]))
            i += 1
        self.data[mypos[0]][mypos[1]] = element
        self.data[res[0]][res[1]] = 0

    def moveUp(self):
        self.swap(self.up)
        self.refreshNeighbors()

    def moveDown(self):
        self.swap(self.down)
        self.refreshNeighbors()

    def moveLeft(self):
        self.swap(self.left)
        self.refreshNeighbors()

    def moveRight(self):
        self.swap(self.right)
        self.refreshNeighbors()

    def getUp(self):
        a = self.position
        return self.data[a[0] - 1][a[1]]

    def getDown(self):
        a = self.position
        return self.data[a[0] + 1][a[1]]

    def getLeft(self):
        a = self.position
        return self.data[a[0]][a[1] - 1]

    def getRight(self):
        a = self.position
        return self.data[a[0]][a[1] + 1]

    def refreshNeighbors(self):
        self.position = self.getPos()
        self.up = self.getUp()
        self.down = self.getDown()
        self.left = self.getLeft()
        self.right = self.getRight()


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
        # mypos = self.rootnode.getPos()
        # self.rootnode.up =
        self.level_nodes.append(self.rootnode)

    def generate_child(self, parent, data, doreturn=True):
        cur = np.array(parent.data)
        noodle = Node("{}-{}".format(self.level, self.n), cur)  # names the node as the level and child num
        self.n += 1

        #############################################################
        if data == "up" and parent.up != -1:
            noodle.moveUp()
        elif data == "down" and parent.down != -1:
            noodle.moveDown()
        elif data == "left" and parent.left != -1:
            noodle.moveLeft()
        elif data == "right" and parent.right != -1:
            noodle.moveRight()
        else:
            noodle.end = True
            noodle.name = "ENDED"
            self.n -= 1
        ##############################################################

        if noodle.name != "ENDED":
            parr = parent
            while parr.name != "0-0(ROOT)":
                if np.array_equal(noodle.data, parr.data):
                    noodle.end = True
                    noodle.name = "ENDED"
                    self.n -= 1
                parr = parr.parent
            parent.new_child(noodle)  # Adds new node as child to its parent node
            noodle.parent = parent  # Adds parent to new node

        if doreturn is True:
            return noodle

    # Generates an entire level of nodes based off the previous level's nodes and the amount of possible moves
    def generate_level(self):
        self.level += 1
        self.n = 0
        newlevelnodes = []

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
            epz = path[i].data
            print("\n"
                  "{}\n"
                  "///////////\n"
                  "// {}|{}|{} //\n"
                  "// {}|{}|{} //\n"
                  "// {}|{}|{} //\n"
                  "///////////".format(path[i].name, epz[1][1], epz[1][2], epz[1][3],
                                      epz[2][1], epz[2][2], epz[2][3],
                                      epz[3][1], epz[3][2], epz[3][3]))


# finds the solution to the Missionaries and Cannibals problem
def find_solution(mytree, goal):
    this = False
    start = time.time()
    while this is False:
        for i in range(len(mytree.level_nodes)):
            if np.array_equal(mytree.level_nodes[i].data, goal):
                end = time.time()
                print("\n"
                      ":::::::::::::::::::::::::::::::::\n"
                      "::: SOLUTION FOUND IN {:.2f}s :::::\n"
                      "::: NODE {}    ::::::::::::::::\n"
                      ":::::::::::::::::::::::::::::::::".format(end-start, mytree.level_nodes[i].name), end='')
                mytree.print_path(mytree.level_nodes[i])

                if input("Find Next Solution?(y/n)") == 'y':
                    start = time.time()
                    break
                else:
                    this = True
                    return mytree.level_nodes[i]

        mytree.generate_level()
        if mytree.level >= 40:    # Just to catch it if it explodes for some reason
            print("\n:: OVERFLOWED :: \n TOO MANY MOVES MADE -- SOMETHING GOOFED UP \nPLEASE TRY AGAIN")
            print(input("\n:: Press Enter To Exit ::\n") or "")
            quit()                  # Shouldn't happen unless given impossible inputs
