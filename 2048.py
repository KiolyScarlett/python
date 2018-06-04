# -*- coding: utf-8 -*-
# from collections import defaultdict
import random
import numpy as np

# My_array=[[0 for i in range(4)] for i in range(4)]
# My_Array = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
My_Array = np.zeros((4, 4))
Flag = 1
Score = 0


def notzero(n):
    return int(n) if n != 0 else ''


# game init
def produce_num():
    return 2 if random.randrange(0, 10) > 3 else 4


def AddNewNum():
    while 1:
        k = produce_num()
        s = divmod(random.randrange(0, 16), 4)
        if My_Array[s[0], s[1]] == 0:
            My_Array[s[0], s[1]] = k
            break
    display()


def game_init():
    InitNumFlag = 0
    while 1:
        k = produce_num()
        s = divmod(random.randrange(0, 16), 4)
        if My_Array[s[0], s[1]] == 0:
            My_Array[s[0], s[1]] = k
            InitNumFlag += 1
            if InitNumFlag == 2:
                break


# display
def display():
    print("\r\
┌──┬──┬──┬──┐\n\
│%4s│%4s│%4s│%4s│\n\
├──┬──┬──┬──┤\n\
│%4s│%4s│%4s│%4s│\n\
├──┬──┬──┬──┤\n\
│%4s│%4s│%4s│%4s│\n\
├──┬──┬──┬──┤\n\
│%4s│%4s│%4s│%4s│\n\
└──┴──┴──┴──┘" \
          % (notzero(My_Array[0][0]), notzero(My_Array[0][1]), notzero(My_Array[0][2]), notzero(My_Array[0][3]), \
             notzero(My_Array[1][0]), notzero(My_Array[1][1]), notzero(My_Array[1][2]), notzero(My_Array[1][3]), \
             notzero(My_Array[2][0]), notzero(My_Array[2][1]), notzero(My_Array[2][2]), notzero(My_Array[2][3]), \
             notzero(My_Array[3][0]), notzero(My_Array[3][1]), notzero(My_Array[3][2]), notzero(My_Array[3][3]),)
          )
    print('Score:%s' % Score)


def GameStart():
    global My_Array, Flag, Score
    My_Array = np.zeros((4, 4))
    Flag = 1
    Score = 0
    game_init()
    display()


def check():
    for i in range(3):
        for j in range(3):
            if My_Array[i, j] == 0 or My_Array[i, j] == My_Array[i + 1, j] or My_Array[i, j] == My_Array[i, j + 1]:
                return True
    return False


# 排序，把0放前面
def Sort_D_R(row):
    return sorted(row, key=lambda x: x != 0)


def Sort_U_L(row):
    return sorted(row, key=lambda x: x != 0, reverse=True)


# 合并相同数字
def merge_R(row):
    global Score
    for i in range(3, 0, -1):
        if row[i] != 0:
            if row[i] == row[i - 1]:
                row[i] *= 2
                row[i - 1] = 0
                Score += int(row[i])


def merge_L(row):
    global Score
    for i in range(0, 3, 1):
        if row[i] != 0:
            if row[i] == row[i + 1]:
                row[i] *= 2
                row[i + 1] = 0
                Score += int(row[i])


def moveDown():
    global My_Array
    IsChange = 0
    temp_Array = My_Array.copy()
    for i in range(4):
        temp_Array[:, i] = Sort_D_R(temp_Array[:, i])
        merge_R(temp_Array[:, i])
        temp_Array[:, i] = Sort_D_R(temp_Array[:, i])
        for j in range(4):
            if (My_Array[j, i] != temp_Array[j, i]):
                IsChange += 1
    if IsChange > 0:
        My_Array = temp_Array.copy()
        AddNewNum()


def moveUp():
    global My_Array
    IsChange = 0
    temp_Array = My_Array.copy()
    for i in range(4):
        temp_Array[:, i] = Sort_U_L(temp_Array[:, i])
        merge_L(temp_Array[:, i])
        temp_Array[:, i] = Sort_U_L(temp_Array[:, i])
        for j in range(4):
            if (My_Array[j, i] != temp_Array[j, i]):
                IsChange += 1
    if IsChange > 0:
        My_Array = temp_Array.copy()
        AddNewNum()


def moveLeft():
    global My_Array
    IsChange = 0
    temp_Array = My_Array.copy()
    for i in range(4):
        temp_Array[i] = Sort_U_L(temp_Array[i])
        merge_L(temp_Array[i])
        temp_Array[i] = Sort_U_L(temp_Array[i])
        for j in range(4):
            if (My_Array[i, j] != temp_Array[i, j]):
                IsChange += 1
    if IsChange > 0:
        My_Array = temp_Array.copy()
        AddNewNum()


def moveRight():
    global My_Array
    IsChange = 0
    temp_Array = My_Array.copy()
    for i in range(4):
        temp_Array[i] = Sort_D_R(temp_Array[i])
        merge_R(temp_Array[i])
        temp_Array[i] = Sort_D_R(temp_Array[i])
        for j in range(4):
            if (My_Array[i, j] != temp_Array[i, j]):
                IsChange += 1
    if IsChange > 0:
        My_Array = temp_Array.copy()
        AddNewNum()


def main():
    global Score
    while Flag:
        d = input(' (↑:w) (↓:s) (←:a) (→:d) q(uit) n(newgame):')
        if check():
            if d == 'a':
                moveLeft()
            elif d == 's':
                moveDown()
            elif d == 'w':
                moveUp()
            elif d == 'd':
                moveRight()
            elif d == 'n':
                GameStart()
            elif d == 'q':
                break
            else:
                pass
        else :
            print('Game Over! You Score:%s q(uit) n(newgame):' % Score)
            if d == 'n':
                GameStart()
            elif d == 'q':
                break
            else:
                pass


if __name__ == '__main__':
    main()
