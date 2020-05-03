"""This module contains all information about the player, Mario."""
# IMPORTING MODULES
import os


class Player(object):
    """This class contains the attributes and functions of player."""
    xcor = 10
    ycor = 40

    moves = 1

    s_img = []
    b_img = []

    bullets = []

    lives = 5

    intheair = True
    top = True

    def __init__(self):
        """This method is a constructor, sets player image."""
        for i in range(3):
            row = []
            for j in range(3):
                row.append(" ")
            self.s_img.append(row)

        self.s_img[0][1] = "O"
        self.s_img[1][0] = "/"
        self.s_img[1][1] = "M"
        self.s_img[1][2] = "\\"
        self.s_img[2][0] = "/"
        self.s_img[2][2] = "\\"

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

    def movemario(self, scrobj, ch, mv=0):
        """This method updates Mario's position according to surroundings."""
        self.moves = self.moves + 1

        clry = self.ycor-1
        clrx = self.xcor-1

        for i in range(3):
            for j in range(3):
                if scrobj.scr[clrx+i][clry+j] != "X":
                    scrobj.scr[clrx+i][clry+j] = " "

        if ch == "d":
            self.ycor = self.ycor+1+mv
        elif ch == "a":
            self.ycor = self.ycor-1+mv

        if (self.intheair == False and
                (scrobj.scr[self.xcor+2][self.ycor] != "X" or
                 scrobj.scr[self.xcor+2][self.ycor] != "|")):
            self.top = True
            self.intheair = True

        # To paste mario
        bufx = self.xcor-1
        bufy = self.ycor-1

        # To flip/change hands
        if ch == "d":
            self.s_img[1][0] = " "
            self.s_img[1][2] = "\\"
        elif ch == "a":
            self.s_img[1][2] = " "
            self.s_img[1][0] = "/"

        # Pasting mario
        for i in range(3):
            for j in range(3):
                scrobj.scr[bufx+i][bufy+j] = self.s_img[i][j]

    def gravity(self, scrobj):
        """This method gives the gravity effect by increasing Mario's y coordinate."""
        flag = 1

        if (self.xcor+2 > 33 or scrobj.scr[self.xcor+2][self.ycor] == "X" or
                scrobj.scr[self.xcor+2][self.ycor] == "|" or
                scrobj.scr[self.xcor+2][self.ycor+1] == "X" or
                scrobj.scr[self.xcor+2][self.ycor+1] == "|" or
                scrobj.scr[self.xcor+2][self.ycor-1] == "X" or
                scrobj.scr[self.xcor+2][self.ycor-1] == "|"):
            self.intheair = False
            self.top = False
            flag = 0

        clry = self.ycor-1
        clrx = self.xcor-1

        for i in range(3):
            for j in range(3):
                if scrobj.scr[clrx+i][clry+j] != "X":
                    scrobj.scr[clrx+i][clry+j] = " "

        # To make mario go to ground
        if flag == 1:
            self.xcor = self.xcor+1

        # To paste mario
        bufx = self.xcor-1
        bufy = self.ycor-1

        # Pasting mario
        for i in range(3):
            for j in range(3):
                scrobj.scr[bufx+i][bufy+j] = (self.s_img[i][j])

    def jump(self, scrobj, c):
        """This method gives the jump effect by decreasing Mario's y coordinate."""
        flag = 1
        self.intheair = True

        if c <= 0:
            self.top = True

        if (scrobj.scr[self.xcor-2][self.ycor] == "X" or
                scrobj.scr[self.xcor-2][self.ycor] == "|" or
                scrobj.scr[self.xcor-2][self.ycor+1] == "X" or
                scrobj.scr[self.xcor-2][self.ycor+1] == "|" or
                scrobj.scr[self.xcor-2][self.ycor-1] == "X" or
                scrobj.scr[self.xcor-2][self.ycor-1] == "|"):
            self.top = True
            flag = 0

        clry = self.ycor-1
        clrx = self.xcor-1

        for i in range(3):
            for j in range(3):
                if scrobj.scr[clrx+i][clry+j] != "X":
                    scrobj.scr[clrx+i][clry+j] = " "

        self.s_img[1][2] = "\\"
        self.s_img[1][0] = "/"

        if flag == 1:
            self.xcor = self.xcor-1

        # To paste mario
        bufx = self.xcor-1
        bufy = self.ycor-1

        # Pasting mario
        for i in range(3):
            for j in range(3):
                scrobj.scr[bufx+i][bufy+j] = self.s_img[i][j]

        return c-1

    def shooting(self, scrobj, ch="m"):
        """This method generates and updates bullets' positions."""
        if ch == "b":
            self.bullets.append([self.xcor, self.ycor+2])

        for bullet in self.bullets:
            bullet[1] = bullet[1] + 1

        if len(self.bullets) >= 1:
            for bullet in self.bullets:
                if bullet[1] > 110 or bullet[1] < 5 or scrobj.scr[bullet[0]][bullet[1]] != " ":
                    scrobj.scr[bullet[0]][bullet[1]-1] = " "
                    self.bullets.remove(bullet)

        # removing previous position & pasting new bullet position
        for bullet in self.bullets:
            scrobj.scr[bullet[0]][bullet[1]-1] = " "
            scrobj.scr[bullet[0]][bullet[1]] = "*"

    def lifecheck(self, scrobj):
        """This method checks the player's life."""
        if scrobj.scr[self.xcor][self.ycor+2] == "@":
            self.lives = self.lives - 1
            os.system("aplay "+str("./modules/mb_touch.wav"))
        elif scrobj.scr[self.xcor-1][self.ycor+2] == "@":
            self.lives = self.lives - 2
            os.system("aplay " + str("./modules/mb_touch.wav"))
