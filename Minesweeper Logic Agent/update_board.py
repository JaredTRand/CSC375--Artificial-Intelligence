import pyautogui
from time import sleep


def update(tiles, board, holder, gameLocX, gameLocY):
    # smile, blank, one, two, three, four, empty
    # [scanXStart, scanYStart] = [gameLocX - 90, gameLocY + 20]  # scan over the game board
    # [scanXEnd, scanYEnd] = [scanXStart + 220, scanYStart + 270]
    scanXStart = board[0][0].left - 5
    scanYStart = board[0][0].top - 10
    scanXEnd = board[len(board)-2][len(board[0])-1].left + board[len(board)-2][len(board[0])-1].width + 5
    scanYEnd = board[len(board)-2][len(board[0])-1].top + board[len(board)-2][len(board[0])-1].height + 10

    ones = list(pyautogui.locateAllOnScreen(tiles[2], grayscale=False, region=(scanXStart, scanYStart, scanXEnd, scanYEnd)))
    twos = list(pyautogui.locateAllOnScreen(tiles[3], grayscale=False, region=(scanXStart, scanYStart, scanXEnd, scanYEnd)))
    threes = list(pyautogui.locateAllOnScreen(tiles[4], grayscale=False, region=(scanXStart, scanYStart, scanXEnd, scanYEnd)))
    fours = list(pyautogui.locateAllOnScreen(tiles[5], grayscale=False, region=(scanXStart, scanYStart, scanXEnd, scanYEnd)))
    emptys = list(pyautogui.locateAllOnScreen(tiles[6], grayscale=True, region=(scanXStart, scanYStart, scanXEnd, scanYEnd)))
    flagged = list(pyautogui.locateAllOnScreen(tiles[7], grayscale=True, region=(scanXStart, scanYStart, scanXEnd, scanYEnd)))
    bombs = list(pyautogui.locateAllOnScreen(tiles[8], grayscale=True, region=(scanXStart, scanYStart, scanXEnd, scanYEnd)))

    # Wow It's a Real Mess In Here, isnt it?
    if len(bombs) > 0:
        print("OH NO I MESSED UP (˃ω˂)")
        quit()
    for i in range(len(emptys)):
        s = str(emptys[i].left-1) + str(emptys[i].top-1)
        holder[s].type = 'empty'
        holder[s].likelihood = -1
    for i in range(len(flagged)):
        s = str(flagged[i].left-1) + str(flagged[i].top-1)
        holder[s].type = 'flagged'
        holder[s].likelihood = 100
    for i in range(len(ones)):
        s = str(ones[i].left-1) + str(ones[i].top-1)
        holder[s].type = 'one'
        holder[s].likelihood = -1

        count = 0
        keepaneyeon = []
        for j in range(len(holder[s].surroundings[0])):
            if holder[s].surroundings[0][j] != None and holder[s].surroundings[0][j].type == 'blank':
                count += 1
                keepaneyeon.append(holder[s].surroundings[0][j])
            if holder[s].surroundings[0][j] != None and holder[s].surroundings[0][j].type == 'flagged':
                count += 1
                keepaneyeon.append(holder[s].surroundings[0][j])
        if len(keepaneyeon) == 1:
            for j in range(len(keepaneyeon)):
                if keepaneyeon[j].flagged != True:
                    keepaneyeon[j].flagged = True
                    pyautogui.rightClick(x=keepaneyeon[j].left + 10, y=keepaneyeon[j].top + 10)
                    for k in range(len(keepaneyeon[j].surroundings[0])):
                        if keepaneyeon[j].surroundings[0][k] is None:
                            continue
                        if keepaneyeon[j].surroundings[0][k].type == 'blank' or keepaneyeon[j].surroundings[0][k].type == 'empty':
                            continue
                        elif keepaneyeon[j].surroundings[0][k].type == 'one' or \
                                keepaneyeon[j].surroundings[0][k].type == 'two' or \
                                keepaneyeon[j].surroundings[0][k].type == 'three' or \
                                keepaneyeon[j].surroundings[0][k].type == 'four':
                            pyautogui.click(x=keepaneyeon[j].surroundings[0][k].left + 10, y=keepaneyeon[j].surroundings[0][k].top + 10)
    for i in range(len(twos)):
        s = str(twos[i].left-1) + str(twos[i].top-1)
        holder[s].type = 'two'
        holder[s].likelihood = -1
        count = 0
        keepaneyeon = []
        for j in range(len(holder[s].surroundings[0])):
            if holder[s].surroundings[0][j] != None and holder[s].surroundings[0][j].type == 'blank':
                count += 1
                keepaneyeon.append(holder[s].surroundings[0][j])
            if holder[s].surroundings[0][j] != None and holder[s].surroundings[0][j].type == 'flagged':
                count += 1
                keepaneyeon.append(holder[s].surroundings[0][j])
        if len(keepaneyeon) == 2:
            for j in range(len(keepaneyeon)):
                if keepaneyeon[j].flagged != True:
                    keepaneyeon[j].flagged = True
                    pyautogui.rightClick(x=keepaneyeon[j].left + 10, y=keepaneyeon[j].top + 10)
                    for k in range(len(keepaneyeon[j].surroundings[0])):
                        if keepaneyeon[j].surroundings[0][k] is None:
                            continue
                        if keepaneyeon[j].surroundings[0][k].type == 'blank' or keepaneyeon[j].surroundings[0][k].type == 'empty':
                            continue
                        elif keepaneyeon[j].surroundings[0][k].type == 'one' or \
                                keepaneyeon[j].surroundings[0][k].type == 'two' or \
                                keepaneyeon[j].surroundings[0][k].type == 'three' or \
                                keepaneyeon[j].surroundings[0][k].type == 'four':
                            pyautogui.click(x=keepaneyeon[j].surroundings[0][k].left + 10,
                                            y=keepaneyeon[j].surroundings[0][k].top + 10)
    for i in range(len(threes)):
        s = str(threes[i].left-1) + str(threes[i].top-1)
        holder[s].type = 'three'
        holder[s].likelihood = -1
        count = 0
        keepaneyeon = []
        for j in range(len(holder[s].surroundings[0])):
            if holder[s].surroundings[0][j] != None and holder[s].surroundings[0][j].type == 'blank':
                count += 1
                keepaneyeon.append(holder[s].surroundings[0][j])
            if holder[s].surroundings[0][j] != None and holder[s].surroundings[0][j].type == 'flagged':
                count += 1
                keepaneyeon.append(holder[s].surroundings[0][j])
        if len(keepaneyeon) == 3:
            for j in range(len(keepaneyeon)):
                if keepaneyeon[j].flagged != True:
                    keepaneyeon[j].flagged = True
                    pyautogui.rightClick(x=keepaneyeon[j].left + 10, y=keepaneyeon[j].top + 10)
                    for k in range(len(keepaneyeon[j].surroundings[0])):
                        if keepaneyeon[j].surroundings[0][k] is None:
                            continue
                        if keepaneyeon[j].surroundings[0][k].type == 'blank' or keepaneyeon[j].surroundings[0][k].type == 'empty':
                            continue
                        elif keepaneyeon[j].surroundings[0][k].type == 'one' or \
                                keepaneyeon[j].surroundings[0][k].type == 'two' or \
                                keepaneyeon[j].surroundings[0][k].type == 'three' or \
                                keepaneyeon[j].surroundings[0][k].type == 'four':
                            pyautogui.click(x=keepaneyeon[j].surroundings[0][k].left + 10,
                                            y=keepaneyeon[j].surroundings[0][k].top + 10)
    for i in range(len(fours)):
        s = str(fours[i].left-1) + str(fours[i].top-1)
        holder[s].type = 'four'
        holder[s].likelihood = -1
        count = 0
        keepaneyeon = []
        for j in range(len(holder[s].surroundings[0])):
            if holder[s].surroundings[0][j] != None and holder[s].surroundings[0][j].type == 'blank':
                count += 1
                keepaneyeon.append(holder[s].surroundings[0][j])
            if holder[s].surroundings[0][j] != None and holder[s].surroundings[0][j].type == 'flagged':
                count += 1
                keepaneyeon.append(holder[s].surroundings[0][j])
        if len(keepaneyeon) == 4:
            for j in range(len(keepaneyeon)):
                if keepaneyeon[j].flagged != True:
                    keepaneyeon[j].flagged = True
                    pyautogui.rightClick(x=keepaneyeon[j].left + 10, y=keepaneyeon[j].top + 10)
                    for k in range(len(keepaneyeon[j].surroundings[0])):
                        if keepaneyeon[j].surroundings[0][k] is None:
                            continue
                        if keepaneyeon[j].surroundings[0][k].type == 'blank' or 'empty':
                            continue
                        elif keepaneyeon[j].surroundings[0][k].type == 'one' or 'two' or 'three' or 'four':
                            pyautogui.click(x=keepaneyeon[j].surroundings[0][k].left + 10,
                                            y=keepaneyeon[j].surroundings[0][k].top + 10)


   # for i in range(len(board)):
   #     for j in range(len(board[i])):
   #         print("{} ".format(board[i][j].type), end="")
   #     print("")




    return holder

def getleastlikely(blanks, holder):
    s = str(blanks[0].left) + str(blanks[0].top)
    leastlikely = holder[s]
    found = False
    for i in range(len(blanks) - 1):
        sss = str(blanks[i + 1].left) + str(blanks[i + 1].top)
        newone = holder[sss]
        for j in range(len(newone.surroundings)):
            test = newone.surroundings[0][j]
            if test == None:
                break
            test = newone.surroundings[0][j].type
            b = newone.surroundings[0][j]
            if test == 'one' and b not in newone.added:
                newone.likelihood += 1
                newone.added.append(b)
            elif test == 'two' and b not in newone.added:
                newone.likelihood += 2
                newone.added.append(b)
            elif test == 'three' and b not in newone.added:
                newone.likelihood += 3
                newone.added.append(b)
            elif test == 'four' and b not in newone.added:
                newone.likelihood += 4
                newone.added.append(b)
        if leastlikely.flagged == True:
            continue
        if found == False and newone.likelihood > 0:
            leastlikely = newone
            found = True
        elif newone.likelihood > 0 and newone.likelihood < leastlikely.likelihood:
            leastlikely = newone
    return leastlikely
