# -*- coding:utf-8 -*-

import pygame
import random
import time
from sys import exit
import ctypes

whnd = ctypes.windll.kernel32.GetConsoleWindow()    
if whnd != 0:    
    ctypes.windll.user32.ShowWindow(whnd, 0)    
    ctypes.windll.kernel32.CloseHandle(whnd)
    
def new():
    while True:
        x = random.randint(0,3)
        y = random.randint(0,3)
        if s[x][y]==0:
            s[x][y]=2
            break

def check():
    n1 = [0,1,0,-1]
    n2 = [1,0,-1,0]
    lose = True
    for i in range(4):
        for j in range(4):
            if s[i][j]==0:
                lose = False
                break
    if lose:
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    x = i + n1[k]
                    y = j + n2[k]
                    if x>=0 and y>=0 and x<=3 and y<=3:
                        if s[i][j]==s[x][y]:
                            lose = False
    if lose:
        screen.blit(ilose,(0,0))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        exit()
    
#初始化
s = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
pygame.init()
screen = pygame.display.set_mode((400,400),0,32)
pygame.display.set_caption("2048")

#图片素材
p = {}
p["0"]=pygame.image.load("0.jpg").convert()
p["2"]=pygame.image.load("2.jpg").convert()
p["4"]=pygame.image.load("4.jpg").convert()
p["8"]=pygame.image.load("8.jpg").convert()
p["16"]=pygame.image.load("16.jpg").convert()
p["32"]=pygame.image.load("32.jpg").convert()
p["64"]=pygame.image.load("64.jpg").convert()
p["128"]=pygame.image.load("128.jpg").convert()
p["256"]=pygame.image.load("256.jpg").convert()
p["512"]=pygame.image.load("512.jpg").convert()
p["1024"]=pygame.image.load("1024.jpg").convert()
p["2048"]=pygame.image.load("2048.jpg").convert()
iwin = pygame.image.load("win.jpg").convert()
ilose = pygame.image.load("lose.jpg").convert()

#生成初始数字
a = (random.randint(0,3),random.randint(0,3))
b = a
while b==a:
    b = (random.randint(0,3),random.randint(0,3))
s[a[0]][a[1]] = s[b[0]][b[1]] = 2

while True:

    win = False
    for i in range(4):
        for j in range(4):
            if s[i][j]==2048:
                win = True
            screen.blit(p[str(s[i][j])],(j*100,i*100))

    if win:
        screen.blit(iwin,(0,0))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        exit()
       
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == 273:
                flag = False
                for j in range(4):
                    for i in range(4):
                        if i == 0 or s[i][j]==0:
                            continue
                        t = i-1
                        while s[t][j] == 0:
                            t = t - 1
                            if t == -1:
                                break
                        if t != -1:
                            if s[t][j] == s[i][j]:
                                flag = True
                                s[t][j] = s[t][j]*2
                                s[i][j] = 0
                            else:
                                s[t+1][j] = s[i][j]
                                if t+1!=i:
                                    flag = True
                                    s[i][j] = 0
                        else:
                            flag = True
                            s[0][j] = s[i][j]
                            if i!=0:
                                s[i][j] = 0
                if flag:
                    new()
                else:
                    check()
            elif e.key == 274:
                flag = False
                for j in range(4):
                    for i in range(3,-1,-1):
                        if i == 3:
                            continue
                        t = i+1
                        while s[t][j] == 0:
                            t = t + 1
                            if t == 4:
                                break
                        if t != 4:
                            if s[t][j] == s[i][j]:
                                s[t][j] = s[t][j]*2
                                flag = True
                                s[i][j]=0
                            else:
                                s[t-1][j] = s[i][j]
                                if t-1!=i:
                                    flag = True
                                    s[i][j] = 0
                        else:
                            flag = True
                            s[3][j] = s[i][j]
                            if i!=3:
                                s[i][j] = 0
                if flag:
                    new()
                else:
                    check()
            elif e.key == 275:
                flag = False
                for i in range(4):
                    for j in range(3,-1,-1):
                        if j == 3:
                            continue
                        t = j+1
                        while s[i][t] == 0:
                            t = t + 1
                            if t == 4:
                                break
                        if t != 4:
                            if s[i][t] == s[i][j]:
                                s[i][t] = s[i][t]*2
                                flag = True
                                s[i][j]=0
                            else:
                                s[i][t-1] = s[i][j]
                                if t-1!=j:
                                    flag = True
                                    s[i][j] = 0
                        else:
                            flag = True
                            s[i][3] = s[i][j]
                            if j!=3:
                                s[i][j] = 0
                if flag:
                    new()
                else:
                    check()
            elif e.key == 276:
                flag = False
                for i in range(4):
                    for j in range(4):
                        if j == 0:
                            continue
                        t = j-1
                        while s[i][t] == 0 and t != -1:
                            t = t - 1
                        if s[i][t] == s[i][j] and t != -1:
                            s[i][t] = s[i][t]*2
                            flag = True
                            s[i][j]=0
                        else:
                            s[i][t+1] = s[i][j]
                            if t+1!=j:
                                flag = True
                                s[i][j] = 0
                if flag:
                    new()
                else:
                    check()
    pygame.display.update()
        



