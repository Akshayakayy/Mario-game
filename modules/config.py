import sys

colors = {
    'Black'            : '\x1b[0;30m',
    'Blue'             : '\x1b[0;34m',
    'Green'            : '\x1b[0;32m',
    'Cyan'             : '\x1b[0;36m',
    'Red'              : '\x1b[0;31m',
    'Purple'           : '\x1b[0;35m',
    'Brown'            : '\x1b[0;33m',
    'Gray'             : '\x1b[0;37m',
    'Dark Gray'        : '\x1b[1;30m',
    'Light Blue'       : '\x1b[1;34m',
    'Light Green'      : '\x1b[1;32m',
    'Light Cyan'       : '\x1b[1;36m',
    'Light Red'        : '\x1b[1;31m',
    'Light Purple'     : '\x1b[1;35m',
    'Yellow'           : '\x1b[1;33m',
    'White'            : '\x1b[1;37m'
}

def printcc(st):
    if st == "X":
        print(colors['Light Green'] + st, end='')
    elif st == "(" or st == ")" or st == "_":
        print(colors['Light Blue'] + st, end='')
    elif st == "M":
        print(colors['Light Red'] + st, end='')
    elif st == "{" or st == "}":
        print(colors['Purple'] + st, end='')
    elif st == "<" or st == ">":
        print(colors['Light Purple'] + st, end='')
    elif st == "*":
        print(colors['Yellow'] + st, end='')
    elif st == "#":
        print(colors['White'] + st, end='')
    elif st == "@":
        print(colors['Red'] + st, end='')
    elif st == "|":
        print(colors['Brown'] + st, end='')
    elif st == "!" or st == "^":
        print(colors['Gray'] + st, end='')
    elif st == "$":
        print(colors['Yellow'] + st, end='')
    elif st == "\\" or st == "/":
        print(colors['Light Cyan'] + st, end='')
    elif st == "=":
        print(colors['Light Red'] + st, end='')
    elif st == "I":
        print(colors['Gray'] + st, end='')
    else:
        print(colors['White'] + st, end='')
