"""
Map would be a matrix (size def in settings) with N depth
0-layer:        terrain type (v) 0 = None, 1 = ocean, 2 = Sea, 3 = Plain, 4 = Grass ...
1-layer:        forest       (v) 0 = None, 1 = Plowed, 2 Forest, 3 Hill ...
2-layer:        bonus        (v) 0 = None, 1 = Tobacco, 2 Fur, 3 Silver ...
3-layer:        unit         (v) 0 = None, 1 = Criminal, 2 Servant, 3 Colonist ...
4-layer:        unit_owner   (v) 0 = None, 1 = Player1, 2 = Player2, 7 Incas ...
# road + river
"""

import numpy as np


class GameMap:
    """"""
    import random

    def __init__(self):
        self.settings = MapSettings()

        # self.depth = self.settings.TOTAL_LAYERS
        # self.shape = self.settings.SHAPE
        #################################
        self.game_map = self.create_map()

    def create_map(self):
        """"""
        size = self.settings.DEPTH, *self.settings.SHAPE
        game_map = np.zeros(size, dtype=np.int8)

        # DEBUG
        for x in range(self.settings.SHAPE[0]):
            for y in range(self.settings.SHAPE[1]):
                game_map[0][x, y] = GameMap.random.randint(0, 3)
                if GameMap.random.randint(0, 20) < 1:
                    game_map[3][x][y] = GameMap.random.randint(1, 4)
            # print()
        # DEBUG
        game_map[3][4, 4] = 1
        return game_map


class MapSettings:
    TOTAL_LAYERS = 4
    SHAPE = (30, 30)
    DEPTH = 4
    TERRAIN_NAME = {
        0: "undefined",
        1: "sea",
        2: "ocean",
        3: "plain",
        4: "grassland",
        5: "prairie",
        6: "savannah",
        7: "marsh",
        8: "swamp",
        9: "dessert",
        10: "tundra",
        11: "arctic",
        # 12: "hill",
        # 13: "mountain",
    }
    IMAGE_PATH = {
        0: r"data\images\terrain\0.png ",
        1: r"data\images\terrain\1.png ",
        2: r"data\images\terrain\2.png ",
        3: r"data\images\terrain\3.png ",
        4: r"data\images\terrain\4.png ",
        # 1: r"data\images\groundunits\indianConvert.png",
        # 2: r"data\images\groundunits\pettyCriminal.png",
        # 3: r"data\images\groundunits\indenturedServant.png",
        # 4: r"data\images\groundunits\freeColonist.png",
        # 5: r"data\images\groundunits\undefined.png",
        # 6: r"data\images\groundunits\undefined.png",
        # 7: r"data\images\groundunits\undefined.png",
        # 8: r"data\images\groundunits\undefined.png",
        # 9: r"data\images\groundunits\undefined.png",
        # 10: r"data\images\groundunits\undefined.png",
        # 11: r"data\images\groundunits\undefined.png",
        # 12: r"data\images\groundunits\undefined.png",
        # 13: r"data\images\groundunits\undefined.png",
        # 14: r"data\images\groundunits\undefined.png",
        # 15: r"data\images\groundunits\undefined.png",
        # 16: r"data\images\groundunits\undefined.png",
        # 17: r"data\images\groundunits\undefined.png",
        # 18: r"data\images\groundunits\undefined.png",
        # 19: r"data\images\groundunits\undefined.png",
        # 20: r"data\images\groundunits\undefined.png",
        # 21: r"data\images\groundunits\undefined.png",
        # 22: r"data\images\groundunits\undefined.png",
        # 23: r"data\images\groundunits\undefined.png",
        # 24: r"data\images\groundunits\undefined.png",
        # 25: r"data\images\groundunits\undefined.png",
        # 26: r"data\images\groundunits\undefined.png",
        # 27: r"data\images\groundunits\undefined.png",
        # 28: r"data\images\groundunits\undefined.png",
        #
        # 5: "Expert Farmer",
        # 6: "Expert Fisherman",
        # 7: "Expert Fur Trapper",
        # 8: "Expert Lumberjack",
        # 9: "Expert Ore Miner",
        # 10: "Expert Silver Miner",
        # 11: "Master Sugar Planter",
        # 12: "Master Tobacco Planter",
        # 13: "Master Fur Trader",
        # 14: "Master Cotton Planter",
        # 15: "Master Distiller",
        # 16: "Master Tobacconist",
        # 17: "Master Weaver",
        # 18: "Master Blacksmith",
        # 19: "Master Carpenter",
        # 20: "Master Gunsmith",
        # 21: "Seasoned Scout",
        # 22: "Hardy Pioneer",
        # 23: "Firebrand Preacher",
        # 24: "Elder Statesman",
        # 25: "Jesuit Missionary",
        # 26: "Veteran Solder"
    }
    TERRAIN_IMAGE = dict()

    import pygame as pg
    TERRAIN_IMAGE[0] = pg.image.load(IMAGE_PATH[0])
    TERRAIN_IMAGE[1] = pg.image.load(IMAGE_PATH[1])
    TERRAIN_IMAGE[2] = pg.image.load(IMAGE_PATH[2])
    TERRAIN_IMAGE[3] = pg.image.load(IMAGE_PATH[3])
    TERRAIN_IMAGE[4] = pg.image.load(IMAGE_PATH[4])
    ...


if __name__ == '__main__':
    from data.settings.settings import SettingsClass
    import pygame as pg
    st = SettingsClass()
    map = GameMap()
    print(map.game_map)


