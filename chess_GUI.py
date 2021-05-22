import pygame as p
from board import *

B = Board()


class GUI:
    def __init__(self):

        self.dim = 13
        self.larg = 611
        self.haut = 700
        self.dimcar = int(611 // self.dim)
        self.img = {}
        self.maxfps = 15
        self.running = ''
        self.fen = p.display.set_mode((self.larg, self.haut))

    def chargimg(self):
        images = ["ar", "ca", "dr", "kn", "ma", "or", "og", '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                  '12', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

        for image in images:
            self.img[image] = p.transform.scale(p.image.load("images/" + image + ".png"), (self.dimcar, self.dimcar))

    def desstatut(self, stat):
        Board.dessplat(Board.fen)
        Board.desspieces(Board.fen, stat)

    def dessplat(self, screen):
        colors = [p.Color("white"), p.Color("gray")]
        for i in range(self.dim):
            for x in range(self.dim):
                color = colors[((i + x) % 2)]
                p.draw.rect(screen, color, p.Rect(i * self.dimcar, x * self.dimcar, self.dimcar, self.dimcar))

    def desspieces(self, screen, board):
        for i in range(self.dim):
            for x in range(self.dim):
                piece = board[x][i]
                if piece != "--":
                    screen.blit(self.img[piece], p.Rect(i * self.dimcar, x * self.dimcar, self.dimcar, self.dimcar))

    def lancement(self, status):
        Board.fen.fill((30, 30, 0))
        Board.chargimg()
        font = p.font.Font(None, 32)
        input_box = p.Rect(200, 650, 140, 32)
        color_inactive = p.Color('lightskyblue3')
        color_active = p.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        done = False
        input = ""
        Board.running = True
        while Board.running:
            for event in p.event.get():
                if event.type == p.QUIT:
                    Board.running = False
                if event.type == p.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == p.KEYDOWN:
                    if active:
                        if event.key == p.K_RETURN:
                            text = ""
                        elif event.key == p.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                Board.desstatut(status)
                p.display.flip()
