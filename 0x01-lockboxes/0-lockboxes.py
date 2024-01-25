#!/usr/bin/python3
'''determines if all the boxes can be opened'''


def canUnlockAll(boxes):
    '''Return True if all boxes can be opened, else return False'''

    pos = 0
    unlocked = {}
    for b in boxes:
        if(len(b) == 0 or pos == 0):
            unlocked[pos] = "always unlocked"
        for key in b:
            if key < len(boxes) and key != pos:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        pos += 1
    return False
