'''
PROGRAMMERS: MOHAMMAD HADI BABALOO & SEPEHR HARFI & AMIR KHOSRO KATIRAEI
TEACHER: MR.VAZIRI
SCHOOL: ALLAME HELLI 1 MIDDLE SCHOOL
'''

from random import *
from math import *
from time import *
import pygame
from pygame.locals import *

pygame.init()
w = 975
h = 650
sc = pygame.display.set_mode((w,h))

#Variables:
fasele = 100 #faseleye beine 2 morabba dar safhe
zel_morabba = 225 #tool zel'e yek vajhe moka'abe rubic
Turn=pygame.mixer.music.load('RubixCube.mp3')


def tabdil(a):
    white =pygame.image.load('White256.png')
    red =pygame.image.load('Red256.png')
    green =pygame.image.load('Green256.png')
    blue =pygame.image.load('Blue256.png')
    orange =pygame.image.load('Orange256.png')
    yellow =pygame.image.load('Yellow256.png')
    if a=='white':
        return white
    if a=='yellow':
        return yellow
    if a=='red':
        return red
    if a=='blue':
        return blue
    if a=='orange':
        return orange
    if a=='green':
        return green

#Menue
def menue():
    f1=0
    f2=1
    f3=1
    a=pygame.image.load('Menue.png')
    b=pygame.image.load('Levels.png')
    c=pygame.image.load('Help.png')
    done=False
    while not done:
        if f1==0:
            sc.blit(a,(0,0))
            pygame.display.flip()
            for e in pygame.event.get():
                if e.type==pygame.MOUSEBUTTONDOWN:
                    (x,y)=pygame.mouse.get_pos()
                    if 235<x<455 and 150<y<225:
                        f2=0
                        f1=1
                    if 170<x<315 and 520<y<585:
                        f1=1
                        f3=0
        if f2==0:
            sc.blit(b,(0,0))
            pygame.display.flip()
            for e in pygame.event.get():
                if e.type==pygame.MOUSEBUTTONDOWN:
                    (x,y)=pygame.mouse.get_pos()
                    if 0<x<65 and 0<y<65:
                        f1=0
                        f2=1
                    if 315<x<625 and 120<y<175:
                        sc.fill((0,0,0))
                        return 15 
                    if 315<x<625 and 275<y<335:
                        sc.fill((0,0,0))
                        return 8
                    if 315<x<470 and 415<y<475:
                        sc.fill((0,0,0))
                        return 3
        if f3==0:
            sc.blit(c,(0,0))
            pygame.display.flip()
            for e in pygame.event.get():
                if e.type==pygame.MOUSEBUTTONDOWN:
                    (x,y)=pygame.mouse.get_pos()
                    if 0<x<60 and 0<y<60:
                        f3=1
                        f1=0

#Random Mode
def random():
    white ='white'
    red ='red'
    green ='green'
    blue ='blue'
    orange ='orange'
    yellow ='yellow'
    #creating Rubic Cube:
    global rubic
    rubic = 54*[0]
    for i in range(0,9):
        rubic[i] = red
    for i in range(9,18):
        rubic[i] = blue
    for i in range(18,27):
        rubic[i] = orange
    for i in range(27,36):
        rubic[i] = green
    for i in range(36,45):
        rubic[i] = white
    for i in range(45,54):
        rubic[i] = yellow
    morabba1=[115,119,100,97]
    for i in range(menue()):
        key=morabba1[randint(0,3)]
        morabba=randint(1,54)
        if key == 119:
            if morabba == 1 or morabba == 4 or morabba == 7:
                a = rubic[42]
                b = rubic[43]
                c = rubic[44]
                rubic[42] = rubic[0]
                rubic[43] = rubic[3]
                rubic[44] = rubic[6]
                rubic[0]  = rubic[47]
                rubic[3]  = rubic[46]
                rubic[6]  = rubic[45]
                rubic[47] = rubic[26]
                rubic[46] = rubic[23]
                rubic[45] = rubic[20]
                rubic[26] = a
                rubic[23] = b
                rubic[20] = c
            if morabba == 2  or morabba == 5 or morabba == 8:
                a = rubic[39]
                b = rubic[40]
                c = rubic[41]
                rubic[39] = rubic[1]
                rubic[40] = rubic[4]
                rubic[41] = rubic[7]
                rubic[1]  = rubic[50]
                rubic[4]  = rubic[49]
                rubic[7]  = rubic[48]
                rubic[50] = rubic[25]
                rubic[49] = rubic[22]
                rubic[48] = rubic[19]
                rubic[25] = a
                rubic[22] = b
                rubic[19] = c
            if morabba == 3  or morabba == 6 or morabba == 9:
                a = rubic[36]
                b = rubic[37]
                c = rubic[38]
                rubic[36] = rubic[2]
                rubic[37] = rubic[5]
                rubic[38] = rubic[8]
                rubic[2]  = rubic[53]
                rubic[5]  = rubic[52]
                rubic[8]  = rubic[51]
                rubic[53] = rubic[24]
                rubic[52] = rubic[21]
                rubic[51] = rubic[18]
                rubic[24] = a
                rubic[21] = b
                rubic[18] = c
            if morabba == 10  or morabba == 13 or morabba == 16:
                a = rubic[44]
                b = rubic[41]
                c = rubic[38]
                rubic[44] = rubic[9]
                rubic[41] = rubic[12]
                rubic[38] = rubic[15]
                rubic[9]  = rubic[53]
                rubic[12] = rubic[50]
                rubic[15] = rubic[47]
                rubic[53] = rubic[35]
                rubic[50] = rubic[32]
                rubic[47] = rubic[29]
                rubic[35] = a
                rubic[32] = b
                rubic[29] = c
            if morabba == 11  or morabba == 14 or morabba == 17:
                a = rubic[43]
                b = rubic[40]
                c = rubic[37]
                rubic[43] = rubic[10]
                rubic[40] = rubic[13]
                rubic[37] = rubic[16]
                rubic[10] = rubic[52]
                rubic[13] = rubic[49]
                rubic[16] = rubic[46]
                rubic[52] = rubic[34]
                rubic[49] = rubic[31]
                rubic[46] = rubic[28]
                rubic[34] = a
                rubic[31] = b
                rubic[28] = c
            if morabba == 12  or morabba == 15 or morabba == 18:
                a = rubic[42]
                b = rubic[39]
                c = rubic[36]
                rubic[42] = rubic[11]
                rubic[39] = rubic[14]
                rubic[36] = rubic[17]
                rubic[11] = rubic[51]
                rubic[14] = rubic[48]
                rubic[17] = rubic[45]
                rubic[51] = rubic[33]
                rubic[48] = rubic[30]
                rubic[45] = rubic[27]
                rubic[33] = a
                rubic[30] = b
                rubic[27] = c
            if morabba == 19  or morabba == 22 or morabba == 25:
                a = rubic[38]
                b = rubic[37]
                c = rubic[36]
                rubic[38] = rubic[18]
                rubic[37] = rubic[21]
                rubic[36] = rubic[24]
                rubic[18] = rubic[51]
                rubic[21] = rubic[52]
                rubic[24] = rubic[53]
                rubic[51] = rubic[8]
                rubic[52] = rubic[5]
                rubic[53] = rubic[2]
                rubic[8]  = a
                rubic[5]  = b
                rubic[2]  = c
            if morabba == 20  or morabba == 23 or morabba == 26:
                a = rubic[41]
                b = rubic[40]
                c = rubic[39]
                rubic[41] = rubic[19]
                rubic[40] = rubic[22]
                rubic[39] = rubic[25]
                rubic[19] = rubic[48]
                rubic[22] = rubic[49]
                rubic[25] = rubic[50]
                rubic[48] = rubic[7]
                rubic[49] = rubic[4]
                rubic[50] = rubic[1]
                rubic[7]  = a
                rubic[4]  = b
                rubic[1]  = c
            if morabba == 21  or morabba == 24 or morabba == 27:
                a = rubic[44]
                b = rubic[43]
                c = rubic[42]
                rubic[44] = rubic[20]
                rubic[43] = rubic[23]
                rubic[42] = rubic[26]
                rubic[20] = rubic[45]
                rubic[23] = rubic[46]
                rubic[26] = rubic[47]
                rubic[45] = rubic[6]
                rubic[46] = rubic[3]
                rubic[47] = rubic[0]
                rubic[6]  = a
                rubic[3]  = b
                rubic[0]  = c
            if morabba == 28  or morabba == 31 or morabba == 34 or morabba == 37 or morabba == 40 or morabba == 43 or morabba == 46 or morabba == 49 or morabba == 52:
                a = rubic[36]
                b = rubic[39]
                c = rubic[42]
                rubic[36] = rubic[27]
                rubic[39] = rubic[30]
                rubic[42] = rubic[33]
                rubic[27] = rubic[45]
                rubic[30] = rubic[48]
                rubic[33] = rubic[51]
                rubic[45] = rubic[17]
                rubic[48] = rubic[14]
                rubic[51] = rubic[11]
                rubic[17] = a
                rubic[14] = b
                rubic[11] = c
            if morabba == 29  or morabba == 32 or morabba == 35 or morabba == 47 or morabba == 50 or morabba == 53 or morabba == 38 or morabba == 41 or morabba == 44:
                a = rubic[37]
                b = rubic[40]
                c = rubic[43]
                rubic[37] = rubic[28]
                rubic[40] = rubic[31]
                rubic[43] = rubic[34]
                rubic[28] = rubic[46]
                rubic[31] = rubic[49]
                rubic[34] = rubic[52]
                rubic[46] = rubic[16]
                rubic[49] = rubic[13]
                rubic[52] = rubic[10]
                rubic[16] = a
                rubic[13] = b
                rubic[10] = c
            if morabba == 30  or morabba == 33 or morabba == 36 or morabba == 48 or morabba == 51 or morabba == 54 or morabba == 39 or morabba == 42 or morabba == 45:
                a = rubic[38]
                b = rubic[41]
                c = rubic[44]
                rubic[38] = rubic[29]
                rubic[41] = rubic[32]
                rubic[44] = rubic[35]
                rubic[29] = rubic[47]
                rubic[32] = rubic[50]
                rubic[35] = rubic[53]
                rubic[47] = rubic[15]
                rubic[50] = rubic[12]
                rubic[53] = rubic[9]
                rubic[15] = a
                rubic[12] = b
                rubic[9]  = c
        if key==97:
                    if morabba == 1 or morabba == 2 or morabba == 3 or morabba == 10 or morabba == 11 or morabba == 12 or morabba == 19 or morabba == 20 or morabba == 21 or morabba == 28 or morabba == 29 or morabba == 30:
                        a = rubic[27]
                        b = rubic[28]
                        c = rubic[29]
                        rubic[27] = rubic[0]
                        rubic[28] = rubic[1]
                        rubic[29] = rubic[2]
                        rubic[0]  = rubic[9]
                        rubic[1]  = rubic[10]
                        rubic[2]  = rubic[11]
                        rubic[9]  = rubic[18]
                        rubic[10] = rubic[19]
                        rubic[11] = rubic[20]
                        rubic[18] = a
                        rubic[19] = b
                        rubic[20] = c
                    if morabba == 4 or morabba == 5 or morabba == 6 or morabba == 13 or morabba == 14 or morabba == 15 or morabba == 22 or morabba == 23 or morabba == 24 or morabba == 31 or morabba == 32 or morabba == 33:
                        a = rubic[30]
                        b = rubic[31]
                        c = rubic[32]
                        rubic[30] = rubic[3]
                        rubic[31] = rubic[4]
                        rubic[32] = rubic[5]
                        rubic[3]  = rubic[12]
                        rubic[4]  = rubic[13]
                        rubic[5]  = rubic[14]
                        rubic[12] = rubic[21]
                        rubic[13] = rubic[22]
                        rubic[14] = rubic[23]
                        rubic[21] = a
                        rubic[22] = b
                        rubic[23] = c
                    if morabba == 7 or morabba == 8 or morabba == 9 or morabba == 16 or morabba == 17 or morabba == 18 or morabba == 25 or morabba == 26 or morabba == 27 or morabba == 34 or morabba == 35 or morabba == 36:
                        a = rubic[33]
                        b = rubic[34]
                        c = rubic[35]
                        rubic[33] = rubic[6]
                        rubic[34] = rubic[7]
                        rubic[35] = rubic[8]
                        rubic[6]  = rubic[15]
                        rubic[7]  = rubic[16]
                        rubic[8]  = rubic[17]
                        rubic[15] = rubic[24]
                        rubic[16] = rubic[25]
                        rubic[17] = rubic[26]
                        rubic[24] = a
                        rubic[25] = b
                        rubic[26] = c
                    if morabba == 37 or morabba == 38 or morabba == 39:
                        a = rubic[36]
                        b = rubic[37]
                        c = rubic[38]
                        rubic[36] = rubic[2]
                        rubic[37] = rubic[5]
                        rubic[38] = rubic[8]
                        rubic[2]  = rubic[53]
                        rubic[5]  = rubic[52]
                        rubic[8]  = rubic[51]
                        rubic[53] = rubic[24]
                        rubic[52] = rubic[21]
                        rubic[51] = rubic[18]
                        rubic[24] = a
                        rubic[21] = b
                        rubic[18] = c
                    if morabba == 40 or morabba == 41 or morabba == 42:
                        a = rubic[39]
                        b = rubic[40]
                        c = rubic[41]
                        rubic[39] = rubic[1]
                        rubic[40] = rubic[4]
                        rubic[41] = rubic[7]
                        rubic[1]  = rubic[50]
                        rubic[4]  = rubic[49]
                        rubic[7]  = rubic[48]
                        rubic[50] = rubic[25]
                        rubic[49] = rubic[22]
                        rubic[48] = rubic[19]
                        rubic[25] = a
                        rubic[22] = b
                        rubic[19] = c
                    if morabba == 43 or morabba == 44 or morabba == 45:
                        a = rubic[42]
                        b = rubic[43]
                        c = rubic[44]
                        rubic[42] = rubic[0]
                        rubic[43] = rubic[3]
                        rubic[44] = rubic[6]
                        rubic[0]  = rubic[47]
                        rubic[3]  = rubic[46]
                        rubic[6]  = rubic[45]
                        rubic[47] = rubic[26]
                        rubic[46] = rubic[23]
                        rubic[45] = rubic[20]
                        rubic[26] = a
                        rubic[23] = b
                        rubic[20] = c
                    if morabba == 46 or morabba == 47 or morabba == 48:
                        a = rubic[44]
                        b = rubic[43]
                        c = rubic[42]
                        rubic[44] = rubic[20]
                        rubic[43] = rubic[23]
                        rubic[42] = rubic[26]
                        rubic[20] = rubic[45]
                        rubic[23] = rubic[46]
                        rubic[26] = rubic[47]
                        rubic[45] = rubic[6]
                        rubic[46] = rubic[3]
                        rubic[47] = rubic[0]
                        rubic[6]  = a
                        rubic[3]  = b
                        rubic[0]  = c
                    if morabba == 49 or morabba == 50 or morabba == 51:
                        a = rubic[41]
                        b = rubic[40]
                        c = rubic[39]
                        rubic[41] = rubic[19]
                        rubic[40] = rubic[22]
                        rubic[39] = rubic[25]
                        rubic[19] = rubic[48]
                        rubic[22] = rubic[49]
                        rubic[25] = rubic[50]
                        rubic[48] = rubic[7]
                        rubic[49] = rubic[4]
                        rubic[50] = rubic[1]
                        rubic[7]  = a
                        rubic[4]  = b
                        rubic[1]  = c
                    if morabba == 52 or morabba == 53 or morabba == 54:
                        a = rubic[38]
                        b = rubic[37]
                        c = rubic[36]
                        rubic[38] = rubic[18]
                        rubic[37] = rubic[21]
                        rubic[36] = rubic[24]
                        rubic[18] = rubic[51]
                        rubic[21] = rubic[52]
                        rubic[24] = rubic[53]
                        rubic[51] = rubic[8]
                        rubic[52] = rubic[5]
                        rubic[53] = rubic[2]
                        rubic[8]  = a
                        rubic[5]  = b
                        rubic[2]  = c




                        
        if key == 115:
                    if morabba == 1 or morabba == 4 or morabba == 7:
                        a = rubic[44]
                        b = rubic[43]
                        c = rubic[42]
                        rubic[44] = rubic[20]
                        rubic[43] = rubic[23]
                        rubic[42] = rubic[26]
                        rubic[20] = rubic[45]
                        rubic[23] = rubic[46]
                        rubic[26] = rubic[47]
                        rubic[45] = rubic[6]
                        rubic[46] = rubic[3]
                        rubic[47] = rubic[0]
                        rubic[6]  = a
                        rubic[3]  = b
                        rubic[0]  = c
                    if morabba == 2 or morabba == 5 or morabba == 8:
                        a = rubic[41]
                        b = rubic[40]
                        c = rubic[39]
                        rubic[41] = rubic[19]
                        rubic[40] = rubic[22]
                        rubic[39] = rubic[25]
                        rubic[19] = rubic[48]
                        rubic[22] = rubic[49]
                        rubic[25] = rubic[50]
                        rubic[48] = rubic[7]
                        rubic[49] = rubic[4]
                        rubic[50] = rubic[1]
                        rubic[7]  = a
                        rubic[4]  = b
                        rubic[1]  = c
                    if morabba == 3 or morabba == 6 or morabba == 9:
                        a = rubic[38]
                        b = rubic[37]
                        c = rubic[36]
                        rubic[38] = rubic[18]
                        rubic[37] = rubic[21]
                        rubic[36] = rubic[24]
                        rubic[18] = rubic[51]
                        rubic[21] = rubic[52]
                        rubic[24] = rubic[53]
                        rubic[51] = rubic[8]
                        rubic[52] = rubic[5]
                        rubic[53] = rubic[2]
                        rubic[8]  = a
                        rubic[5]  = b
                        rubic[2]  = c
                    if morabba == 10 or morabba == 13 or morabba == 16:
                        a = rubic[38]
                        b = rubic[41]
                        c = rubic[44]
                        rubic[38] = rubic[29]
                        rubic[41] = rubic[32]
                        rubic[44] = rubic[35]
                        rubic[29] = rubic[47]
                        rubic[32] = rubic[50]
                        rubic[35] = rubic[53]
                        rubic[47] = rubic[15]
                        rubic[50] = rubic[12]
                        rubic[53] = rubic[9]
                        rubic[15] = a
                        rubic[12] = b
                        rubic[9]  = c
                    if morabba == 11 or morabba == 14 or morabba == 17:
                        a = rubic[37]
                        b = rubic[40]
                        c = rubic[43]
                        rubic[37] = rubic[28]
                        rubic[40] = rubic[31]
                        rubic[43] = rubic[34]
                        rubic[28] = rubic[46]
                        rubic[31] = rubic[49]
                        rubic[34] = rubic[52]
                        rubic[46] = rubic[16]
                        rubic[49] = rubic[13]
                        rubic[52] = rubic[10]
                        rubic[16] = a
                        rubic[13] = b
                        rubic[10] = c
                    if morabba == 12 or morabba == 15 or morabba == 18:
                        a = rubic[36]
                        b = rubic[39]
                        c = rubic[42]
                        rubic[36] = rubic[27]
                        rubic[39] = rubic[30]
                        rubic[42] = rubic[33]
                        rubic[27] = rubic[45]
                        rubic[30] = rubic[48]
                        rubic[33] = rubic[51]
                        rubic[45] = rubic[17]
                        rubic[48] = rubic[14]
                        rubic[51] = rubic[11]
                        rubic[17] = a
                        rubic[14] = b
                        rubic[11] = c
                    if morabba == 19 or morabba == 22 or morabba == 25:
                        a = rubic[36]
                        b = rubic[37]
                        c = rubic[38]
                        rubic[36] = rubic[2]
                        rubic[37] = rubic[5]
                        rubic[38] = rubic[8]
                        rubic[2]  = rubic[53]
                        rubic[5]  = rubic[52]
                        rubic[8]  = rubic[51]
                        rubic[53] = rubic[24]
                        rubic[52] = rubic[21]
                        rubic[51] = rubic[18]
                        rubic[24] = a
                        rubic[21] = b
                        rubic[18] = c
                    if morabba == 20 or morabba == 23 or morabba == 26:
                        a = rubic[39]
                        b = rubic[40]
                        c = rubic[41]
                        rubic[39] = rubic[1]
                        rubic[40] = rubic[4]
                        rubic[41] = rubic[7]
                        rubic[1]  = rubic[50]
                        rubic[4]  = rubic[49]
                        rubic[7]  = rubic[48]
                        rubic[50] = rubic[25]
                        rubic[49] = rubic[22]
                        rubic[48] = rubic[19]
                        rubic[25] = a
                        rubic[22] = b
                        rubic[19] = c
                    if morabba == 21 or morabba == 24 or morabba == 27:
                        a = rubic[42]
                        b = rubic[43]
                        c = rubic[44]
                        rubic[42] = rubic[0]
                        rubic[43] = rubic[3]
                        rubic[44] = rubic[6]
                        rubic[0]  = rubic[47]
                        rubic[3]  = rubic[46]
                        rubic[6]  = rubic[45]
                        rubic[47] = rubic[26]
                        rubic[46] = rubic[23]
                        rubic[45] = rubic[20]
                        rubic[26] = a
                        rubic[23] = b
                        rubic[20] = c
                    if morabba == 28 or morabba == 31 or morabba == 34 or morabba == 37 or morabba == 40 or morabba == 43 or morabba == 46 or morabba == 49 or morabba == 52:
                        a = rubic[42]
                        b = rubic[39]
                        c = rubic[36]
                        rubic[42] = rubic[11]
                        rubic[39] = rubic[14]
                        rubic[36] = rubic[17]
                        rubic[11] = rubic[51]
                        rubic[14] = rubic[48]
                        rubic[17] = rubic[45]
                        rubic[51] = rubic[33]
                        rubic[48] = rubic[30]
                        rubic[45] = rubic[27]
                        rubic[33] = a
                        rubic[30] = b
                        rubic[27] = c
                    if morabba == 29 or morabba == 32 or morabba == 35 or morabba == 47 or morabba == 50 or morabba == 53 or morabba == 38 or morabba == 41 or morabba == 44:
                        a = rubic[43]
                        b = rubic[40]
                        c = rubic[37]
                        rubic[43] = rubic[10]
                        rubic[40] = rubic[13]
                        rubic[37] = rubic[16]
                        rubic[10] = rubic[52]
                        rubic[13] = rubic[49]
                        rubic[16] = rubic[46]
                        rubic[52] = rubic[34]
                        rubic[49] = rubic[31]
                        rubic[46] = rubic[28]
                        rubic[34] = a
                        rubic[31] = b
                        rubic[28] = c
                    if morabba == 30 or morabba == 33 or morabba == 36 or morabba == 39 or morabba == 42 or morabba == 45 or morabba == 48 or morabba == 51 or morabba == 54:
                        a = rubic[44]
                        b = rubic[41]
                        c = rubic[38]
                        rubic[44] = rubic[9]
                        rubic[41] = rubic[12]
                        rubic[38] = rubic[15]
                        rubic[9]  = rubic[53]
                        rubic[12] = rubic[50]
                        rubic[15] = rubic[47]
                        rubic[53] = rubic[35]
                        rubic[50] = rubic[32]
                        rubic[47] = rubic[29]
                        rubic[35] = a
                        rubic[32] = b
                        rubic[29] = c
                    
                        
                        
                        
                        
        if key == 100:
                    if morabba == 1 or morabba == 2 or morabba == 3 or morabba == 10 or morabba == 11 or morabba == 12 or morabba == 19 or morabba == 20 or morabba == 21 or morabba == 28 or morabba == 29 or morabba == 30:
                        a = rubic[2]
                        b = rubic[1]
                        c = rubic[0]
                        rubic[2]  = rubic[29]
                        rubic[1]  = rubic[28]
                        rubic[0]  = rubic[27]
                        rubic[29] = rubic[20]
                        rubic[28] = rubic[19]
                        rubic[27] = rubic[18]
                        rubic[20] = rubic[11]
                        rubic[19] = rubic[10]
                        rubic[18] = rubic[9]
                        rubic[11] = a
                        rubic[10] = b
                        rubic[9]  = c
                    if morabba == 4 or morabba == 5 or morabba == 6 or morabba == 13 or morabba == 14 or morabba == 15 or morabba == 22 or morabba == 23 or morabba == 24 or morabba == 31 or morabba == 32 or morabba == 33:
                        a = rubic[5]
                        b = rubic[4]
                        c = rubic[3]
                        rubic[5]  = rubic[32]
                        rubic[4]  = rubic[31]
                        rubic[3]  = rubic[30]
                        rubic[32] = rubic[23]
                        rubic[31] = rubic[22]
                        rubic[30] = rubic[21]
                        rubic[23] = rubic[14]
                        rubic[22] = rubic[13]
                        rubic[21] = rubic[12]
                        rubic[14] = a
                        rubic[13] = b
                        rubic[12] = c
                    if morabba == 7 or morabba == 8 or morabba == 9 or morabba == 16 or morabba == 17 or morabba == 18 or morabba == 25 or morabba == 26 or morabba == 27 or morabba == 34 or morabba == 35 or morabba == 36:
                        a = rubic[8]
                        b = rubic[7]
                        c = rubic[6]
                        rubic[8]  = rubic[35]
                        rubic[7]  = rubic[34]
                        rubic[6]  = rubic[33]
                        rubic[35] = rubic[26]
                        rubic[34] = rubic[25]
                        rubic[33] = rubic[24]
                        rubic[26] = rubic[17]
                        rubic[25] = rubic[16]
                        rubic[24] = rubic[15]
                        rubic[17] = a
                        rubic[16] = b
                        rubic[15] = c
                    
                        a = rubic[38]
                        b = rubic[37]
                        c = rubic[36]
                        rubic[38] = rubic[18]
                        rubic[37] = rubic[21]
                        rubic[36] = rubic[24]
                        rubic[18] = rubic[51]
                        rubic[21] = rubic[52]
                        rubic[24] = rubic[53]
                        rubic[51] = rubic[8]
                        rubic[52] = rubic[5]
                        rubic[53] = rubic[2]
                        rubic[8]  = a
                        rubic[5]  = b
                        rubic[2]  = c
                    if morabba == 40 or morabba == 41 or morabba == 42:
                        a = rubic[41]
                        b = rubic[40]
                        c = rubic[39]
                        rubic[41] = rubic[19]
                        rubic[40] = rubic[22]
                        rubic[39] = rubic[25]
                        rubic[19] = rubic[48]
                        rubic[22] = rubic[49]
                        rubic[25] = rubic[50]
                        rubic[48] = rubic[7]
                        rubic[49] = rubic[4]
                        rubic[50] = rubic[1]
                        rubic[7]  = a
                        rubic[4]  = b
                        rubic[1]  = c
                    if morabba == 43 or morabba == 44 or morabba == 45:
                        a = rubic[44]
                        b = rubic[43]
                        c = rubic[42]
                        rubic[44] = rubic[20]
                        rubic[43] = rubic[23]
                        rubic[42] = rubic[26]
                        rubic[20] = rubic[45]
                        rubic[23] = rubic[46]
                        rubic[26] = rubic[47]
                        rubic[45] = rubic[6]
                        rubic[46] = rubic[3]
                        rubic[47] = rubic[0]
                        rubic[6]  = a
                        rubic[3]  = b
                        rubic[0]  = c
                    if morabba == 46 or morabba == 47 or morabba == 48:
                        a = rubic[42]
                        b = rubic[43]
                        c = rubic[44]
                        rubic[42] = rubic[0]
                        rubic[43] = rubic[3]
                        rubic[44] = rubic[6]
                        rubic[0]  = rubic[47]
                        rubic[3]  = rubic[46]
                        rubic[6]  = rubic[45]
                        rubic[47] = rubic[26]
                        rubic[46] = rubic[23]
                        rubic[45] = rubic[20]
                        rubic[26] = a
                        rubic[23] = b
                        rubic[20] = c
                    if morabba == 49 or morabba == 50 or morabba == 51:
                        a = rubic[39]
                        b = rubic[40]
                        c = rubic[41]
                        rubic[39] = rubic[1]
                        rubic[40] = rubic[4]
                        rubic[41] = rubic[7]
                        rubic[1]  = rubic[50]
                        rubic[4]  = rubic[49]
                        rubic[7]  = rubic[48]
                        rubic[50] = rubic[25]
                        rubic[49] = rubic[22]
                        rubic[48] = rubic[19]
                        rubic[25] = a
                        rubic[22] = b
                        rubic[19]= c
                    if morabba == 52 or morabba == 53 or morabba == 54:
                        a = rubic[36]
                        b = rubic[37]
                        c = rubic[38]
                        rubic[36] = rubic[2]
                        rubic[37] = rubic[5]
                        rubic[38] = rubic[8]
                        rubic[2]  = rubic[53]
                        rubic[5]  = rubic[52]
                        rubic[8]  = rubic[51]
                        rubic[53] = rubic[24]
                        rubic[52] = rubic[21]
                        rubic[51] = rubic[18]
                        rubic[24] = a
                        rubic[21] = b
                        rubic[18] = c
    z = 75
    fasele=100
    main=pygame.image.load('Main.png')
    sc.blit(main,(0,0))
    sc.blit(tabdil(rubic[36]),(fasele//2,fasele//2,z,z))
    sc.blit(tabdil(rubic[37]),(fasele//2+z,fasele//2,z,z))
    sc.blit(tabdil(rubic[38]),(fasele//2+z+z,fasele//2,z,z))
    sc.blit(tabdil(rubic[39]),(fasele//2,fasele//2+z,z,z))
    sc.blit(tabdil(rubic[40]),(fasele//2+z,fasele//2+z,z,z))
    sc.blit(tabdil(rubic[41]),(fasele//2+z+z,fasele//2+z,z,z))
    sc.blit(tabdil(rubic[42]),(fasele//2,fasele//2+z+z,z,z))
    sc.blit(tabdil(rubic[43]),(fasele//2+z,fasele//2+z+z,z,z))
    sc.blit(tabdil(rubic[44]),(fasele//2+z+z,fasele//2+z+z,z,z))

    sc.blit(tabdil(rubic[0]),(3*fasele//2+zel_morabba,fasele//2,z,z))
    sc.blit(tabdil(rubic[1]),(3*fasele//2+zel_morabba+z,fasele//2,z,z))
    sc.blit(tabdil(rubic[2]),(3*fasele//2+zel_morabba+z+z,fasele//2,z,z))
    sc.blit(tabdil(rubic[3]),(3*fasele//2+zel_morabba,fasele//2+z,z,z))
    sc.blit(tabdil(rubic[4]),(3*fasele//2+zel_morabba+z,fasele//2+z,z,z))
    sc.blit(tabdil(rubic[5]),(3*fasele//2+zel_morabba+z+z,fasele//2+z,z,z))
    sc.blit(tabdil(rubic[6]),(3*fasele//2+zel_morabba,fasele//2+z+z,z,z))
    sc.blit(tabdil(rubic[7]),(3*fasele//2+zel_morabba+z,fasele//2+z+z,z,z))
    sc.blit(tabdil(rubic[8]),(3*fasele//2+zel_morabba+z+z,fasele//2+z+z,z,z))

    sc.blit(tabdil(rubic[27]),(5*fasele//2+2*zel_morabba,fasele//2,z,z))
    sc.blit(tabdil(rubic[28]),(5*fasele//2+2*zel_morabba+z,fasele//2,z,z))
    sc.blit(tabdil(rubic[29]),(5*fasele//2+2*zel_morabba+z+z,fasele//2,z,z))
    sc.blit(tabdil(rubic[30]),(5*fasele//2+2*zel_morabba,fasele//2+z,z,z))
    sc.blit(tabdil(rubic[31]),(5*fasele//2+2*zel_morabba+z,fasele//2+z,z,z))
    sc.blit(tabdil(rubic[32]),(5*fasele//2+2*zel_morabba+z+z,fasele//2+z,z,z))
    sc.blit(tabdil(rubic[33]),(5*fasele//2+2*zel_morabba,fasele//2+z+z,z,z))
    sc.blit(tabdil(rubic[34]),(5*fasele//2+2*zel_morabba+z,fasele//2+z+z,z,z))
    sc.blit(tabdil(rubic[35]),(5*fasele//2+2*zel_morabba+z+z,fasele//2+z+z,z,z))

    sc.blit(tabdil(rubic[9]) ,(fasele//2,3*fasele//2+zel_morabba,z,z))
    sc.blit(tabdil(rubic[10]),(fasele//2+z,3*fasele//2+zel_morabba,z,z))
    sc.blit(tabdil(rubic[11]),(fasele//2+z+z,3*fasele//2+zel_morabba,z,z))
    sc.blit(tabdil(rubic[12]),(fasele//2,3*fasele//2+zel_morabba+z,z,z))
    sc.blit(tabdil(rubic[13]),(fasele//2+z,3*fasele//2+zel_morabba+z,z,z))
    sc.blit(tabdil(rubic[14]),(fasele//2+z+z,3*fasele//2+zel_morabba+z,z,z))
    sc.blit(tabdil(rubic[15]),(fasele//2,3*fasele//2+zel_morabba+z+z,z,z))
    sc.blit(tabdil(rubic[16]),(fasele//2+z,3*fasele//2+zel_morabba+z+z,z,z))
    sc.blit(tabdil(rubic[17]),(fasele//2+z+z,3*fasele//2+zel_morabba+z+z,z,z))

    sc.blit(tabdil(rubic[18]),(3*fasele//2+zel_morabba,3*fasele//2+zel_morabba,z,z))
    sc.blit(tabdil(rubic[19]),(3*fasele//2+zel_morabba+z,3*fasele//2+zel_morabba,z,z))
    sc.blit(tabdil(rubic[20]),(3*fasele//2+zel_morabba+z+z,3*fasele//2+zel_morabba,z,z))
    sc.blit(tabdil(rubic[21]),(3*fasele//2+zel_morabba,3*fasele//2+zel_morabba+z,z,z))
    sc.blit(tabdil(rubic[22]),(3*fasele//2+zel_morabba+z,3*fasele//2+zel_morabba+z,z,z))
    sc.blit(tabdil(rubic[23]),(3*fasele//2+zel_morabba+z+z,3*fasele//2+zel_morabba+z,z,z))
    sc.blit(tabdil(rubic[24]),(3*fasele//2+zel_morabba,3*fasele//2+zel_morabba+z+z,z,z))
    sc.blit(tabdil(rubic[25]),(3*fasele//2+zel_morabba+z,3*fasele//2+zel_morabba+z+z,z,z))
    sc.blit(tabdil(rubic[26]),(3*fasele//2+zel_morabba+z+z,3*fasele//2+zel_morabba+z+z,z,z))
                
    sc.blit(tabdil(rubic[45]),(5*fasele//2+2*zel_morabba,3*fasele//2+zel_morabba,z,z))
    sc.blit(tabdil(rubic[46]),(5*fasele//2+2*zel_morabba+z,3*fasele//2+zel_morabba,z,z))
    sc.blit(tabdil(rubic[47]),(5*fasele//2+2*zel_morabba+z+z,3*fasele//2+zel_morabba,z,z))
    sc.blit(tabdil(rubic[48]),(5*fasele//2+2*zel_morabba,3*fasele//2+zel_morabba+z,z,z))
    sc.blit(tabdil(rubic[49]),(5*fasele//2+2*zel_morabba+z,3*fasele//2+zel_morabba+z,z,z))
    sc.blit(tabdil(rubic[50]),(5*fasele//2+2*zel_morabba+z+z,3*fasele//2+zel_morabba+z,z,z))
    sc.blit(tabdil(rubic[51]),(5*fasele//2+2*zel_morabba,3*fasele//2+zel_morabba+z+z,z,z))
    sc.blit(tabdil(rubic[52]),(5*fasele//2+2*zel_morabba+z,3*fasele//2+zel_morabba+z+z,z,z))
    sc.blit(tabdil(rubic[53]),(5*fasele//2+2*zel_morabba+z+z,3*fasele//2+zel_morabba+z+z,z,z))
    pygame.display.update()

#View 3D
def Rx(x,y,z,t):
        y , z = y*cos(t) - z*sin(t) , z*cos(t) + y*sin(t)
        return y,z
def Ry(x,y,z,t):
        x , z = x*cos(t) - z*sin(t) , z*cos(t) + x*sin(t)
        return x,z
def Rz(x,y,z,t):
        x , y = x*cos(t) - y*sin(t) , y*cos(t) + x*sin(t)
        return x,y
def Action():
        global tx , ty , tz
        A = [[-1,-1,-1],[-1,-1,1],[-1,1,-1],[-1,1,1],[1,-1,-1],[1,-1,1],[1,1,-1],[1,1,1],[-1,-1,-0.25],[-1,-1,0.25]]
        for i in range(len(A)):
            A[i][0] *= 100
            A[i][1] *= 100
            A[i][2] *= 100
        for i in range(len(A)):
            A[i][1] , A[i][2] = Rx( A[i][0] , A[i][1] , A[i][2] , tx )
            A[i][0] , A[i][2] = Ry( A[i][0] , A[i][1] , A[i][2] , ty )
            A[i][0] , A[i][1] = Rz( A[i][0] , A[i][1] , A[i][2] , tz )
        return A
def xnav():
        global tx,ty,tz,C
        A = []
        main=pygame.image.load('Main.png')
        for i in range(90):
            sc.blit(main,(0,0))
            A[:] = Action()
            Show(A,C)
            tx -= AG
def xnavp():
        global tx,ty,tz,C
        A = []
        main=pygame.image.load('Main.png')
        for i in range(90):
            sc.blit(main,(0,0))
            A[:] = Action()
            Show(A,C)
            tx += AG
def ynav():
        global tx,ty,tz,C
        A = []
        main=pygame.image.load('Main.png')
        for i in range(90):
            sc.blit(main,(0,0))
            A[:] = Action()
            Show(A,C)
            ty -= AG
def ynavp():
        global tx,ty,tz,C
        A = []
        main=pygame.image.load('Main.png')
        for i in range(90):
            sc.blit(main,(0,0))
            A[:] = Action()
            Show(A,C)
            ty += AG
def znav():
        global tx,ty,tz,C
        A = []
        main=pygame.image.load('Main.png')
        for i in range(90):
            sc.blit(main,(0,0))
            A[:] = Action()
            Show(A,C)
            tz -= AG
def znavp():
        global tx,ty,tz,C
        A = []
        main=pygame.image.load('Main.png')
        for i in range(90):
            sc.blit(main,(0,0))
            A[:] = Action()
            Show(A,C)
            tz += AG
def rectpos(pos1,pos2,pos3,pos4,color):
        (x1,y1) = pos1
        (x2,y2) = pos2
        (x3,y3) = pos3
        (x4,y4) = pos4
        pos = [pos1 , pos2 , pos3 , pos4 , [(x1*2+x2)//3,(y1*2+y2)//3] , [(x3*2+x4)//3,(y3*2+y4)//3] , [(x1+x2*2)//3,(y1+y2*2)//3] , [(x3+x4*2)//3,(y3+y4*2)//3] , [(x1*2+x3)//3,(y1*2+y3)//3] , [(x2*2+x4)//3,(y2*2+y4)//3] , [(x1+x3*2)//3,(y1+y3*2)//3] , [(x2+x4*2)//3,(y2+y4*2)//3] , [(x1*2+x4)//3,(y1*2+y4)//3] , [(x2*2+x3)//3,(y2*2+y3)//3] , [(x1+x4*2)//3,(y1+y4*2)//3] , [(x2+x3*2)//3,(y2+y3*2)//3]]
        #        0       1        2       3                           4                                    5                                         6                                            7                                         8                                     9                                             10                                       11                                12                                          13                                       14                                       15
        pygame.draw.polygon(sc , color[0] , (pos[0] , pos[4] , pos[12], pos[8]))
        pygame.draw.polygon(sc , color[1] , (pos[4] , pos[6] , pos[13], pos[12]))
        #p.draw.circle(sc , (255,0,0) , (pos[13]),5)
        pygame.draw.polygon(sc , color[2] , (pos[6] , pos[1] , pos[9], pos[13]))
        pygame.draw.polygon(sc , color[3] , (pos[8] , pos[12] , pos[15], pos[10]))
        pygame.draw.polygon(sc , color[4] , (pos[12] , pos[13] , pos[14], pos[15]))
        pygame.draw.polygon(sc , color[5] , (pos[13] , pos[9] , pos[11], pos[14]))
        pygame.draw.polygon(sc , color[6] , (pos[10] , pos[15] , pos[5], pos[2]))
        pygame.draw.polygon(sc , color[7] , (pos[15] , pos[14] , pos[7], pos[5]))
        pygame.draw.polygon(sc , color[8] , (pos[14] , pos[11] , pos[3], pos[7]))
        pygame.draw.line(sc , (0,0,0) , pos[4] , pos[5] , 2)
        pygame.draw.line(sc , (0,0,0) , pos[6] , pos[7] , 2)
        pygame.draw.line(sc , (0,0,0) , pos[10] , pos[11] , 2)
        pygame.draw.line(sc , (0,0,0) , pos[8] , pos[9] , 2)
        pygame.draw.line(sc , (0,0,0) , pos[0] , pos[1] , 2)
        pygame.draw.line(sc , (0,0,0) , pos[0] , pos[2] , 2)
        pygame.draw.line(sc , (0,0,0) , pos[2] , pos[3] , 2)
        pygame.draw.line(sc , (0,0,0) , pos[1] , pos[3] , 2)
def Show(A,C):
        J = [(int(A[0][2])+400 + int(A[1][2])+400 + int(A[5][2])+400 + int(A[4][2])+400) , (int(A[0][2])+400 + int(A[4][2])+400 + int(A[6][2])+400 + int(A[2][2])+400) , (int(A[5][2])+400 + int(A[1][2])+400 + int(A[3][2])+400 + int(A[7][2])+400) , (int(A[2][2])+400 + int(A[3][2])+400 + int(A[7][2])+400 + int(A[6][2])+400)]
        if A[4][2] + A[5][2] + A[7][2] + A[6][2] > A[0][2] + A[1][2] + A[3][2] + A[2][2]:
            f = 1
       #     pygame.draw.polygon( sc , (255,0,0) , ((int(A[0][0])+400,int(A[0][1])+400) , (int(A[1][0])+400,int(A[1][1])+400) , (int(A[3][0])+400,int(A[3][1])+400) , (int(A[2][0])+400,int(A[2][1])+400)))
            rectpos((int(A[0][0])+400,int(A[0][1])+400) , (int(A[1][0])+400,int(A[1][1])+400) , (int(A[2][0])+400,int(A[2][1])+400) , (int(A[3][0])+400,int(A[3][1])+400) , C[0])
        else:
            f = 0
      #      pygame.draw.polygon( sc , (255,0,80) , ( (int(A[4][0])+400,int(A[4][1])+400) , (int(A[6][0])+400,int(A[6][1])+400) , (int(A[7][0])+400,int(A[7][1])+400) , (int(A[5][0])+400,int(A[5][1])+400)))
            rectpos((int(A[4][0])+400,int(A[4][1])+400) , (int(A[6][0])+400,int(A[6][1])+400) , (int(A[5][0])+400,int(A[5][1])+400) , (int(A[7][0])+400,int(A[7][1])+400),C[2])
            
        for i in range(len(J)):
            if min(J) == 100000000000:
                break
            if min(J) == J[0]:
     #           pygame.draw.polygon( sc , (0,0,0) , ((int(A[0][0])+400,int(A[0][1])+400) , (int(A[1][0])+400,int(A[1][1])+400) , (int(A[5][0])+400,int(A[5][1])+400) , (int(A[4][0])+400,int(A[4][1])+400)))
                rectpos((int(A[0][0])+400,int(A[0][1])+400) , (int(A[1][0])+400,int(A[1][1])+400) , (int(A[4][0])+400,int(A[4][1])+400) , (int(A[5][0])+400,int(A[5][1])+400),C[4])
                J[0] = 100000000000
            elif min(J) == J[1]:
    #            pygame.draw.polygon( sc , (0,255,0) , ((int(A[0][0])+400,int(A[0][1])+400) , (int(A[4][0])+400,int(A[4][1])+400) , (int(A[6][0])+400,int(A[6][1])+400) , (int(A[2][0])+400,int(A[2][1])+400)))
                rectpos((int(A[0][0])+400,int(A[0][1])+400) , (int(A[4][0])+400,int(A[4][1])+400) , (int(A[2][0])+400,int(A[2][1])+400) , (int(A[6][0])+400,int(A[6][1])+400),C[3])
                J[1] = 100000000000
            elif min(J) == J[2]:
   #             pygame.draw.polygon( sc , (0,0,255) , ((int(A[5][0])+400,int(A[5][1])+400) , (int(A[1][0])+400,int(A[1][1])+400) , (int(A[3][0])+400,int(A[3][1])+400) , (int(A[7][0])+400,int(A[7][1])+400)))
                rectpos((int(A[5][0])+400,int(A[5][1])+400) , (int(A[1][0])+400,int(A[1][1])+400) , (int(A[7][0])+400,int(A[7][1])+400) , (int(A[3][0])+400,int(A[3][1])+400),C[1])
                J[2] = 100000000000
            elif min(J) == J[3]:
  #              pygame.draw.polygon( sc , (255,255,0) , ( (int(A[2][0])+400,int(A[2][1])+400) , (int(A[3][0])+400,int(A[3][1])+400) , (int(A[7][0])+400,int(A[7][1])+400) , (int(A[6][0])+400,int(A[6][1])+400)))
                rectpos((int(A[2][0])+400,int(A[2][1])+400) , (int(A[3][0])+400,int(A[3][1])+400) , (int(A[6][0])+400,int(A[6][1])+400) , (int(A[7][0])+400,int(A[7][1])+400),C[5])
                J[3] = 100000000000
        if f == 1:
 #           pygame.draw.polygon( sc , (255,80,0) , ( (int(A[4][0])+400,int(A[4][1])+400) , (int(A[6][0])+400,int(A[6][1])+400) , (int(A[7][0])+400,int(A[7][1])+400) , (int(A[5][0])+400,int(A[5][1])+400)))
            rectpos((int(A[4][0])+400,int(A[4][1])+400) , (int(A[6][0])+400,int(A[6][1])+400) , (int(A[5][0])+400,int(A[5][1])+400) , (int(A[7][0])+400,int(A[7][1])+400), C[2])
        else:
#            pygame.draw.polygon( sc , (255,0,0) , ((int(A[0][0])+400,int(A[0][1])+400) , (int(A[1][0])+400,int(A[1][1])+400) , (int(A[3][0])+400,int(A[3][1])+400) , (int(A[2][0])+400,int(A[2][1])+400)))
            rectpos((int(A[0][0])+400,int(A[0][1])+400) , (int(A[1][0])+400,int(A[1][1])+400) , (int(A[2][0])+400,int(A[2][1])+400) , (int(A[3][0])+400,int(A[3][1])+400) , C[0])
        pygame.display.flip()
        #sleep(0.03)

#Main Loop:
random()
done=False
def jaleb(o):
    if o=='white':
        return (255,255,255)
    elif o=='red':
        return (255,0,0)
    elif o=='green':
        return (0,255,0)
    elif o=='blue':
        return (0,0,255)
    elif o=='orange':
        return (255,100,0)
    elif o=='yellow':
        return (255,255,0)
while not done:
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONDOWN:
            mo_po = pygame.mouse.get_pos() #mo_po = mouse position
            if 0<mo_po[0]<60 and 0<mo_po[1]<60:
                random()
            if 910<mo_po[0]<975 and 0<mo_po[1]<60:
                C=[]
                B=[]
                k2=0
                for i in range(54):
                    B.append(jaleb(rubic[i]))
                    if i!=0 and (i+1)%9==0:
                        C.append(B)
                        B=[]
                sx , sy = 975 , 650                 
                tx = pi/(-4)
                ty = pi/(4)
                tz = 0
                vx = 0
                vy = 0
                vz = 0
                P = []
                f=1
                AG = pi/180
                done1 = True
                P[:] = Action()
                main=pygame.image.load('Main.png')
                sc.blit(main,(0,0))
                while done1:
                    for event in pygame.event.get():
                        if event.type==MOUSEBUTTONDOWN:
                            x,y=pygame.mouse.get_pos()
                            if 0<x<60 and 0<y<60:
                                done1=False
                        if event.type == KEYUP:
                            if event.key == K_UP or event.key == K_DOWN:
                                vx = 0
                            if event.key == K_RIGHT or event.key == K_LEFT:
                                vy = 0
                            if event.key == K_HOME or event.key == K_END:
                                vz = 0
                        if event.type == KEYDOWN:
                            if event.key == K_UP:
                                vx = AG
                            elif event.key == K_DOWN:
                                vx = -AG
                            elif event.key == K_LEFT:
                                vy = AG
                            elif event.key == K_RIGHT:
                                vy = -AG
                            elif event.key == K_HOME:
                                vz = AG
                            elif event.key == K_END:
                                vz = -AG
                            elif event.key == K_x:
                                xnav()
                            elif event.key == K_s:
                                xnavp()
                            elif event.key == K_y:
                                ynav()
                            elif event.key == K_h:
                                ynavp()
                            elif event.key == K_z:
                                znav()
                            elif event.key == K_a:
                                znavp()
                    tx += vx
                    ty += vy
                    tz += vz
                    if vz+vy+vx != 0 or f == 1:
                        P[:] = Action()
                        sc.blit(main,(0,0))
                        Show(P,C)
                        f = 0
                z = zel_morabba//3
                sc.blit(main,(0,0))
                sc.blit(tabdil(rubic[36]),(fasele//2,fasele//2,z,z))
                sc.blit(tabdil(rubic[37]),(fasele//2+z,fasele//2,z,z))
                sc.blit(tabdil(rubic[38]),(fasele//2+z+z,fasele//2,z,z))
                sc.blit(tabdil(rubic[39]),(fasele//2,fasele//2+z,z,z))
                sc.blit(tabdil(rubic[40]),(fasele//2+z,fasele//2+z,z,z))
                sc.blit(tabdil(rubic[41]),(fasele//2+z+z,fasele//2+z,z,z))
                sc.blit(tabdil(rubic[42]),(fasele//2,fasele//2+z+z,z,z))
                sc.blit(tabdil(rubic[43]),(fasele//2+z,fasele//2+z+z,z,z))
                sc.blit(tabdil(rubic[44]),(fasele//2+z+z,fasele//2+z+z,z,z))

                sc.blit(tabdil(rubic[0]),(3*fasele//2+zel_morabba,fasele//2,z,z))
                sc.blit(tabdil(rubic[1]),(3*fasele//2+zel_morabba+z,fasele//2,z,z))
                sc.blit(tabdil(rubic[2]),(3*fasele//2+zel_morabba+z+z,fasele//2,z,z))
                sc.blit(tabdil(rubic[3]),(3*fasele//2+zel_morabba,fasele//2+z,z,z))
                sc.blit(tabdil(rubic[4]),(3*fasele//2+zel_morabba+z,fasele//2+z,z,z))
                sc.blit(tabdil(rubic[5]),(3*fasele//2+zel_morabba+z+z,fasele//2+z,z,z))
                sc.blit(tabdil(rubic[6]),(3*fasele//2+zel_morabba,fasele//2+z+z,z,z))
                sc.blit(tabdil(rubic[7]),(3*fasele//2+zel_morabba+z,fasele//2+z+z,z,z))
                sc.blit(tabdil(rubic[8]),(3*fasele//2+zel_morabba+z+z,fasele//2+z+z,z,z))

                sc.blit(tabdil(rubic[27]),(5*fasele//2+2*zel_morabba,fasele//2,z,z))
                sc.blit(tabdil(rubic[28]),(5*fasele//2+2*zel_morabba+z,fasele//2,z,z))
                sc.blit(tabdil(rubic[29]),(5*fasele//2+2*zel_morabba+z+z,fasele//2,z,z))
                sc.blit(tabdil(rubic[30]),(5*fasele//2+2*zel_morabba,fasele//2+z,z,z))
                sc.blit(tabdil(rubic[31]),(5*fasele//2+2*zel_morabba+z,fasele//2+z,z,z))
                sc.blit(tabdil(rubic[32]),(5*fasele//2+2*zel_morabba+z+z,fasele//2+z,z,z))
                sc.blit(tabdil(rubic[33]),(5*fasele//2+2*zel_morabba,fasele//2+z+z,z,z))
                sc.blit(tabdil(rubic[34]),(5*fasele//2+2*zel_morabba+z,fasele//2+z+z,z,z))
                sc.blit(tabdil(rubic[35]),(5*fasele//2+2*zel_morabba+z+z,fasele//2+z+z,z,z))

                sc.blit(tabdil(rubic[9]) ,(fasele//2,3*fasele//2+zel_morabba,z,z))
                sc.blit(tabdil(rubic[10]),(fasele//2+z,3*fasele//2+zel_morabba,z,z))
                sc.blit(tabdil(rubic[11]),(fasele//2+z+z,3*fasele//2+zel_morabba,z,z))
                sc.blit(tabdil(rubic[12]),(fasele//2,3*fasele//2+zel_morabba+z,z,z))
                sc.blit(tabdil(rubic[13]),(fasele//2+z,3*fasele//2+zel_morabba+z,z,z))
                sc.blit(tabdil(rubic[14]),(fasele//2+z+z,3*fasele//2+zel_morabba+z,z,z))
                sc.blit(tabdil(rubic[15]),(fasele//2,3*fasele//2+zel_morabba+z+z,z,z))
                sc.blit(tabdil(rubic[16]),(fasele//2+z,3*fasele//2+zel_morabba+z+z,z,z))
                sc.blit(tabdil(rubic[17]),(fasele//2+z+z,3*fasele//2+zel_morabba+z+z,z,z))

                sc.blit(tabdil(rubic[18]),(3*fasele//2+zel_morabba,3*fasele//2+zel_morabba,z,z))
                sc.blit(tabdil(rubic[19]),(3*fasele//2+zel_morabba+z,3*fasele//2+zel_morabba,z,z))
                sc.blit(tabdil(rubic[20]),(3*fasele//2+zel_morabba+z+z,3*fasele//2+zel_morabba,z,z))
                sc.blit(tabdil(rubic[21]),(3*fasele//2+zel_morabba,3*fasele//2+zel_morabba+z,z,z))
                sc.blit(tabdil(rubic[22]),(3*fasele//2+zel_morabba+z,3*fasele//2+zel_morabba+z,z,z))
                sc.blit(tabdil(rubic[23]),(3*fasele//2+zel_morabba+z+z,3*fasele//2+zel_morabba+z,z,z))
                sc.blit(tabdil(rubic[24]),(3*fasele//2+zel_morabba,3*fasele//2+zel_morabba+z+z,z,z))
                sc.blit(tabdil(rubic[25]),(3*fasele//2+zel_morabba+z,3*fasele//2+zel_morabba+z+z,z,z))
                sc.blit(tabdil(rubic[26]),(3*fasele//2+zel_morabba+z+z,3*fasele//2+zel_morabba+z+z,z,z))
                            
                sc.blit(tabdil(rubic[45]),(5*fasele//2+2*zel_morabba,3*fasele//2+zel_morabba,z,z))
                sc.blit(tabdil(rubic[46]),(5*fasele//2+2*zel_morabba+z,3*fasele//2+zel_morabba,z,z))
                sc.blit(tabdil(rubic[47]),(5*fasele//2+2*zel_morabba+z+z,3*fasele//2+zel_morabba,z,z))
                sc.blit(tabdil(rubic[48]),(5*fasele//2+2*zel_morabba,3*fasele//2+zel_morabba+z,z,z))
                sc.blit(tabdil(rubic[49]),(5*fasele//2+2*zel_morabba+z,3*fasele//2+zel_morabba+z,z,z))
                sc.blit(tabdil(rubic[50]),(5*fasele//2+2*zel_morabba+z+z,3*fasele//2+zel_morabba+z,z,z))
                sc.blit(tabdil(rubic[51]),(5*fasele//2+2*zel_morabba,3*fasele//2+zel_morabba+z+z,z,z))
                sc.blit(tabdil(rubic[52]),(5*fasele//2+2*zel_morabba+z,3*fasele//2+zel_morabba+z+z,z,z))
                sc.blit(tabdil(rubic[53]),(5*fasele//2+2*zel_morabba+z+z,3*fasele//2+zel_morabba+z+z,z,z))
                pygame.display.update()                
            if 0.5*fasele < mo_po[0] < fasele//2+zel_morabba//3:
                if 0.5*fasele < mo_po[1] < 0.5*fasele+zel_morabba//3:
                    morabba = (37)
                if 0.5*fasele+zel_morabba//3 < mo_po[1] < 0.5*fasele+2*zel_morabba//3:
                    morabba = (40)
                if 0.5*fasele+2*zel_morabba//3 < mo_po[1] < 0.5*fasele+zel_morabba:
                    morabba = (43)
                if 1.5*fasele+zel_morabba < mo_po[1] < 1.5*fasele+4*zel_morabba//3:
                    morabba = (10)
                if 1.5*fasele+4*zel_morabba//3 < mo_po[1] < 1.5*fasele+5*zel_morabba//3:
                    morabba = (13)
                if 1.5*fasele+5*zel_morabba//3 < mo_po[1] < 1.5*fasele+2*zel_morabba:
                    morabba = (16)
            if 0.5*fasele+zel_morabba//3 < mo_po[0] < fasele//2+2*zel_morabba//3:
                if 0.5*fasele < mo_po[1] < 0.5*fasele+zel_morabba//3:
                    morabba = (38)
                if 0.5*fasele+zel_morabba//3 < mo_po[1] < 0.5*fasele+2*zel_morabba//3:
                    morabba = (41)
                if 0.5*fasele+2*zel_morabba//3 < mo_po[1] < 0.5*fasele+zel_morabba:
                    morabba = (44)
                if 1.5*fasele+zel_morabba < mo_po[1] < 1.5*fasele+4*zel_morabba//3:
                    morabba = (11)
                if 1.5*fasele+4*zel_morabba//3 < mo_po[1] < 1.5*fasele+5*zel_morabba//3:
                    morabba = (14)
                if 1.5*fasele+5*zel_morabba//3 < mo_po[1] < 1.5*fasele+2*zel_morabba:
                    morabba = (17)
            if 0.5*fasele+2*zel_morabba//3 < mo_po[0] < fasele//2+zel_morabba:
                if 0.5*fasele < mo_po[1] < 0.5*fasele+zel_morabba//3:
                    morabba = (39)
                if 0.5*fasele+zel_morabba//3 < mo_po[1] < 0.5*fasele+2*zel_morabba//3:
                    morabba = (42)
                if 0.5*fasele+2*zel_morabba//3 < mo_po[1] < 0.5*fasele+zel_morabba:
                    morabba = (45)
                if 1.5*fasele+zel_morabba < mo_po[1] < 1.5*fasele+4*zel_morabba//3:
                    morabba = (12)
                if 1.5*fasele+4*zel_morabba//3 < mo_po[1] < 1.5*fasele+5*zel_morabba//3:
                    morabba = (15)
                if 1.5*fasele+5*zel_morabba//3 < mo_po[1] < 1.5*fasele+2*zel_morabba:
                    morabba = (18)
                
            if 1.5*fasele+zel_morabba < mo_po[0] < 1.5*fasele+zel_morabba+zel_morabba//3:
                if 0.5*fasele < mo_po[1] < 0.5*fasele+zel_morabba//3:
                    morabba = (1)
                if 0.5*fasele+zel_morabba//3 < mo_po[1] < 0.5*fasele+2*zel_morabba//3:
                    morabba = (4)
                if 0.5*fasele+2*zel_morabba//3 < mo_po[1] < 0.5*fasele+zel_morabba:
                    morabba = (7)
                if 1.5*fasele+zel_morabba < mo_po[1] < 1.5*fasele+4*zel_morabba//3:
                    morabba = (19)
                if 1.5*fasele+4*zel_morabba//3 < mo_po[1] < 1.5*fasele+5*zel_morabba//3:
                    morabba = (22)
                if 1.5*fasele+5*zel_morabba//3 < mo_po[1] < 1.5*fasele+2*zel_morabba:
                    morabba = (25) 
            if 1.5*fasele+zel_morabba+zel_morabba//3 < mo_po[0] < 1.5*fasele+zel_morabba+2*zel_morabba//3:
                if 0.5*fasele < mo_po[1] < 0.5*fasele+zel_morabba//3:
                    morabba = (2)
                if 0.5*fasele+zel_morabba//3 < mo_po[1] < 0.5*fasele+2*zel_morabba//3:
                    morabba = (5)
                if 0.5*fasele+2*zel_morabba//3 < mo_po[1] < 0.5*fasele+zel_morabba:
                    morabba = (8)
                if 1.5*fasele+zel_morabba < mo_po[1] < 1.5*fasele+4*zel_morabba//3:
                    morabba = (20)
                if 1.5*fasele+4*zel_morabba//3 < mo_po[1] < 1.5*fasele+5*zel_morabba//3:
                    morabba = (23)
                if 1.5*fasele+5*zel_morabba//3 < mo_po[1] < 1.5*fasele+2*zel_morabba:
                    morabba = (26)
            if 1.5*fasele+zel_morabba+2*zel_morabba//3 < mo_po[0] < 1.5*fasele+2*zel_morabba:
                if 0.5*fasele < mo_po[1] < 0.5*fasele+zel_morabba//3:
                    morabba = (3)
                if 0.5*fasele+zel_morabba//3 < mo_po[1] < 0.5*fasele+2*zel_morabba//3:
                    morabba = (6)
                if 0.5*fasele+2*zel_morabba//3 < mo_po[1] < 0.5*fasele+zel_morabba:
                    morabba = (9)
                if 1.5*fasele+zel_morabba < mo_po[1] < 1.5*fasele+4*zel_morabba//3:
                    morabba = (21)
                if 1.5*fasele+4*zel_morabba//3 < mo_po[1] < 1.5*fasele+5*zel_morabba//3:
                    morabba = (24)
                if 1.5*fasele+5*zel_morabba//3 < mo_po[1] < 1.5*fasele+2*zel_morabba:
                    morabba = (27)

            if 2.5*fasele+2*zel_morabba < mo_po[0] < 2.5*fasele+2*zel_morabba+zel_morabba//3:
                if 0.5*fasele < mo_po[1] < 0.5*fasele+zel_morabba//3:
                    morabba = (28)
                if 0.5*fasele+zel_morabba//3 < mo_po[1] < 0.5*fasele+2*zel_morabba//3:
                    morabba = (31)
                if 0.5*fasele+2*zel_morabba//3 < mo_po[1] < 0.5*fasele+zel_morabba:
                    morabba = (34)
                if 1.5*fasele+zel_morabba < mo_po[1] < 1.5*fasele+4*zel_morabba//3:
                    morabba = (46)
                if 1.5*fasele+4*zel_morabba//3 < mo_po[1] < 1.5*fasele+5*zel_morabba//3:
                    morabba = (49)
                if 1.5*fasele+5*zel_morabba//3 < mo_po[1] < 1.5*fasele+2*zel_morabba:
                    morabba = (52)
            if 2.5*fasele+2*zel_morabba+zel_morabba//3 < mo_po[0] < 2.5*fasele+2*zel_morabba+2*zel_morabba//3:
                if 0.5*fasele < mo_po[1] < 0.5*fasele+zel_morabba//3:
                    morabba = (29)
                if 0.5*fasele+zel_morabba//3 < mo_po[1] < 0.5*fasele+2*zel_morabba//3:
                    morabba = (32)
                if 0.5*fasele+2*zel_morabba//3 < mo_po[1] < 0.5*fasele+zel_morabba:
                    morabba = (35)
                if 1.5*fasele+zel_morabba < mo_po[1] < 1.5*fasele+4*zel_morabba//3:
                    morabba = (47)
                if 1.5*fasele+4*zel_morabba//3 < mo_po[1] < 1.5*fasele+5*zel_morabba//3:
                    morabba = (50)
                if 1.5*fasele+5*zel_morabba//3 < mo_po[1] < 1.5*fasele+2*zel_morabba:
                    morabba = (53)
            if 2.5*fasele+2*zel_morabba+2*zel_morabba//3 < mo_po[0] < 2.5*fasele+3*zel_morabba:
                if 0.5*fasele < mo_po[1] < 0.5*fasele+zel_morabba//3:
                    morabba = (30)
                if 0.5*fasele+zel_morabba//3 < mo_po[1] < 0.5*fasele+2*zel_morabba//3:
                    morabba = (33)
                if 0.5*fasele+2*zel_morabba//3 < mo_po[1] < 0.5*fasele+zel_morabba:
                    morabba = (36)
                if 1.5*fasele+zel_morabba < mo_po[1] < 1.5*fasele+4*zel_morabba//3:
                    morabba = (48)
                if 1.5*fasele+4*zel_morabba//3 < mo_po[1] < 1.5*fasele+5*zel_morabba//3:
                    morabba = (51)
                if 1.5*fasele+5*zel_morabba//3 < mo_po[1] < 1.5*fasele+2*zel_morabba:
                    morabba = (54)


                    
        if e.type == pygame.KEYDOWN:
            if e.key == 119:
                if morabba == 1 or morabba == 4 or morabba == 7:
                    a = rubic[42]
                    b = rubic[43]
                    c = rubic[44]
                    rubic[42] = rubic[0]
                    rubic[43] = rubic[3]
                    rubic[44] = rubic[6]
                    rubic[0]  = rubic[47]
                    rubic[3]  = rubic[46]
                    rubic[6]  = rubic[45]
                    rubic[47] = rubic[26]
                    rubic[46] = rubic[23]
                    rubic[45] = rubic[20]
                    rubic[26] = a
                    rubic[23] = b
                    rubic[20] = c
                if morabba == 2  or morabba == 5 or morabba == 8:
                    a = rubic[39]
                    b = rubic[40]
                    c = rubic[41]
                    rubic[39] = rubic[1]
                    rubic[40] = rubic[4]
                    rubic[41] = rubic[7]
                    rubic[1]  = rubic[50]
                    rubic[4]  = rubic[49]
                    rubic[7]  = rubic[48]
                    rubic[50] = rubic[25]
                    rubic[49] = rubic[22]
                    rubic[48] = rubic[19]
                    rubic[25] = a
                    rubic[22] = b
                    rubic[19] = c
                if morabba == 3  or morabba == 6 or morabba == 9:
                    a = rubic[36]
                    b = rubic[37]
                    c = rubic[38]
                    rubic[36] = rubic[2]
                    rubic[37] = rubic[5]
                    rubic[38] = rubic[8]
                    rubic[2]  = rubic[53]
                    rubic[5]  = rubic[52]
                    rubic[8]  = rubic[51]
                    rubic[53] = rubic[24]
                    rubic[52] = rubic[21]
                    rubic[51] = rubic[18]
                    rubic[24] = a
                    rubic[21] = b
                    rubic[18] = c
                if morabba == 10  or morabba == 13 or morabba == 16:
                    a = rubic[44]
                    b = rubic[41]
                    c = rubic[38]
                    rubic[44] = rubic[9]
                    rubic[41] = rubic[12]
                    rubic[38] = rubic[15]
                    rubic[9]  = rubic[53]
                    rubic[12] = rubic[50]
                    rubic[15] = rubic[47]
                    rubic[53] = rubic[35]
                    rubic[50] = rubic[32]
                    rubic[47] = rubic[29]
                    rubic[35] = a
                    rubic[32] = b
                    rubic[29] = c
                if morabba == 11  or morabba == 14 or morabba == 17:
                    a = rubic[43]
                    b = rubic[40]
                    c = rubic[37]
                    rubic[43] = rubic[10]
                    rubic[40] = rubic[13]
                    rubic[37] = rubic[16]
                    rubic[10] = rubic[52]
                    rubic[13] = rubic[49]
                    rubic[16] = rubic[46]
                    rubic[52] = rubic[34]
                    rubic[49] = rubic[31]
                    rubic[46] = rubic[28]
                    rubic[34] = a
                    rubic[31] = b
                    rubic[28] = c
                if morabba == 12  or morabba == 15 or morabba == 18:
                    a = rubic[42]
                    b = rubic[39]
                    c = rubic[36]
                    rubic[42] = rubic[11]
                    rubic[39] = rubic[14]
                    rubic[36] = rubic[17]
                    rubic[11] = rubic[51]
                    rubic[14] = rubic[48]
                    rubic[17] = rubic[45]
                    rubic[51] = rubic[33]
                    rubic[48] = rubic[30]
                    rubic[45] = rubic[27]
                    rubic[33] = a
                    rubic[30] = b
                    rubic[27] = c
                if morabba == 19  or morabba == 22 or morabba == 25:
                    a = rubic[38]
                    b = rubic[37]
                    c = rubic[36]
                    rubic[38] = rubic[18]
                    rubic[37] = rubic[21]
                    rubic[36] = rubic[24]
                    rubic[18] = rubic[51]
                    rubic[21] = rubic[52]
                    rubic[24] = rubic[53]
                    rubic[51] = rubic[8]
                    rubic[52] = rubic[5]
                    rubic[53] = rubic[2]
                    rubic[8]  = a
                    rubic[5]  = b
                    rubic[2]  = c
                if morabba == 20  or morabba == 23 or morabba == 26:
                    a = rubic[41]
                    b = rubic[40]
                    c = rubic[39]
                    rubic[41] = rubic[19]
                    rubic[40] = rubic[22]
                    rubic[39] = rubic[25]
                    rubic[19] = rubic[48]
                    rubic[22] = rubic[49]
                    rubic[25] = rubic[50]
                    rubic[48] = rubic[7]
                    rubic[49] = rubic[4]
                    rubic[50] = rubic[1]
                    rubic[7]  = a
                    rubic[4]  = b
                    rubic[1]  = c
                if morabba == 21  or morabba == 24 or morabba == 27:
                    a = rubic[44]
                    b = rubic[43]
                    c = rubic[42]
                    rubic[44] = rubic[20]
                    rubic[43] = rubic[23]
                    rubic[42] = rubic[26]
                    rubic[20] = rubic[45]
                    rubic[23] = rubic[46]
                    rubic[26] = rubic[47]
                    rubic[45] = rubic[6]
                    rubic[46] = rubic[3]
                    rubic[47] = rubic[0]
                    rubic[6]  = a
                    rubic[3]  = b
                    rubic[0]  = c
                if morabba == 28  or morabba == 31 or morabba == 34 or morabba == 37 or morabba == 40 or morabba == 43 or morabba == 46 or morabba == 49 or morabba == 52:
                    a = rubic[36]
                    b = rubic[39]
                    c = rubic[42]
                    rubic[36] = rubic[27]
                    rubic[39] = rubic[30]
                    rubic[42] = rubic[33]
                    rubic[27] = rubic[45]
                    rubic[30] = rubic[48]
                    rubic[33] = rubic[51]
                    rubic[45] = rubic[17]
                    rubic[48] = rubic[14]
                    rubic[51] = rubic[11]
                    rubic[17] = a
                    rubic[14] = b
                    rubic[11] = c
                if morabba == 29  or morabba == 32 or morabba == 35 or morabba == 47 or morabba == 50 or morabba == 53 or morabba == 38 or morabba == 41 or morabba == 44:
                    a = rubic[37]
                    b = rubic[40]
                    c = rubic[43]
                    rubic[37] = rubic[28]
                    rubic[40] = rubic[31]
                    rubic[43] = rubic[34]
                    rubic[28] = rubic[46]
                    rubic[31] = rubic[49]
                    rubic[34] = rubic[52]
                    rubic[46] = rubic[16]
                    rubic[49] = rubic[13]
                    rubic[52] = rubic[10]
                    rubic[16] = a
                    rubic[13] = b
                    rubic[10] = c
                if morabba == 30  or morabba == 33 or morabba == 36 or morabba == 48 or morabba == 51 or morabba == 54 or morabba == 39 or morabba == 42 or morabba == 45:
                    a = rubic[38]
                    b = rubic[41]
                    c = rubic[44]
                    rubic[38] = rubic[29]
                    rubic[41] = rubic[32]
                    rubic[44] = rubic[35]
                    rubic[29] = rubic[47]
                    rubic[32] = rubic[50]
                    rubic[35] = rubic[53]
                    rubic[47] = rubic[15]
                    rubic[50] = rubic[12]
                    rubic[53] = rubic[9]
                    rubic[15] = a
                    rubic[12] = b
                    rubic[9]  = c



                    
            if e.key == 97:
                if morabba == 1 or morabba == 2 or morabba == 3 or morabba == 10 or morabba == 11 or morabba == 12 or morabba == 19 or morabba == 20 or morabba == 21 or morabba == 28 or morabba == 29 or morabba == 30:
                    a = rubic[27]
                    b = rubic[28]
                    c = rubic[29]
                    rubic[27] = rubic[0]
                    rubic[28] = rubic[1]
                    rubic[29] = rubic[2]
                    rubic[0]  = rubic[9]
                    rubic[1]  = rubic[10]
                    rubic[2]  = rubic[11]
                    rubic[9]  = rubic[18]
                    rubic[10] = rubic[19]
                    rubic[11] = rubic[20]
                    rubic[18] = a
                    rubic[19] = b
                    rubic[20] = c
                if morabba == 4 or morabba == 5 or morabba == 6 or morabba == 13 or morabba == 14 or morabba == 15 or morabba == 22 or morabba == 23 or morabba == 24 or morabba == 31 or morabba == 32 or morabba == 33:
                    a = rubic[30]
                    b = rubic[31]
                    c = rubic[32]
                    rubic[30] = rubic[3]
                    rubic[31] = rubic[4]
                    rubic[32] = rubic[5]
                    rubic[3]  = rubic[12]
                    rubic[4]  = rubic[13]
                    rubic[5]  = rubic[14]
                    rubic[12] = rubic[21]
                    rubic[13] = rubic[22]
                    rubic[14] = rubic[23]
                    rubic[21] = a
                    rubic[22] = b
                    rubic[23] = c
                if morabba == 7 or morabba == 8 or morabba == 9 or morabba == 16 or morabba == 17 or morabba == 18 or morabba == 25 or morabba == 26 or morabba == 27 or morabba == 34 or morabba == 35 or morabba == 36:
                    a = rubic[33]
                    b = rubic[34]
                    c = rubic[35]
                    rubic[33] = rubic[6]
                    rubic[34] = rubic[7]
                    rubic[35] = rubic[8]
                    rubic[6]  = rubic[15]
                    rubic[7]  = rubic[16]
                    rubic[8]  = rubic[17]
                    rubic[15] = rubic[24]
                    rubic[16] = rubic[25]
                    rubic[17] = rubic[26]
                    rubic[24] = a
                    rubic[25] = b
                    rubic[26] = c
                if morabba == 37 or morabba == 38 or morabba == 39:
                    a = rubic[36]
                    b = rubic[37]
                    c = rubic[38]
                    rubic[36] = rubic[2]
                    rubic[37] = rubic[5]
                    rubic[38] = rubic[8]
                    rubic[2]  = rubic[53]
                    rubic[5]  = rubic[52]
                    rubic[8]  = rubic[51]
                    rubic[53] = rubic[24]
                    rubic[52] = rubic[21]
                    rubic[51] = rubic[18]
                    rubic[24] = a
                    rubic[21] = b
                    rubic[18] = c
                if morabba == 40 or morabba == 41 or morabba == 42:
                    a = rubic[39]
                    b = rubic[40]
                    c = rubic[41]
                    rubic[39] = rubic[1]
                    rubic[40] = rubic[4]
                    rubic[41] = rubic[7]
                    rubic[1]  = rubic[50]
                    rubic[4]  = rubic[49]
                    rubic[7]  = rubic[48]
                    rubic[50] = rubic[25]
                    rubic[49] = rubic[22]
                    rubic[48] = rubic[19]
                    rubic[25] = a
                    rubic[22] = b
                    rubic[19] = c
                if morabba == 43 or morabba == 44 or morabba == 45:
                    a = rubic[42]
                    b = rubic[43]
                    c = rubic[44]
                    rubic[42] = rubic[0]
                    rubic[43] = rubic[3]
                    rubic[44] = rubic[6]
                    rubic[0]  = rubic[47]
                    rubic[3]  = rubic[46]
                    rubic[6]  = rubic[45]
                    rubic[47] = rubic[26]
                    rubic[46] = rubic[23]
                    rubic[45] = rubic[20]
                    rubic[26] = a
                    rubic[23] = b
                    rubic[20] = c
                if morabba == 46 or morabba == 47 or morabba == 48:
                    a = rubic[44]
                    b = rubic[43]
                    c = rubic[42]
                    rubic[44] = rubic[20]
                    rubic[43] = rubic[23]
                    rubic[42] = rubic[26]
                    rubic[20] = rubic[45]
                    rubic[23] = rubic[46]
                    rubic[26] = rubic[47]
                    rubic[45] = rubic[6]
                    rubic[46] = rubic[3]
                    rubic[47] = rubic[0]
                    rubic[6]  = a
                    rubic[3]  = b
                    rubic[0]  = c
                if morabba == 49 or morabba == 50 or morabba == 51:
                    a = rubic[41]
                    b = rubic[40]
                    c = rubic[39]
                    rubic[41] = rubic[19]
                    rubic[40] = rubic[22]
                    rubic[39] = rubic[25]
                    rubic[19] = rubic[48]
                    rubic[22] = rubic[49]
                    rubic[25] = rubic[50]
                    rubic[48] = rubic[7]
                    rubic[49] = rubic[4]
                    rubic[50] = rubic[1]
                    rubic[7]  = a
                    rubic[4]  = b
                    rubic[1]  = c
                if morabba == 52 or morabba == 53 or morabba == 54:
                    a = rubic[38]
                    b = rubic[37]
                    c = rubic[36]
                    rubic[38] = rubic[18]
                    rubic[37] = rubic[21]
                    rubic[36] = rubic[24]
                    rubic[18] = rubic[51]
                    rubic[21] = rubic[52]
                    rubic[24] = rubic[53]
                    rubic[51] = rubic[8]
                    rubic[52] = rubic[5]
                    rubic[53] = rubic[2]
                    rubic[8]  = a
                    rubic[5]  = b
                    rubic[2]  = c




                    
            if e.key == 115:
                if morabba == 1 or morabba == 4 or morabba == 7:
                    a = rubic[44]
                    b = rubic[43]
                    c = rubic[42]
                    rubic[44] = rubic[20]
                    rubic[43] = rubic[23]
                    rubic[42] = rubic[26]
                    rubic[20] = rubic[45]
                    rubic[23] = rubic[46]
                    rubic[26] = rubic[47]
                    rubic[45] = rubic[6]
                    rubic[46] = rubic[3]
                    rubic[47] = rubic[0]
                    rubic[6]  = a
                    rubic[3]  = b
                    rubic[0]  = c
                if morabba == 2 or morabba == 5 or morabba == 8:
                    a = rubic[41]
                    b = rubic[40]
                    c = rubic[39]
                    rubic[41] = rubic[19]
                    rubic[40] = rubic[22]
                    rubic[39] = rubic[25]
                    rubic[19] = rubic[48]
                    rubic[22] = rubic[49]
                    rubic[25] = rubic[50]
                    rubic[48] = rubic[7]
                    rubic[49] = rubic[4]
                    rubic[50] = rubic[1]
                    rubic[7]  = a
                    rubic[4]  = b
                    rubic[1]  = c
                if morabba == 3 or morabba == 6 or morabba == 9:
                    a = rubic[38]
                    b = rubic[37]
                    c = rubic[36]
                    rubic[38] = rubic[18]
                    rubic[37] = rubic[21]
                    rubic[36] = rubic[24]
                    rubic[18] = rubic[51]
                    rubic[21] = rubic[52]
                    rubic[24] = rubic[53]
                    rubic[51] = rubic[8]
                    rubic[52] = rubic[5]
                    rubic[53] = rubic[2]
                    rubic[8]  = a
                    rubic[5]  = b
                    rubic[2]  = c
                if morabba == 10 or morabba == 13 or morabba == 16:
                    a = rubic[38]
                    b = rubic[41]
                    c = rubic[44]
                    rubic[38] = rubic[29]
                    rubic[41] = rubic[32]
                    rubic[44] = rubic[35]
                    rubic[29] = rubic[47]
                    rubic[32] = rubic[50]
                    rubic[35] = rubic[53]
                    rubic[47] = rubic[15]
                    rubic[50] = rubic[12]
                    rubic[53] = rubic[9]
                    rubic[15] = a
                    rubic[12] = b
                    rubic[9]  = c
                if morabba == 11 or morabba == 14 or morabba == 17:
                    a = rubic[37]
                    b = rubic[40]
                    c = rubic[43]
                    rubic[37] = rubic[28]
                    rubic[40] = rubic[31]
                    rubic[43] = rubic[34]
                    rubic[28] = rubic[46]
                    rubic[31] = rubic[49]
                    rubic[34] = rubic[52]
                    rubic[46] = rubic[16]
                    rubic[49] = rubic[13]
                    rubic[52] = rubic[10]
                    rubic[16] = a
                    rubic[13] = b
                    rubic[10] = c
                if morabba == 12 or morabba == 15 or morabba == 18:
                    a = rubic[36]
                    b = rubic[39]
                    c = rubic[42]
                    rubic[36] = rubic[27]
                    rubic[39] = rubic[30]
                    rubic[42] = rubic[33]
                    rubic[27] = rubic[45]
                    rubic[30] = rubic[48]
                    rubic[33] = rubic[51]
                    rubic[45] = rubic[17]
                    rubic[48] = rubic[14]
                    rubic[51] = rubic[11]
                    rubic[17] = a
                    rubic[14] = b
                    rubic[11] = c
                if morabba == 19 or morabba == 22 or morabba == 25:
                    a = rubic[36]
                    b = rubic[37]
                    c = rubic[38]
                    rubic[36] = rubic[2]
                    rubic[37] = rubic[5]
                    rubic[38] = rubic[8]
                    rubic[2]  = rubic[53]
                    rubic[5]  = rubic[52]
                    rubic[8]  = rubic[51]
                    rubic[53] = rubic[24]
                    rubic[52] = rubic[21]
                    rubic[51] = rubic[18]
                    rubic[24] = a
                    rubic[21] = b
                    rubic[18] = c
                if morabba == 20 or morabba == 23 or morabba == 26:
                    a = rubic[39]
                    b = rubic[40]
                    c = rubic[41]
                    rubic[39] = rubic[1]
                    rubic[40] = rubic[4]
                    rubic[41] = rubic[7]
                    rubic[1]  = rubic[50]
                    rubic[4]  = rubic[49]
                    rubic[7]  = rubic[48]
                    rubic[50] = rubic[25]
                    rubic[49] = rubic[22]
                    rubic[48] = rubic[19]
                    rubic[25] = a
                    rubic[22] = b
                    rubic[19] = c
                if morabba == 21 or morabba == 24 or morabba == 27:
                    a = rubic[42]
                    b = rubic[43]
                    c = rubic[44]
                    rubic[42] = rubic[0]
                    rubic[43] = rubic[3]
                    rubic[44] = rubic[6]
                    rubic[0]  = rubic[47]
                    rubic[3]  = rubic[46]
                    rubic[6]  = rubic[45]
                    rubic[47] = rubic[26]
                    rubic[46] = rubic[23]
                    rubic[45] = rubic[20]
                    rubic[26] = a
                    rubic[23] = b
                    rubic[20] = c
                if morabba == 28 or morabba == 31 or morabba == 34 or morabba == 37 or morabba == 40 or morabba == 43 or morabba == 46 or morabba == 49 or morabba == 52:
                    a = rubic[42]
                    b = rubic[39]
                    c = rubic[36]
                    rubic[42] = rubic[11]
                    rubic[39] = rubic[14]
                    rubic[36] = rubic[17]
                    rubic[11] = rubic[51]
                    rubic[14] = rubic[48]
                    rubic[17] = rubic[45]
                    rubic[51] = rubic[33]
                    rubic[48] = rubic[30]
                    rubic[45] = rubic[27]
                    rubic[33] = a
                    rubic[30] = b
                    rubic[27] = c
                if morabba == 29 or morabba == 32 or morabba == 35 or morabba == 47 or morabba == 50 or morabba == 53 or morabba == 38 or morabba == 41 or morabba == 44:
                    a = rubic[43]
                    b = rubic[40]
                    c = rubic[37]
                    rubic[43] = rubic[10]
                    rubic[40] = rubic[13]
                    rubic[37] = rubic[16]
                    rubic[10] = rubic[52]
                    rubic[13] = rubic[49]
                    rubic[16] = rubic[46]
                    rubic[52] = rubic[34]
                    rubic[49] = rubic[31]
                    rubic[46] = rubic[28]
                    rubic[34] = a
                    rubic[31] = b
                    rubic[28] = c
                if morabba == 30 or morabba == 33 or morabba == 36 or morabba == 39 or morabba == 42 or morabba == 45 or morabba == 48 or morabba == 51 or morabba == 54:
                    a = rubic[44]
                    b = rubic[41]
                    c = rubic[38]
                    rubic[44] = rubic[9]
                    rubic[41] = rubic[12]
                    rubic[38] = rubic[15]
                    rubic[9]  = rubic[53]
                    rubic[12] = rubic[50]
                    rubic[15] = rubic[47]
                    rubic[53] = rubic[35]
                    rubic[50] = rubic[32]
                    rubic[47] = rubic[29]
                    rubic[35] = a
                    rubic[32] = b
                    rubic[29] = c
                
                    
                    
                    
                    
            if e.key == 100:
                if morabba == 1 or morabba == 2 or morabba == 3 or morabba == 10 or morabba == 11 or morabba == 12 or morabba == 19 or morabba == 20 or morabba == 21 or morabba == 28 or morabba == 29 or morabba == 30:
                    a = rubic[2]
                    b = rubic[1]
                    c = rubic[0]
                    rubic[2]  = rubic[29]
                    rubic[1]  = rubic[28]
                    rubic[0]  = rubic[27]
                    rubic[29] = rubic[20]
                    rubic[28] = rubic[19]
                    rubic[27] = rubic[18]
                    rubic[20] = rubic[11]
                    rubic[19] = rubic[10]
                    rubic[18] = rubic[9]
                    rubic[11] = a
                    rubic[10] = b
                    rubic[9]  = c
                if morabba == 4 or morabba == 5 or morabba == 6 or morabba == 13 or morabba == 14 or morabba == 15 or morabba == 22 or morabba == 23 or morabba == 24 or morabba == 31 or morabba == 32 or morabba == 33:
                    a = rubic[5]
                    b = rubic[4]
                    c = rubic[3]
                    rubic[5]  = rubic[32]
                    rubic[4]  = rubic[31]
                    rubic[3]  = rubic[30]
                    rubic[32] = rubic[23]
                    rubic[31] = rubic[22]
                    rubic[30] = rubic[21]
                    rubic[23] = rubic[14]
                    rubic[22] = rubic[13]
                    rubic[21] = rubic[12]
                    rubic[14] = a
                    rubic[13] = b
                    rubic[12] = c
                if morabba == 7 or morabba == 8 or morabba == 9 or morabba == 16 or morabba == 17 or morabba == 18 or morabba == 25 or morabba == 26 or morabba == 27 or morabba == 34 or morabba == 35 or morabba == 36:
                    a = rubic[8]
                    b = rubic[7]
                    c = rubic[6]
                    rubic[8]  = rubic[35]
                    rubic[7]  = rubic[34]
                    rubic[6]  = rubic[33]
                    rubic[35] = rubic[26]
                    rubic[34] = rubic[25]
                    rubic[33] = rubic[24]
                    rubic[26] = rubic[17]
                    rubic[25] = rubic[16]
                    rubic[24] = rubic[15]
                    rubic[17] = a
                    rubic[16] = b
                    rubic[15] = c
                
                    a = rubic[38]
                    b = rubic[37]
                    c = rubic[36]
                    rubic[38] = rubic[18]
                    rubic[37] = rubic[21]
                    rubic[36] = rubic[24]
                    rubic[18] = rubic[51]
                    rubic[21] = rubic[52]
                    rubic[24] = rubic[53]
                    rubic[51] = rubic[8]
                    rubic[52] = rubic[5]
                    rubic[53] = rubic[2]
                    rubic[8]  = a
                    rubic[5]  = b
                    rubic[2]  = c
                if morabba == 40 or morabba == 41 or morabba == 42:
                    a = rubic[41]
                    b = rubic[40]
                    c = rubic[39]
                    rubic[41] = rubic[19]
                    rubic[40] = rubic[22]
                    rubic[39] = rubic[25]
                    rubic[19] = rubic[48]
                    rubic[22] = rubic[49]
                    rubic[25] = rubic[50]
                    rubic[48] = rubic[7]
                    rubic[49] = rubic[4]
                    rubic[50] = rubic[1]
                    rubic[7]  = a
                    rubic[4]  = b
                    rubic[1]  = c
                if morabba == 43 or morabba == 44 or morabba == 45:
                    a = rubic[44]
                    b = rubic[43]
                    c = rubic[42]
                    rubic[44] = rubic[20]
                    rubic[43] = rubic[23]
                    rubic[42] = rubic[26]
                    rubic[20] = rubic[45]
                    rubic[23] = rubic[46]
                    rubic[26] = rubic[47]
                    rubic[45] = rubic[6]
                    rubic[46] = rubic[3]
                    rubic[47] = rubic[0]
                    rubic[6]  = a
                    rubic[3]  = b
                    rubic[0]  = c
                if morabba == 46 or morabba == 47 or morabba == 48:
                    a = rubic[42]
                    b = rubic[43]
                    c = rubic[44]
                    rubic[42] = rubic[0]
                    rubic[43] = rubic[3]
                    rubic[44] = rubic[6]
                    rubic[0]  = rubic[47]
                    rubic[3]  = rubic[46]
                    rubic[6]  = rubic[45]
                    rubic[47] = rubic[26]
                    rubic[46] = rubic[23]
                    rubic[45] = rubic[20]
                    rubic[26] = a
                    rubic[23] = b
                    rubic[20] = c
                if morabba == 49 or morabba == 50 or morabba == 51:
                    a = rubic[39]
                    b = rubic[40]
                    c = rubic[41]
                    rubic[39] = rubic[1]
                    rubic[40] = rubic[4]
                    rubic[41] = rubic[7]
                    rubic[1]  = rubic[50]
                    rubic[4]  = rubic[49]
                    rubic[7]  = rubic[48]
                    rubic[50] = rubic[25]
                    rubic[49] = rubic[22]
                    rubic[48] = rubic[19]
                    rubic[25] = a
                    rubic[22] = b
                    rubic[19] = c
                if morabba == 52 or morabba == 53 or morabba == 54:
                    a = rubic[36]
                    b = rubic[37]
                    c = rubic[38]
                    rubic[36] = rubic[2]
                    rubic[37] = rubic[5]
                    rubic[38] = rubic[8]
                    rubic[2]  = rubic[53]
                    rubic[5]  = rubic[52]
                    rubic[8]  = rubic[51]
                    rubic[53] = rubic[24]
                    rubic[52] = rubic[21]
                    rubic[51] = rubic[18]
                    rubic[24] = a
                    rubic[21] = b
                    rubic[18] = c
                



            
            pygame.mixer.music.play()
            z = zel_morabba//3
            sc.blit(tabdil(rubic[36]),(fasele//2,fasele//2,z,z))
            sc.blit(tabdil(rubic[37]),(fasele//2+z,fasele//2,z,z))
            sc.blit(tabdil(rubic[38]),(fasele//2+z+z,fasele//2,z,z))
            sc.blit(tabdil(rubic[39]),(fasele//2,fasele//2+z,z,z))
            sc.blit(tabdil(rubic[40]),(fasele//2+z,fasele//2+z,z,z))
            sc.blit(tabdil(rubic[41]),(fasele//2+z+z,fasele//2+z,z,z))
            sc.blit(tabdil(rubic[42]),(fasele//2,fasele//2+z+z,z,z))
            sc.blit(tabdil(rubic[43]),(fasele//2+z,fasele//2+z+z,z,z))
            sc.blit(tabdil(rubic[44]),(fasele//2+z+z,fasele//2+z+z,z,z))

            sc.blit(tabdil(rubic[0]),(3*fasele//2+zel_morabba,fasele//2,z,z))
            sc.blit(tabdil(rubic[1]),(3*fasele//2+zel_morabba+z,fasele//2,z,z))
            sc.blit(tabdil(rubic[2]),(3*fasele//2+zel_morabba+z+z,fasele//2,z,z))
            sc.blit(tabdil(rubic[3]),(3*fasele//2+zel_morabba,fasele//2+z,z,z))
            sc.blit(tabdil(rubic[4]),(3*fasele//2+zel_morabba+z,fasele//2+z,z,z))
            sc.blit(tabdil(rubic[5]),(3*fasele//2+zel_morabba+z+z,fasele//2+z,z,z))
            sc.blit(tabdil(rubic[6]),(3*fasele//2+zel_morabba,fasele//2+z+z,z,z))
            sc.blit(tabdil(rubic[7]),(3*fasele//2+zel_morabba+z,fasele//2+z+z,z,z))
            sc.blit(tabdil(rubic[8]),(3*fasele//2+zel_morabba+z+z,fasele//2+z+z,z,z))

            sc.blit(tabdil(rubic[27]),(5*fasele//2+2*zel_morabba,fasele//2,z,z))
            sc.blit(tabdil(rubic[28]),(5*fasele//2+2*zel_morabba+z,fasele//2,z,z))
            sc.blit(tabdil(rubic[29]),(5*fasele//2+2*zel_morabba+z+z,fasele//2,z,z))
            sc.blit(tabdil(rubic[30]),(5*fasele//2+2*zel_morabba,fasele//2+z,z,z))
            sc.blit(tabdil(rubic[31]),(5*fasele//2+2*zel_morabba+z,fasele//2+z,z,z))
            sc.blit(tabdil(rubic[32]),(5*fasele//2+2*zel_morabba+z+z,fasele//2+z,z,z))
            sc.blit(tabdil(rubic[33]),(5*fasele//2+2*zel_morabba,fasele//2+z+z,z,z))
            sc.blit(tabdil(rubic[34]),(5*fasele//2+2*zel_morabba+z,fasele//2+z+z,z,z))
            sc.blit(tabdil(rubic[35]),(5*fasele//2+2*zel_morabba+z+z,fasele//2+z+z,z,z))

            sc.blit(tabdil(rubic[9]) ,(fasele//2,3*fasele//2+zel_morabba,z,z))
            sc.blit(tabdil(rubic[10]),(fasele//2+z,3*fasele//2+zel_morabba,z,z))
            sc.blit(tabdil(rubic[11]),(fasele//2+z+z,3*fasele//2+zel_morabba,z,z))
            sc.blit(tabdil(rubic[12]),(fasele//2,3*fasele//2+zel_morabba+z,z,z))
            sc.blit(tabdil(rubic[13]),(fasele//2+z,3*fasele//2+zel_morabba+z,z,z))
            sc.blit(tabdil(rubic[14]),(fasele//2+z+z,3*fasele//2+zel_morabba+z,z,z))
            sc.blit(tabdil(rubic[15]),(fasele//2,3*fasele//2+zel_morabba+z+z,z,z))
            sc.blit(tabdil(rubic[16]),(fasele//2+z,3*fasele//2+zel_morabba+z+z,z,z))
            sc.blit(tabdil(rubic[17]),(fasele//2+z+z,3*fasele//2+zel_morabba+z+z,z,z))

            sc.blit(tabdil(rubic[18]),(3*fasele//2+zel_morabba,3*fasele//2+zel_morabba,z,z))
            sc.blit(tabdil(rubic[19]),(3*fasele//2+zel_morabba+z,3*fasele//2+zel_morabba,z,z))
            sc.blit(tabdil(rubic[20]),(3*fasele//2+zel_morabba+z+z,3*fasele//2+zel_morabba,z,z))
            sc.blit(tabdil(rubic[21]),(3*fasele//2+zel_morabba,3*fasele//2+zel_morabba+z,z,z))
            sc.blit(tabdil(rubic[22]),(3*fasele//2+zel_morabba+z,3*fasele//2+zel_morabba+z,z,z))
            sc.blit(tabdil(rubic[23]),(3*fasele//2+zel_morabba+z+z,3*fasele//2+zel_morabba+z,z,z))
            sc.blit(tabdil(rubic[24]),(3*fasele//2+zel_morabba,3*fasele//2+zel_morabba+z+z,z,z))
            sc.blit(tabdil(rubic[25]),(3*fasele//2+zel_morabba+z,3*fasele//2+zel_morabba+z+z,z,z))
            sc.blit(tabdil(rubic[26]),(3*fasele//2+zel_morabba+z+z,3*fasele//2+zel_morabba+z+z,z,z))
                        
            sc.blit(tabdil(rubic[45]),(5*fasele//2+2*zel_morabba,3*fasele//2+zel_morabba,z,z))
            sc.blit(tabdil(rubic[46]),(5*fasele//2+2*zel_morabba+z,3*fasele//2+zel_morabba,z,z))
            sc.blit(tabdil(rubic[47]),(5*fasele//2+2*zel_morabba+z+z,3*fasele//2+zel_morabba,z,z))
            sc.blit(tabdil(rubic[48]),(5*fasele//2+2*zel_morabba,3*fasele//2+zel_morabba+z,z,z))
            sc.blit(tabdil(rubic[49]),(5*fasele//2+2*zel_morabba+z,3*fasele//2+zel_morabba+z,z,z))
            sc.blit(tabdil(rubic[50]),(5*fasele//2+2*zel_morabba+z+z,3*fasele//2+zel_morabba+z,z,z))
            sc.blit(tabdil(rubic[51]),(5*fasele//2+2*zel_morabba,3*fasele//2+zel_morabba+z+z,z,z))
            sc.blit(tabdil(rubic[52]),(5*fasele//2+2*zel_morabba+z,3*fasele//2+zel_morabba+z+z,z,z))
            sc.blit(tabdil(rubic[53]),(5*fasele//2+2*zel_morabba+z+z,3*fasele//2+zel_morabba+z+z,z,z))
            pygame.display.update()
            
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#THE END
