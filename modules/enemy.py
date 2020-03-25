################ IMPORTING MODULES ###################
import sys
from os import system
from modules.screen import *
######################################################

class enemy:
    enemies = []

    enemy_img = []
    boss_img = []

    intheair = True

    def __init__(self):

        for i in range(2):
            row = []
            for j in range(4):
                row.append(" ")
            self.enemy_img.append(row)

        self.enemy_img[0][0] = "<"
        self.enemy_img[0][1] = "@"
        self.enemy_img[0][2] = "@"
        self.enemy_img[0][3] = ">"
        self.enemy_img[1][0] = "{"
        self.enemy_img[1][3] = "}"

        for i in range(4):
            row = []
            for j in range(4):
                row.append(" ")
            self.boss_img.append(row)

        self.boss_img[0][0] = "!"
        self.boss_img[0][1] = "!"
        self.boss_img[0][2] = "!"
        self.boss_img[0][3] = "!"
        self.boss_img[1][0] = "*"
        self.boss_img[1][1] = "@"
        self.boss_img[1][2] = "@"
        self.boss_img[1][3] = "*"
        self.boss_img[2][0] = "<"
        self.boss_img[2][1] = "^"
        self.boss_img[2][2] = "^"
        self.boss_img[2][3] = ">"
        self.boss_img[3][0] = "{"
        self.boss_img[3][3] = "}"



    def moveenemy(self,scrobj,score,level,mary,moves=1,mv=0):
        if moves%(80-level*5) == 0:
            self.enemies.append([self.enemy_img,31,110,1,"small",level])
        elif moves%(50+level*50) == 0:
            self.enemies.append([self.boss_img,31,110,1,"boss",5+level])

        for element in self.enemies:
            clry = element[2]-1
            clrx = element[1]-1

            #erasing previous content
            if element[4] == "small":
                for i in range(2):
                    for j in range(4):
                        if scrobj.scr[clrx+i][clry+j] != "#" and scrobj.scr[clrx+i][clry+j] != "|" and scrobj.scr[clrx+i][clry+j] != "X":
                            scrobj.scr[clrx+i][clry+j] = " "
                if element[2] < 2:
                    self.enemies.remove(element)
                elif (scrobj.scr[element[1]-1][element[2]-2] == "*") or (scrobj.scr[element[1]][element[2]-2] == "*") or (scrobj.scr[element[1]-2][element[2]] == "M") or (scrobj.scr[element[1]-2][element[2]+1] == "M"):
                    element[5] = element[5]-1
                    if element[5] <= 0:
                        score = score + 150
                        self.enemies.remove(element)

            elif element[4] == "boss":
                for i in range(4):
                    for j in range(4):
                        if scrobj.scr[clrx+i-2][clry+j] != "#" and scrobj.scr[clrx+i-2][clry+j] != "|" and scrobj.scr[clrx+i-2][clry+j] != "X":
                            scrobj.scr[clrx+i-2][clry+j] = " "
                if element[2] < 2:
                    self.enemies.remove(element)
                elif (scrobj.scr[element[1]-1][element[2]-2] == "*") or (scrobj.scr[element[1]][element[2]-2] == "*") or (scrobj.scr[element[1]-2][element[2]-2] == "*") or (scrobj.scr[element[1]-3][element[2]-2] == "*"):
                    element[5] = element[5]-1
                    if element[5] <= 0:
                        score = score + 300
                        self.enemies.remove(element)



        for element in self.enemies:
            if element[4] == "small":
                if element[2]>145 or (scrobj.scr[element[1]][element[2]+3] == "|" or scrobj.scr[element[1]+1][element[2]+3] == "|" or scrobj.scr[element[1]-1][element[2]+3] == "|" or element[2] > 105):
                    element[3] = 1
                elif (scrobj.scr[element[1]][element[2]-2] == "|" or scrobj.scr[element[1]+1][element[2]-2] == "|" or scrobj.scr[element[1]-1][element[2]-2] == "|" or element[2] > 105):
                    element[3] = 2

                if element[3] == 1:
                    element[2] = element[2]-1+mv
                elif element[3] == 2:
                    element[2] = element[2]+1

            else:
                if mary >= element[2]:
                    if (scrobj.scr[element[1]][element[2]+3] == "|" or scrobj.scr[element[1]+1][element[2]+3] == "|" or scrobj.scr[element[1]-1][element[2]+3] == "|") or element[2] > 110:
                        pass
                    else:
                        element[2] = element[2]+1
                elif mary < element[2]:
                    if (scrobj.scr[element[1]][element[2]-2] == "|" or scrobj.scr[element[1]+1][element[2]-2] == "|" or scrobj.scr[element[1]-1][element[2]-2] == "|"):
                        pass
                    else:
                        element[2] = element[2]-1+mv


            #To paste enemy
            bufx = element[1]-1
            bufy = element[2]-1


            #Pasting mario
            if element[4] == "small":
                for i in range(2):
                    for j in range(4):
                        if scrobj.scr[bufx+i-1][bufy+j] != "#" and scrobj.scr[bufx+i-1][bufy+j] != "|" and scrobj.scr[bufx+i-1][bufy+j] != "X":
                            scrobj.scr[bufx+i][bufy+j] = element[0][i][j]
            elif element[4] == "boss":
                for i in range(4):
                    for j in range(4):
                        if scrobj.scr[bufx+i-2][bufy+j] != "#" and scrobj.scr[bufx+i-2][bufy+j] != "|" and scrobj.scr[bufx+i-2][bufy+j] != "X":
                            scrobj.scr[bufx+i-2][bufy+j] = element[0][i][j]

        return score
