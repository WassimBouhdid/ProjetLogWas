import pygame as p

import unittest
from moves import Moves
import board
from board import *

B = Board()

class GUI:
    def __init__(self, dimension=12, width=720, height=720):

        self.__dim = dimension
        self.__width = width
        self.__height = height
        self.__dimcar = int(self.__width // self.__dim)
        self.__maxfps = 15

    def chargimg(self):
        images = ["ar", "ca", "dr", "kn", "ma", "or", "og"]
        Loadedimg = {}
        for image in images:
            Loadedimg[image] = p.transform.scale(p.image.load("images/" + image + ".png"),
                                                 (self.__dimcar, self.__dimcar))
        return Loadedimg

    def dessplat(self, screen):
        colors = [p.Color("white"), p.Color("gray")]
        for i in range(self.__dim):
            for x in range(self.__dim):
                color = colors[((i + x) % 2)]
                p.draw.rect(screen, color, p.Rect(i * self.__dimcar, x * self.__dimcar, self.__dimcar, self.__dimcar))

    def desspieces(self, screen, board, img):
        for i in range(self.__dim):
            for x in range(self.__dim):
                piece = board[x][i]
                if piece != "--":
                    screen.blit(img[piece],
                                p.Rect(i * self.__dimcar, x * self.__dimcar, self.__dimcar, self.__dimcar))

    def desstatut(self, interface, screen, stat, img):
        interface.dessplat(screen)
        interface.desspieces(screen, stat, img)

    def lancement(self, status):
        p.init()
        clock = p.time.Clock()
        interface = GUI()
        window = p.display.set_mode((720, 720))
        running = True
        sqselected = ()
        playerClicks = []
        while running:
            for event in p.event.get():
                if event.type == p.QUIT:
                    running = False
                if event.type == p.MOUSEBUTTONDOWN:
                    selection = p.mouse.get_pos()
                    row = selection[0] // self.__dimcar
                    col = selection[1] // self.__dimcar
                    if sqselected == (row, col):
                        sqselected = ()
                        playerClicks = []
                    else:
                        sqselected = (row, col)
                        playerClicks.append(sqselected)
                    if len(playerClicks) == 2:
                        move = Moves(playerClicks[0], playerClicks[1], status)
                        B.makemove(move, status)
                        print(move.getpositionnotation())
                        sqselected = ()
                        playerClicks = []
            interface.desstatut(interface, window, status, interface.chargimg())
            clock.tick(self.__maxfps)
            p.display.flip()
