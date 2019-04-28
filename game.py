"""
Run game file
"""

import pygame as pg
import game_functions, random
from data.settings.settings import SettingsClass
from data.game_map.mapClass import GameMap


pg.init()
st = SettingsClass()
# st.game_map = GameMap(st)
# game_map = GameMap(st)
main_clock = pg.time.Clock()
window = pg.display.set_mode(st.WINDOWSIZE)
pg.display.set_caption("Colonization")


window.fill((0, 0, 0))


# game_functions.wait4keypress()
while True:

    for x in range(st.game_map.settings.SHAPE[0]):
        for y in range(st.game_map.settings.SHAPE[1]):
            # game_map terrain-layer
            t = pg.Rect(32*x, 32*y, 32, 32)
            window.blit(st.game_map.settings.TERRAIN_IMAGE[st.game_map.game_map[0][x, y]], t)
            # game_map unit-layer
            t = pg.Rect(32 * x, 32 * y, 32, 32)
            v = st.game_map.game_map[3][x, y]
            if v:
                image = pg.transform.scale(st.units.unit_images[v], (16, 32))
                window.blit(image, t)

            # MOVEMENT
            SELECTED = (4, 4)

    #
    #
    pg.display.update()
    game_functions.wait4action(st)
    main_clock.tick(st.FPS)

