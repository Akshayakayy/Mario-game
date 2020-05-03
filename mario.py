"""This is the main module where the main code of the game control happens."""
# IMPORTING MODULES
import sys
import time
import os
from modules.object import Wall, Pipe, Flag, Gem
from modules.player import Player
from modules.enemy import Enemy
from modules.screen import Screen
from modules.kbhit import KBHit, kbhit, getch
# GAME OBJECTS
MAR = Player()
ENEMYOBJ = Enemy()
GEMOBJ = Gem()
WALLOBJ = Wall()
PIPEOBJ = Pipe()
FLAGOBJ = Flag()

LASTTIME = time.time()
KB = KBHit()

# SETTING SCENE
SCROBJ = Screen()
SCROBJ.setscene()

# GAME VARIABLES
SCORE = 0
TIMER = 0
LEVEL = 1

FLAGF = 0
C = 0
F = 1
END = 0
RESTART = 0
os.system("aplay "+str("./modules/mb_new.wav"))

# CONTROLS
while True:
    sys.stdout.write("\033c")

    if TIMER == 10:
        SCORE = SCORE + 1
        TIMER = 0

    TIMER = TIMER + 1

    SCROBJ.scr[1][92:101] = str(SCORE)
    SCROBJ.scr[1][61] = str(MAR.lives)
    SCROBJ.scr[1][46] = str(LEVEL)

    SCROBJ.printscr()
    print(MAR.moves)
    time.sleep(0.1)

    LASTTIME = time.time()

    if MAR.lives <= 0:
        os.system("aplay "+str("./modules/mb_die.wav"))
        break

    if kbhit():
        ch = getch()

        # RIGHT
        if ch == "d":
            if (SCROBJ.scr[MAR.xcor][MAR.ycor+2] == "|" or
                    SCROBJ.scr[MAR.xcor+1][MAR.ycor+2] == "|" or
                    SCROBJ.scr[MAR.xcor-1][MAR.ycor+2] == "|"):
                MAR.movemario(SCROBJ, "d", -1)
            elif (MAR.ycor > 70 and
                  (SCROBJ.scr[MAR.xcor][MAR.ycor+2] != "|" or
                   SCROBJ.scr[MAR.xcor+1][MAR.ycor+2] != "|" or
                   SCROBJ.scr[MAR.xcor-1][MAR.ycor+2] != "|")):
                SCROBJ.setscene()
                MAR.movemario(SCROBJ, "d", -1)
                PIPEOBJ.updatelist(SCROBJ, MAR.moves)
                WALLOBJ.updatelist(SCROBJ)
                SCORE = ENEMYOBJ.moveenemy(SCROBJ, SCORE, LEVEL, MAR.ycor, MAR.moves, -1)
                SCORE = GEMOBJ.updatelist(SCROBJ, SCORE, MAR.moves, 1)
                FLAGOBJ.updatelist(SCROBJ, LEVEL, MAR)
            else:
                MAR.movemario(SCROBJ, "d")

        # LEFT
        elif ch == "a":
            if (MAR.ycor < 33 or
                    SCROBJ.scr[MAR.xcor][MAR.ycor-2] == "|" or
                    SCROBJ.scr[MAR.xcor-1][MAR.ycor-2] == "|" or
                    SCROBJ.scr[MAR.xcor+1][MAR.ycor-2] == "|"):
                MAR.movemario(SCROBJ, "a", 1)
            else:
                MAR.movemario(SCROBJ, "a")
            SHOOTCH = "a"

        # JUMP
        elif ch == "w":
            if MAR.intheair == False:
                if SCROBJ.scr[MAR.xcor+2][MAR.ycor] == "X":
                    C = 5
                elif SCROBJ.scr[MAR.xcor+2][MAR.ycor] == "|":
                    C = 9
                os.system("aplay "+str("./modules/mb_jump.wav"))
                C = MAR.jump(SCROBJ, C)

        # SHOOT
        elif ch == "b":
            MAR.shooting(SCROBJ, "b")

        # QUIT
        elif ch == "q":
            os.system("aplay "+str("./modules/mb_die.wav"))
            break

    else:
        SCORE = GEMOBJ.updatelist(SCROBJ, SCORE, MAR.moves)

    # GRAVITY EFFECTS
    if MAR.top:
        MAR.gravity(SCROBJ)
    elif MAR.intheair:
        C = MAR.jump(SCROBJ, C)

    # ENEMY MOVEMENT
    SCORE = ENEMYOBJ.moveenemy(SCROBJ, SCORE, LEVEL, MAR.ycor)
    MAR.lifecheck(SCROBJ)
    MAR.shooting(SCROBJ)

    # CHECKPOINT AND NEXT LEVEL
    if END == 0:
        END = FLAGOBJ.checkend(SCROBJ)

    if END:
        RESTART = FLAGOBJ.lowerflag(SCROBJ)
        if RESTART:
            LEVEL = LEVEL+1
            SCORE = SCORE + 500
            MAR.moves = 1
            FLAGOBJ.remove(SCROBJ)
            time.sleep(1)
            FLAGF = 0
            C = 0
            F = 1
            END = 0
            RESTART = 0

# GAME ENDS
sys.stdout.write("\033c")
print("GAME OVER!")
print("SCORE: " + str(SCORE))
print("LEVEL: " + str(LEVEL))
