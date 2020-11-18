
import pygame as p
from chess import chess_Engine

WIDTH = HEIGHT = 800
DIMENSION = 12
SQUARE_size = HEIGHT//DIMENSION
MAX_FPS = 15
IMAGES = {}

"""
création d'un dictionnaire contenant toute les images du jeux
"""


def load_images():
    pieces = ["ar", "ca", "dr", "kn", "ma", "or"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("chess/images/" + piece + ".png"), (SQUARE_size, SQUARE_size))


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("black"))
    game_status = chess_Engine.GameState()
    load_images()
    running = True
    while running:
        for i in p.event.get():
            if i.type == p.QUIT:
                running = False
        draw_game_status(screen, game_status)
        clock.tick(MAX_FPS)
        p.display.flip()


def draw_game_status(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)


def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for i in range(DIMENSION):
        for x in range(DIMENSION):
            color = colors[((i+x) % 2)]
            p.draw.rect(screen, color, p.Rect(i*SQUARE_size, x*SQUARE_size, SQUARE_size, SQUARE_size))


def draw_pieces(screen, board):
    for i in range(DIMENSION):
        for x in range(DIMENSION):
            piece = board[x][i]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(i*SQUARE_size, x*SQUARE_size, SQUARE_size, SQUARE_size))


if __name__ == "__main__":

    main()
