import pygame as p
import argparse
from Army_class import Army
from Humans_class import humains
from Orcs_class import Orcs
from Party_class import partie


class Board:
    def __init__(self):
        # plateau sur lequelle se trouve les pièce jouable
        # dr = dragon   ma = mage   or = orc pour le coté "noir"
        # ca = catapulte    ar = archer    kn = chevalier
        # "--" représente une case vide
        self.__plateau = [
            ["1", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["2", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["3", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["4", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["5", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["6", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["7", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["8", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["9", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["10", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["11", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["12", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ['--', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']]

        self.dim = 13
        self.larg = 611
        self.haut = 700
        self.dimcar = int(611 // self.dim)
        self.img = {}
        self.__vert = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'f']
        self.__hor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
        self.maxfps = 15
        self.running = ''
        self.fen = p.display.set_mode((self.larg, self.haut))


    def get_board(self):
        return self.__plateau

    def drawboard(self):
        for i in range(12):
            for x in range(12):
                print(Board.get_board()[i][x], end='  ')
            print()

    def get_hor(self):
        return self.__hor

    def get_vert(self):
        return self.__vert

    def chargimg(self):
        images = ["ar", "ca", "dr", "kn", "ma", "or", "og", '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                  '12', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

        for image in images:
            self.img[image] = p.transform.scale(p.image.load("images/" + image + ".png"), (self.dimcar, self.dimcar))

    def desstatut(self, stat):
        pl.dessplat(pl.fen)
        pl.desspieces(pl.fen, stat)

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
        pl.fen.fill((30, 30, 0))
        pl.chargimg()
        font = p.font.Font(None, 32)
        input_box = p.Rect(200, 650, 140, 32)
        color_inactive = p.Color('lightskyblue3')
        color_active = p.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        done = False
        input = ""
        pl.running = True
        while pl.running:
            for event in p.event.get():
                if event.type == p.QUIT:
                    pl.running = False
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
                pl.desstatut(status)
                p.display.flip()


if __name__ == "__main__":
    a = Army()
    h = humains()
    o = Orcs()
    p.init()

    parser = argparse.ArgumentParser()
    parser.add_argument("-cl", "--commandlign", action="lance le jeu en ligne de commande")
    parser.add_argument("-i", "--interface", action="lance l'interface de jeu")
    args = parser.parse_args()
    if args.commandlign:
        def main():
            q = ''

            print('règlement')

            print('l\'équipe des humains commence à déposer ses pièces')

            for v in range(1, a.get_nbrhuman):
                for x in range(1, h.get_nbrknights):
                    placement = input(
                        'ou voulez vous placer vos placer vos chevaliers ? ( {} restant(s))'.format(h.get_nbrknights-x))
                    Board.get_Board()[Board.get_hor().index(placement[0])][Board.get_vert().index(placement[1:])] = \
                        h.get_nota()[0]

                    h.kill_arch()
                    Board.drawboard()

                for y in range(1, h.get_nbrarch):
                    placement = input(
                        'ou voulez vous placer vos placer vos archers ? ( {} restant(s))'.format(h.get_nbrarch-y))
                    Board.get_Board()[Board.hor.index(placement[0])][
                        Board.ver.index(placement[1:])] = Board.achersnotation
                    Board.drawboard()

                for z in range(1, h.get_nbrcata):
                    placement = input(
                        'ou voulez vous placer vos placer vos catapultes ? ( {} restant(s))'.format(gs.nbrcata-z))
                    gs.board[gs.hor.index(placement[0])][gs.ver.index(placement[1:])] = gs.catanotation
                    Board.drawboard()

            print('c\'est maintenant à l\'équipe des orcs de déposer ses pièces sur le champ de bataille')

            for v in range(1, h.get_nbrcata):
                for x in range(1, h.get_nbrcata):
                    placement = input('ou voulez vous placer vos placer vos orcs ? ( {} restant(s))'.format(gs.nbrorcs-x))
                    gs.board[gs.hor.index(placement[0])][gs.ver.index(placement[1:])] = gs.orcsnotation
                    Board.drawboard()

                for y in range(1, h.get_nbrcata):
                    placement = input(
                        'ou voulez vous placer vos placer vos mages ? ( {} restant(s))'.format(gs.nbrmages-y))
                    gs.board[gs.hor.index(placement[0])][gs.ver.index(placement[1:])] = gs.magesnotation
                    Board.drawboard()

                for z in range(1, h.get_nbrcata):
                    placement = input(
                        'ou voulez vous placer vos placer vos dragons ? ( {} restant(s))'.format(gs.nbrdrakes-z))
                    gs.board[gs.hor.index(placement[0])][gs.ver.index(placement[1:])] = gs.drakesnotation
                    Board.drawboard()

            print(
                'maintenant que toute les pièces que chaqu\'une des équipes sont placées le combat peut enfin commencé')

            while q != 'quit':

                if gs.tour_des_humains:
                    print('c\'est au tour des humain de jouer !')
                    gs.tour_des_humains = False
                else:
                    print('c\'est au tour des orcs de jouer !')
                    gs.tour_des_humains = True

                gs.drawboard()

                pos = input('inserez les coordonnées d\'une case contenant l\'une de vos pièces')

                while pos != 'ff' and gs.board[gs.hor.index(pos[0])][gs.ver.index(pos[1:])] == '--':
                    position = input('inserez les coordonnées correctes d\'une case contenant l\'une de vos pièce')

                if pos == 'ff':
                    if gs.tour_des_humains:
                        print('les humains ont gagné car les orcs ont déclaré forfait')
                        break
                    else:
                        print('les orcs ont gagné car les humains ont déclaré forfait')
                        break
                else:
                    deplacement = input('ou voullez vous déplacer la pièce choisis ?')

                    gs.board[gs.hor.index(deplacement[0])][gs.ver.index(deplacement[1:])] = \
                        gs.board[gs.hor.index(pos[0])][
                            gs.ver.index(pos[1:])]

                    gs.board[gs.hor.index(pos[0])][gs.ver.index(pos[1:])] = '--'

                for x in range(len(gs.board)):
                    if len(set(gs.board[x])) > 1:
                        break
                    else:
                        q = 'quit'

            print('partie terminé')
    elif (args.interface):
        B = Board()
        B.lancement(B.get_Board())
