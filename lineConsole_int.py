from board import Board
from Army_class import *
from human import *
from Orcs_class import *

a = Army()
h = Humans()
o = Orcs()
B = Board()


def drawboard():
    for i in range(12):
        for x in range(12):
            print(B.get_board()[i][x], end='  ')
        print()

def lineConsoleGame():

    q = ''

    print('règlement')

    print('l\'équipe des humains commence à déposer ses pièces')

    for v in range(1, a.get_nbrhuman):
        for x in range(1, h.get_nbrknights()):
            placement = input(
                'ou voulez vous placer vos placer vos chevaliers ? ( {} restant(s))'.format(h.get_nbrknights() - x))
            B.get_board()[B.get_hor().index(placement[0])][B.get_vert().index(placement[1:])] = \
                h.get_notaHuman(0)
            drawboard()

        for y in range(1, h.get_nbrarch()):
            placement = input(
                'ou voulez vous placer vos placer vos archers ? ( {} restant(s))'.format(h.get_nbrarch() - y))
            B.get_board()[B.get_hor().index(placement[0])][
                B.get_vert().index(placement[1:])] = h.get_notaHuman(1)
            drawboard()

        for z in range(1, h.get_nbrcata()):
            placement = input(
                'ou voulez vous placer vos placer vos catapultes ? ( {} restant(s))'.format(h.get_nbrcata() - z))
            B.get_board()[B.get_hor().index(placement[0])][B.get_vert().index(placement[1:])] = h.get_notaHuman(2)
            drawboard()

    print('c\'est maintenant à l\'équipe des orcs de déposer ses pièces sur le champ de bataille')

    for v in range(1, h.get_nbrcata()):
        for x in range(1, h.get_nbrcata()):
            placement = input('ou voulez vous placer vos placer vos orcs ? ( {} restant(s))'.format(o.get_nbrorcs() - x))
            B.get_board()[B.get_hor().index(placement[0])][B.get_vert().index(placement[1:])] = o.get_notaOrcs(0)
            drawboard()

        for y in range(1, h.get_nbrcata()):
            placement = input(
                'ou voulez vous placer vos placer vos mages ? ( {} restant(s))'.format(o.get_nbr_mages() - y))
            B.get_board()[B.get_hor().index(placement[0])][B.get_vert().index(placement[1:])] = o.get_notaOrcs(1)
            drawboard()

        for z in range(1, h.get_nbrcata()):
            placement = input(
                'ou voulez vous placer vos placer vos dragons ? ( {} restant(s))'.format(o.get_nbrdrakes() - z))
            B.get_board()[B.get_hor().index(placement[0])][B.get_vert().index(placement[1:])] = o.get_notaOrcs(2)
            drawboard()

    print(
        'maintenant que toute les pièces que chaqu\'une des équipes sont placées le combat peut enfin commencé')

    while q != 'quit':

        if B.tour_des_humains:
            print('c\'est au tour des humain de jouer !')
            B.tour_des_humains = False
        else:
            print('c\'est au tour des orcs de jouer !')
            B.tour_des_humains = True

        drawboard()

        pos = input('inserez les coordonnées d\'une case contenant l\'une de vos pièces')

        while pos != 'ff' and B.get_board()[B.get_hor().index(pos[0])][B.get_vert().index(pos[1:])] == '--':
            position = input('inserez les coordonnées correctes d\'une case contenant l\'une de vos pièce')

        if pos == 'ff':
            if B.tour_des_humains:
                print('les humains ont gagné car les orcs ont déclaré forfait')
                break
            else:
                print('les orcs ont gagné car les humains ont déclaré forfait')
                break
        else:
            deplacement = input('ou voullez vous déplacer la pièce choisis ?')

            B.get_board()[B.get_hor().index(deplacement[0])][B.get_vert().index(deplacement[1:])] = \
                B.get_board()[B.get_hor().index(pos[0])][B.get_vert().index(pos[1:])]

            B.get_board()[B.get_hor().index(pos[0])][B.get_vert().index(pos[1:])] = '--'

        for x in range(len(B.get_board())):
            if len(set(B.get_board()[x])) > 1:
                break
            else:
                q = 'quit'

    print('partie terminé')
