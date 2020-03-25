############## IMPORTING MODULES #################
from os import system
from modules.object import *
from modules.player import *
from modules.enemy import *
from modules.screen import *
from modules.config import *
import tty
import sys
import termios
from modules.kbhit import *
import time

################## GAME OBJECTS ###################
mar = player()
enemyobj = enemy()
gemobj = gem()
wallobj = wall()
pipeobj = pipe()
flagobj = flag()

lastTime = time.time()
kb = KBHit()

################# SETTING SCENE #################
scrobj = screen()
scrobj.setscene()

################# GAME VARIABLES #################
score = 0
timer = 0
level = 1

flagf=0
c=0
f=1
end = 0
restart = 0
os.system("aplay "+str("./modules/mb_new.wav"))
################### CONTROLS #####################
while True:
    sys.stdout.write("\033c")

    if timer == 10:
        score = score + 1
        timer = 0

    timer = timer + 1

    scrobj.scr[1][92:101] = str(score)
    scrobj.scr[1][61] = str(mar.lives)
    scrobj.scr[1][46] = str(level)

    scrobj.printscr()
    print(mar.moves)
    time.sleep(0.1)

    lastTime=time.time()

    if mar.lives<=0:
        os.system("aplay "+str("./modules/mb_die.wav"))
        break

    if kb.kbhit():
        ch = kb.getch()

        ############ RIGHT #############
        if ch == "d":
            if scrobj.scr[mar.x][mar.y+2] == "|" or scrobj.scr[mar.x+1][mar.y+2] == "|" or scrobj.scr[mar.x-1][mar.y+2] == "|":
                mar.movemario(scrobj,"d",-1)
            elif mar.y > 70 and (scrobj.scr[mar.x][mar.y+2] != "|" or scrobj.scr[mar.x+1][mar.y+2] != "|" or scrobj.scr[mar.x-1][mar.y+2] != "|"):
                scrobj.setscene()
                mar.movemario(scrobj,"d",-1)
                pipeobj.updatelist(scrobj,mar.moves)
                wallobj.updatelist(scrobj)
                score = enemyobj.moveenemy(scrobj,score,level,mar.y,mar.moves,-1)
                score = gemobj.updatelist(scrobj,score,1)
                flagobj.updatelist(scrobj,score,level,mar)
            else:
                mar.movemario(scrobj,"d")

        ############ LEFT #############
        elif ch == "a":
            if mar.y<33 or scrobj.scr[mar.x][mar.y-2] == "|" or scrobj.scr[mar.x-1][mar.y-2] == "|" or scrobj.scr[mar.x+1][mar.y-2] == "|":
                mar.movemario(scrobj,"a",1)
            else:
                mar.movemario(scrobj,"a")
            shootch = "a"

        ############ JUMP #############
        elif ch == "w":
            if mar.intheair == False:
                if scrobj.scr[mar.x+2][mar.y] == "X":
                    c = 5
                elif scrobj.scr[mar.x+2][mar.y] == "|":
                    c = 9
                os.system("aplay "+str("./modules/mb_jump.wav"))
                c = mar.jump(scrobj,c)

        ############ SHOOT #############
        elif ch == "b":
            mar.shooting(scrobj,"b")

        ############ QUIT #############
        elif ch == "q":
            os.system("aplay "+str("./modules/mb_die.wav"))
            break

    else:
        score = gemobj.updatelist(scrobj,score)

    #### GRAVITY EFFECTS ####
    if mar.top:
        mar.gravity(scrobj)
    elif mar.intheair:
        c = mar.jump(scrobj,c)

    #### ENEMY MOVEMENT ####
    score = enemyobj.moveenemy(scrobj,score,level,mar.y)
    mar.lifecheck(scrobj)
    mar.shooting(scrobj)

    #### CHECKPOINT AND NEXT LEVEL ####
    if end == 0:
        end = flagobj.checkend(scrobj)

    if end:
        restart = flagobj.lowerflag(scrobj)
        if restart:
            level = level+1
            score = score + 500
            mar.moves = 1
            flagobj.remove(scrobj)
            time.sleep(1)
            flagf=0
            c=0
            f=1
            end = 0
            restart = 0

################# GAME ENDS #################
sys.stdout.write("\033c")
print("GAME OVER!")
print("Score: " + str(score))
print("LEVEL: " +str(level))
