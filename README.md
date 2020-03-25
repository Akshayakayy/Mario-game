# Python Terminal Mario

## Introduction
This game has been written using Python. Important to note that the game has been tested on **ONLY** Linux-based OSs.

## Structure
This application demonstrates inheritance, encapsulation, abstraction as well as polymorphism.
    - Each "object" is a derived class of the `Object` class.
    - The `board` has its own class and and captures all objects placed on it.

## Running the program
    - Running the program is easy
            - `python3 ./mario.py`

## Controls
    - Controls follow traditional classic titles (w,a,d)
    - To shoot a bullet press `b`
    - To quit, press `q`
    - To kill small enemies, you can either jump on it or shoot it
    - To kill boss enemies, you have to shoot it

## Features

### Movements
    - Mario can move left, right, jump and shoot
    - Mario jumps and lands back to the ground as gravity effect
    - He jumps higher on pipes than on grass/ground

### Obstacles
    - Enemies move left and right automatically
    - Boss enemies are smart, and can chase the player
    - Boss enemies have extra lives
    - The enemies and boss gain lives as the level increases
    - Mario can't pass through pipes and bridges, can only jump over them. If Mario hits a bridge while jumping, he falls back down.

### Score
    - Score increases for the duration of the game
    - Bonus score for coins collected
    - Score increases for killing the small enemies and boss. More for the boss.
    - Score, lives and level is displayed on screen

### Background and Scenery
    - Scenery is changed while Mario moves
    - Bridges, clouds, pipes, flags and other objects move as Mario movesforward
    - The scenery is colored
    - Everytime Mario starts, dies, gets coins, jumps or gets hit by the enemy, sound is created

### Levels
    - When Mario reaches the flag post, the flag is lowered and Mario advances to the next level where the enemies are tougher, the game duration is longer and coins are lesser.
    - When Mario loses or quits, the end score and level are displayed on the terminal
