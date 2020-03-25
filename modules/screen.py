################ IMPORTING MODULES ###################
import sys
from os import system
import random
from .config import *
######################################################

class screen:
    scr = []

    #cloud variables
    cloudimg = []
    climg1 = []
    climg2 = []
    climg3 = []
    clouds = []
    cloudcountdown = 8

    def __init__(self):
        for i in range(35):
            row = []
            for j in range(150):
                if i == 0 or i == 2 or i == 34:
                    row.append("#")
                elif (j == 30 or j== 109) and i != 1:
                    row.append("#")
                else:
                    row.append(" ")
            self.scr.append(row)


        self.scr[1][53:60] = "LIVES: "
        self.scr[1][83:90] = "SCORE: "
        self.scr[1][38:45] = "LEVEL: "

        for i in range(3):
            row = []
            for j in range(7):
                row.append(" ")
            self.climg1.append(row)

        for i in range(4):
            row = []
            for j in range(11):
                row.append(" ")
            self.climg2.append(row)

        for i in range(3):
            row = []
            for j in range(9):
                row.append(" ")
            self.climg3.append(row)

        self.climg1[0][4] = "_"
        self.climg1[1][3] = "("
        self.climg1[1][5] = ")"
        self.climg1[1][1:1 + 2] = ("_" for i in range(2))
        self.climg1[1][6] = "_"
        self.climg1[2][0] = "("
        self.climg1[2][1:1 + 5] = ("_" for i in range(5))
        self.climg1[2][6] = ")"

        self.climg2[3][0] = "("
        self.climg2[3][1:1 + 9] = ("_" for i in range(9))
        self.climg2[3][10] = ")"
        self.climg2[2][1] = "_"
        self.climg2[2][2] = "("
        self.climg2[2][8] = ")"
        self.climg2[2][9] = "_"
        self.climg2[1][3] = "_"
        self.climg2[1][4] = "("
        self.climg2[1][6] = ")"
        self.climg2[1][7] = "_"
        self.climg2[0][5] = "_"

        self.climg3[2][0] = "("
        self.climg3[2][1:1 + 7] = ("_" for i in range(7))
        self.climg3[2][8] = ")"
        self.climg3[1][1] = "_"
        self.climg3[1][2] = "("
        self.climg3[1][6] = ")"
        self.climg3[1][7] = "_"
        self.climg3[0][3:3 + 3] = ("_" for i in range(3))

        self.cloudimg.append([self.climg1,3,7])
        self.cloudimg.append([self.climg2,4,11])
        self.cloudimg.append([self.climg3,3,9])

    def printscr(self):
        for row in self.scr:
            r = (''.join(row))[30:110]
            for col in r:
                printcc(col)
            sys.stdout.write('\n')

    def setscene(self):
        if self.cloudcountdown == 8:
            self.clouds.append([self.cloudimg[2],random.randint(3,4),120])
        if self.cloudcountdown == 1:
            self.clouds.append([self.cloudimg[random.randint(0,2)],random.randint(3,4),120])
            self.cloudcountdown = random.randint(25,40)
        else:
            self.cloudcountdown = self.cloudcountdown - 1

        for i in self.clouds:
            i[2] = i[2] - 1

            if i[2] < 2:
                self.clouds.remove(i)

        for i in self.clouds:
            row = i[0][1]
            col = i[0][2]
            ycor = i[2]
            xcor = i[1]
            img = i[0][0]

            for i in range(row):
                for j in range(col):
                    if self.scr[xcor+i][ycor+j+1] != "#":
                        self.scr[xcor+i][ycor+j+1] = " "
                    if self.scr[xcor+i][ycor+j] != "#":
                        self.scr[xcor+i][ycor+j] = img[i][j]

        #ground
        self.scr[-3][1:1 + 138]= ("X" for i in range(138))
        self.scr[-2][1:1 + 138]= ("X" for i in range(138))
