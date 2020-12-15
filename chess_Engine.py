import pygame as p


class Plateau:
    def __init__(self):
        # plateau sur lequelle se trouve les pièce jouable
        # dr = dragon   ma = mage   or = orc pour le coté "noir"
        # ca = catapulte    ar = archer    kn = chevalier
        # "--" représente une case vide
        self.plateau = [
            ["1", "--", "--", "--", "--", "kn", "ma", "or", "ca", "--", "--", "--", "--"],
            ["2", "--", "--", "--", "--", "--", "dr", "ar", "og", "--", "--", "--", "--"],
            ["3", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["4", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["5", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["6", "--", "--", "--", "--", "og", "--", "--", "--", "--", "--", "--", "--"],
            ["7", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["8", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["9", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["10", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["11", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["12", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ['--', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']]

        self.dim = 13
        self.larg = 800
        self.haut = 800
        self.dimcar = int(self.haut / self.dim)
        self.img = {}
        self.ligneVert = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'f']
        self.ligneHor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
        self.fen = p.display.set_mode((self.haut, self.larg))
        self.maxfps = 15

    def chargimg(self):
        images = ["ar", "ca", "dr", "kn", "ma", "or", "og", '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                  '12', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

        for image in images:
            self.img[image] = p.transform.scale(p.image.load("images/" + image + ".png"), (self.dimcar, self.dimcar))

    def lancement(self, status):
        p.init()
        clock = p.time.Clock()
        pl.chargimg()
        running = True
        while running:
            for i in p.event.get():
                if i.type == p.QUIT:
                    running = False
            pl.desstatut(self.fen, status)
            clock.tick(pl.maxfps)
            p.display.flip()

    def desstatut(self, screen, stat):
        pl.dessplat(screen)
        pl.desspieces(screen, stat)

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


pl = Plateau()

if __name__ == "__main__":
    pl.lancement(pl.plateau)
