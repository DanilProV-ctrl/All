import pygame as pg

WIN_WIDTH,WIN_HEIGHT = 780,320

pg.init()

pg.display.set_caption('Window')

screen = pg.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

run = True
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
            run = False