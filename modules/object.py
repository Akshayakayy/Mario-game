################ IMPORTING MODULES ###################
import sys
from os import system
from modules.screen import *
import time
######################################################

class object:
    def __init__(self,n,m,c):
        self.img = []
        self.listofobjs = []
        self.countdown = c
        self.n=n
        self.m=m

        for i in range(n):
            row = []
            for j in range(m):
                row.append(" ")
            self.img.append(row)

    def updatelist(self,scrobj):
        pass

    def updating(self,scrobj,num):
        for i in self.listofobjs:
            i[num] = i[num] - 1

            if i[num] < 10:
                self.listofobjs.remove(i)

    def cutandupdate(self,scrobj):
        for i in self.listofobjs:
            img = i[0]
            xcor = i[1]
            ycor = i[2]

            for i in range(self.n):
                for j in range(self.m):
                    if scrobj.scr[xcor-i+1][ycor+j+1] != "#":
                        scrobj.scr[xcor-i+1][ycor+j+1] = " "
                    if scrobj.scr[xcor-i+1][ycor+j] != "#":
                        scrobj.scr[xcor-i+1][ycor+j] = self.img[i][j]



################### CLASS WALL INHERITED FROM OBJECT ##################
class wall(object):

    def __init__(self):
        super(wall,self).__init__(1,5,15)

        self.img[0][0] = "|"
        self.img[0][1] = "X"
        self.img[0][2] = "X"
        self.img[0][3] = "X"
        self.img[0][4] = "|"

    def updatelist(self,scrobj):
        if self.countdown == 15:
            self.listofobjs.append([self.img,random.randint(21,24),110])
            self.listofobjs.append([self.img,random.randint(21,24),120])

        if self.countdown == 1:
            self.listofobjs.append([self.img,random.randint(21,24),120])
            self.countdown = random.randint(30,55)
        else:
            self.countdown = self.countdown - 1

        self.updating(scrobj,2)
        self.cutandupdate(scrobj)

################### CLASS PIPE INHERITED FROM OBJECT ##################
class pipe(object):

    def __init__(self):
        super(pipe,self).__init__(3,8,20)

        self.img[0][0:0 + 8] = ("|" for _ in range(8))
        self.img[1][0:0 + 8] = ("|" for _ in range(8))
        self.img[2][0:0 + 8] = ("|" for _ in range(8))

    def updatelist(self,scrobj,moves=1):
        if self.countdown == 40:
            self.listofobjs.append([self.img,30,120])

        if moves%59 == 0:
            self.listofobjs.append([self.img,30,120])
        else:
            self.countdown = self.countdown - 1

        self.updating(scrobj,2)
        self.cutandupdate(scrobj)

################### CLASS FLAG INHERITED FROM OBJECT ##################
class flag(object):
    y = 150

    def __init__(self):
        super(flag,self).__init__(20,8,20)

        self.img[0][0] = "|"
        self.img[1][0] = "|"
        self.img[2][0] = "|"
        self.img[3][0] = "|"
        self.img[4][0] = "|"
        self.img[5][0] = "|"
        self.img[6][0] = "|"
        self.img[7][0] = "|"
        self.img[8][0] = "|"
        self.img[9][0] = "|"
        self.img[10][0] = "|"
        self.img[11][0] = "|"
        self.img[12][0] = "|"
        self.img[13][0] = "|"
        self.img[14][0] = "|"
        self.img[15][0] = "|"
        self.img[16][0] = "|"
        self.img[17][0] = "|"
        self.img[18][0] = "|"
        self.img[19][0] = "|"

        self.img[0][1:1 + 6] = ("=" for _ in range(6))
        self.img[1][1:1 + 6] = ("=" for _ in range(6))
        self.img[2][1:1 + 6] = ("=" for _ in range(6))

    def updatelist(self,scrobj,score,level,mar):
        moves = mar.moves
        self.y = mar.y + 50


        if moves%(50+level*50) == 0:
            self.listofobjs.append([12,self.y])

        self.updating(scrobj,1)
        self.cutandupdate(scrobj)

    def cutandupdate(self,scrobj):
        for flag in self.listofobjs:
            xcor = flag[0]
            ycor = flag[1]

            for i in range(self.n):
                for j in range(self.m):
                    if scrobj.scr[12+i][ycor+j+1] != "#":
                        scrobj.scr[12+i][ycor+j+1] = " "
                    if scrobj.scr[12+i][ycor+j] != "#":
                        scrobj.scr[12+i][ycor+j] = self.img[i][j]

    def remove(self,scrobj):
        for flag in self.listofobjs:
            xcor = 12
            ycor = flag[1]-1

            for i in range(20):
                for j in range(8):
                    if scrobj.scr[xcor+i][ycor+j+1] != "#":
                        scrobj.scr[xcor+i][ycor+j+1] = " "
            self.listofobjs.remove(flag)

    def checkend(self,scrobj):
        for i in self.listofobjs:
            for j in range(10):
                if scrobj.scr[31-j][i[1]-1] == "\\":
                    return 1

        return 0

    def lowerflag(self,scrobj):
        for flag in self.listofobjs:
            xcor = flag[0]
            ycor = flag[1]+1


            for i in range(3):
                for j in range(7):
                    scrobj.scr[xcor+i][ycor+j] = " "

            for i in range(3):
                for j in range(7):
                    scrobj.scr[xcor+1+i][ycor+j-1] = self.img[i][j]

            flag[0] = flag[0] + 1

            if flag[0] > 28:
                return 1

        return 0

################### CLASS GEM INHERITED FROM OBJECT ##################
class gem(object):

    def __init__(self):
        super(gem,self).__init__(1,1,15)

    def updatelist(self,scrobj,score,mv=0):
        if self.countdown == 1:
            self.listofobjs.append([9,115])
            self.countdown = random.randint(40,95)
        else:
            self.countdown = self.countdown - 1

        for i in self.listofobjs:
            while (scrobj.scr[i[0]+1][i[1]]) == " ":
                i[0] = i[0] + 1

            i[1] = i[1] - mv

            if scrobj.scr[i[0]][i[1]-1] == "/" or scrobj.scr[i[0]][i[1]+1] == "\\" or scrobj.scr[i[0]][i[1]+1] == "/" or scrobj.scr[i[0]][i[1]-1] == "\\":
                for sound in range(1,2):
                    sys.stdout.write('\r\a{s}'.format(s=sound))
                score = score + 50
                if scrobj.scr[i[0]][i[1]+1] != "#" and scrobj.scr[i[0]][i[1]+1] != "X" and scrobj.scr[i[0]][i[1]+1] != "|":
                    scrobj.scr[i[0]][i[1]+1] = " "
                self.listofobjs.remove(i)


            if i[1] < 10:
                self.listofobjs.remove(i)

        for i in self.listofobjs:
            xcor = i[0]
            ycor = i[1]

            if scrobj.scr[xcor][ycor+1] != "#" and scrobj.scr[xcor][ycor+1] != "X" and scrobj.scr[xcor][ycor+1] != "|":
                scrobj.scr[xcor][ycor+1] = " "
            if scrobj.scr[xcor][ycor] != "#":
                scrobj.scr[xcor][ycor] = "$"

        return score
