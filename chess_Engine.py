import argparse
from lineConsole_int import lineConsoleGame
from chess_GUI import *

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-cl", "--commandlign", action="store_true")
    parser.add_argument("-i", "--interface", action="store_true")
    args = parser.parse_args()

    if args.commandlign:
        lineConsoleGame()
    else:
        GUI.lancement()


