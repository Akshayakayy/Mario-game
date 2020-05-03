"""This module contains colors functions."""

COLORS = {
    'Black': '\x1b[0;30m',
    'Blue': '\x1b[0;34m',
    'Green': '\x1b[0;32m',
    'Cyan': '\x1b[0;36m',
    'Red': '\x1b[0;31m',
    'Purple': '\x1b[0;35m',
    'Brown': '\x1b[0;33m',
    'Gray': '\x1b[0;37m',
    'Dark Gray': '\x1b[1;30m',
    'Light Blue': '\x1b[1;34m',
    'Light Green': '\x1b[1;32m',
    'Light Cyan': '\x1b[1;36m',
    'Light Red': '\x1b[1;31m',
    'Light Purple': '\x1b[1;35m',
    'Yellow': '\x1b[1;33m',
    'White': '\x1b[1;37m'
}


def printcc(stvar):
    """This function returns colors."""
    if stvar == "X":
        print(COLORS['Light Green'] + stvar, end='')
    elif stvar in ('(', ')', '_'):
        print(COLORS['Light Blue'] + stvar, end='')
    elif stvar == "M":
        print(COLORS['Light Red'] + stvar, end='')
    elif stvar in ('{', '}'):
        print(COLORS['Purple'] + stvar, end='')
    elif stvar in ('<', '>'):
        print(COLORS['Light Purple'] + stvar, end='')
    elif stvar == "*":
        print(COLORS['Yellow'] + stvar, end='')
    elif stvar == "#":
        print(COLORS['White'] + stvar, end='')
    elif stvar == "@":
        print(COLORS['Red'] + stvar, end='')
    elif stvar == "|":
        print(COLORS['Brown'] + stvar, end='')
    elif stvar in ('!', '^'):
        print(COLORS['Gray'] + stvar, end='')
    elif stvar == "$":
        print(COLORS['Yellow'] + stvar, end='')
    elif stvar in ('\\\\', '/'):
        print(COLORS['Light Cyan'] + stvar, end='')
    elif stvar == "=":
        print(COLORS['Light Red'] + stvar, end='')
    elif stvar == "I":
        print(COLORS['Gray'] + stvar, end='')
    else:
        print(COLORS['White'] + stvar, end='')
