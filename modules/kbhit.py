"""This module contains the working of keys pressed."""
import os

# Posix (Linux, OS X)

import sys
import termios
import atexit
from select import select


class KBHit(object):
    """This class has all the functions related to keys pressed."""
    def __init__(self):
        '''Creates a KBHit object that you can call to do various keyboard things.
        '''

        # Save the terminal settings
        self.file_d = sys.stdin.fileno()
        self.new_term = termios.tcgetattr(self.file_d)
        self.old_term = termios.tcgetattr(self.file_d)

        # New terminal setting unbuffered
        self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
        termios.tcsetattr(self.file_d, termios.TCSAFLUSH, self.new_term)

        # Support normal-terminal reset at exit
        atexit.register(self.set_normal_term)

    def set_normal_term(self):
        ''' Resets to normal terminal.  On Windows this is a no-op.
        '''

        if os.name == 'nt':
            pass

        else:
            termios.tcsetattr(self.file_d, termios.TCSAFLUSH, self.old_term)


def getch():
    ''' Returns a keyboard character after kbhit() has been called.
        Should not be called in the same program as getarrow().
    '''
    return sys.stdin.read(1)


def getarrow():
    ''' Returns an arrow-key code after kbhit() has been called. Codes are
    0 : up
    1 : right
    2 : down
    3 : left
    Should not be called in the same program as getch().
    '''

    cvar = sys.stdin.read(3)[2]
    vals = [65, 67, 66, 68]

    return vals.index(ord(cvar.decode('utf-8')))


def kbhit():
    ''' Returns True if keyboard character was hit, False otherwise.
    '''
    drvar, dwvar, devar = select([sys.stdin], [], [], 0)
    _ = str(dwvar) + str(devar)  # Debug
    return drvar != []
