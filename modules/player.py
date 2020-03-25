################ IMPORTING MODULES ###################
import sys
from os import system
from modules.screen import *
from .config import *
import os
######################################################

class player:
    x = 10
    y = 40

    moves = 1

    s_img = []
    b_img = []

    bullets = []

    lives = 5

    intheair = True
    top = True

    def __init__(self):

        for i in range(3):
            row = []
            for j in range(3):
                row.append(" ")
            self.s_img.append(row)

        self.s_img[0][1] = "O"
        self.s_img[1][0] = "/"#,'White')
        self.s_img[1][1] = "M"#,'Red')
        self.s_img[1][2] = "\\"#,'White')
        self.s_img[2][0] = "/"#,'Blue')
        self.s_img[2][2] = "\\"#,'Blue')

        for i in range(3):
            row = []
            for j in range(3):
                row.append(" ")
            self.b_img.append(row)

        self.b_img[0][1] = "O"
        self.b_img[1][0] = "/"
        self.b_img[1][1] = "S"
        self.b_img[1][2] = "\\"
        self.b_img[2][0] = "/"
        self.b_img[2][2] = "\\"


    def movemario(self,scrobj,ch,mv=0):

        self.moves = self.moves + 1

        clry = self.y-1
        clrx = self.x-1

        for i in range(3):
            for j in range(3):
                if scrobj.scr[clrx+i][clry+j] != "X":
                    scrobj.scr[clrx+i][clry+j] = " "

        if ch == "d":
            self.y = self.y+1+mv
        elif ch == "a":
            self.y = self.y-1+mv

        if self.intheair == False and (scrobj.scr[self.x+2][self.y] != "X" or scrobj.scr[self.x+2][self.y] != "|"):
            self.top = True
            self.intheair = True

        #To paste mario
        bufx = self.x-1
        bufy = self.y-1

        #To flip/change hands
        if ch == "d":
            self.s_img[1][0] = " "
            self.s_img[1][2] = "\\"#,'White')
        elif ch == "a":
            self.s_img[1][2] = " "
            self.s_img[1][0] = "/"#,'White')


        #Pasting mario
        for i in range(3):
            for j in range(3):
                scrobj.scr[bufx+i][bufy+j] = self.s_img[i][j]

    def gravity(self,scrobj):
        flag = 1

        if self.x+2>33 or scrobj.scr[self.x+2][self.y] == "X" or scrobj.scr[self.x+2][self.y] == "|" or scrobj.scr[self.x+2][self.y+1] == "X" or scrobj.scr[self.x+2][self.y+1] == "|" or scrobj.scr[self.x+2][self.y-1] == "X" or scrobj.scr[self.x+2][self.y-1] == "|":
                self.intheair = False
                self.top = False
                flag = 0

        clry = self.y-1
        clrx = self.x-1

        for i in range(3):
            for j in range(3):
                if scrobj.scr[clrx+i][clry+j] != "X":
                    scrobj.scr[clrx+i][clry+j] = " "

        #To make mario go to ground
        if flag == 1:
            self.x = self.x+1

        #To paste mario
        bufx = self.x-1
        bufy = self.y-1

        #Pasting mario
        for i in range(3):
            for j in range(3):
                scrobj.scr[bufx+i][bufy+j] = (self.s_img[i][j])

    def jump(self,scrobj,c):
        flag = 1
        self.intheair = True

        if c<=0:
            self.top = True

        if scrobj.scr[self.x-2][self.y] == "X" or scrobj.scr[self.x-2][self.y] == "|" or scrobj.scr[self.x-2][self.y+1] == "X" or scrobj.scr[self.x-2][self.y+1] == "|" or scrobj.scr[self.x-2][self.y-1] == "X" or scrobj.scr[self.x-2][self.y-1] == "|":
            self.top = True
            flag = 0

        clry = self.y-1
        clrx = self.x-1

        for i in range(3):
            for j in range(3):
                if scrobj.scr[clrx+i][clry+j] != "X":
                    scrobj.scr[clrx+i][clry+j] = " "

        self.s_img[1][2] = "\\"#,'White')
        self.s_img[1][0] = "/"#,'White')

        if flag == 1:
            self.x = self.x-1

        #To make mario go higher
        #if flag == 1:
        #    self.x = self.x+1

        #To paste mario
        bufx = self.x-1
        bufy = self.y-1

        #Pasting mario
        for i in range(3):
            for j in range(3):
                scrobj.scr[bufx+i][bufy+j] = self.s_img[i][j]

        return c-1

    def shooting(self,scrobj,ch="m"):

        if ch == "b":
            self.bullets.append([self.x,self.y+2])

        for bullet in self.bullets:
            bullet[1] = bullet[1] + 1

        if len(self.bullets) >= 1:
            for bullet in self.bullets:
                if bullet[1] > 110 or bullet[1] < 5 or scrobj.scr[bullet[0]][bullet[1]] != " ":
                    scrobj.scr[bullet[0]][bullet[1]-1] = " "
                    self.bullets.remove(bullet)

        #removing previous position & pasting new bullet position
        for bullet in self.bullets:
            scrobj.scr[bullet[0]][bullet[1]-1] = " "
            scrobj.scr[bullet[0]][bullet[1]] = "*"

    def lifecheck(self,scrobj):
        if scrobj.scr[self.x][self.y+2] == "@":
            self.lives = self.lives -1
            os.system("aplay "+str("./modules/mb_touch.wav"))
        elif scrobj.scr[self.x-1][self.y+2] == "@":
            self.lives = self.lives - 2
            os.system("aplay "+str("./modules/mb_touch.wav"))
