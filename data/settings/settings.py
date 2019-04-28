import pygame as pg
from data.game_map.mapClass import GameMap


class SettingsClass:

    def __init__(self):

        """ UNIT TYPES """

        self.WINDOWSIZE = 800, 600
        self.FPS = 60
        self.BGCOLOR = (0, 0, 0)
        # self.font = pg.font.SysFont(None, 35)

        self.units = UnitSettings()
        self.game_map = GameMap()

        # SELECTED by cursor cell address in game_map.game_map
        self.selected = (4, 4)

        """MAP SETTINGS"""
        self.map_shape = (30, 30)


#
#
# class MapSettings:
#     shape = (30, 30)
#     terrain_name = {
#         0: "undefined",
#         1: "sea",
#         2: "ocean",
#         3: "plain",
#         4: "grassland",
#         5: "prairie",
#         6: "savannah",
#         7: "marsh",
#         8: "swamp",
#         9: "dessert",
#         10: "tundra",
#         11: "arctic",
#         # 12: "hill",
#         # 13: "mountain",
#     }
#     image_path = {
#         0: r"data\images\terrain\0.png ",
#         1: r"data\images\terrain\1.png ",
#         2: r"data\images\terrain\2.png ",
#         3: r"data\images\terrain\3.png ",
#         4: r"data\images\terrain\4.png ",
#         # 1: r"data\images\groundunits\indianConvert.png",
#         # 2: r"data\images\groundunits\pettyCriminal.png",
#         # 3: r"data\images\groundunits\indenturedServant.png",
#         # 4: r"data\images\groundunits\freeColonist.png",
#         # 5: r"data\images\groundunits\undefined.png",
#         # 6: r"data\images\groundunits\undefined.png",
#         # 7: r"data\images\groundunits\undefined.png",
#         # 8: r"data\images\groundunits\undefined.png",
#         # 9: r"data\images\groundunits\undefined.png",
#         # 10: r"data\images\groundunits\undefined.png",
#         # 11: r"data\images\groundunits\undefined.png",
#         # 12: r"data\images\groundunits\undefined.png",
#         # 13: r"data\images\groundunits\undefined.png",
#         # 14: r"data\images\groundunits\undefined.png",
#         # 15: r"data\images\groundunits\undefined.png",
#         # 16: r"data\images\groundunits\undefined.png",
#         # 17: r"data\images\groundunits\undefined.png",
#         # 18: r"data\images\groundunits\undefined.png",
#         # 19: r"data\images\groundunits\undefined.png",
#         # 20: r"data\images\groundunits\undefined.png",
#         # 21: r"data\images\groundunits\undefined.png",
#         # 22: r"data\images\groundunits\undefined.png",
#         # 23: r"data\images\groundunits\undefined.png",
#         # 24: r"data\images\groundunits\undefined.png",
#         # 25: r"data\images\groundunits\undefined.png",
#         # 26: r"data\images\groundunits\undefined.png",
#         # 27: r"data\images\groundunits\undefined.png",
#         # 28: r"data\images\groundunits\undefined.png",
#         #
#         # 5: "Expert Farmer",
#         # 6: "Expert Fisherman",
#         # 7: "Expert Fur Trapper",
#         # 8: "Expert Lumberjack",
#         # 9: "Expert Ore Miner",
#         # 10: "Expert Silver Miner",
#         # 11: "Master Sugar Planter",
#         # 12: "Master Tobacco Planter",
#         # 13: "Master Fur Trader",
#         # 14: "Master Cotton Planter",
#         # 15: "Master Distiller",
#         # 16: "Master Tobacconist",
#         # 17: "Master Weaver",
#         # 18: "Master Blacksmith",
#         # 19: "Master Carpenter",
#         # 20: "Master Gunsmith",
#         # 21: "Seasoned Scout",
#         # 22: "Hardy Pioneer",
#         # 23: "Firebrand Preacher",
#         # 24: "Elder Statesman",
#         # 25: "Jesuit Missionary",
#         # 26: "Veteran Solder"
#     }
#     terrain_image = dict()
#     terrain_image[0] = pg.image.load(image_path[0])
#     terrain_image[1] = pg.image.load(image_path[1])
#     terrain_image[2] = pg.image.load(image_path[2])
#     terrain_image[3] = pg.image.load(image_path[3])
#     terrain_image[4] = pg.image.load(image_path[4])
#     ...


class UnitSettings:

    def __init__(self):
        self.groundunit_names = {
            0: "undefined",
            1: "Indian Converts",
            2: "Petty Criminals",
            3: "Indentured Servants",
            4: "Free Colonist",
            5: "Expert Farmer",
            6: "Expert Fisherman",
            7: "Expert Fur Trapper",
            8: "Expert Lumberjack",
            9: "Expert Ore Miner",
            10: "Expert Silver Miner",
            11: "Master Sugar Planter",
            12: "Master Tobacco Planter",
            13: "Master Fur Trader",
            14: "Master Cotton Planter",
            15: "Master Distiller",
            16: "Master Tobacconist",
            17: "Master Weaver",
            18: "Master Blacksmith",
            19: "Master Carpenter",
            20: "Master Gunsmith",
            21: "Seasoned Scout",
            22: "Hardy Pioneer",
            23: "Firebrand Preacher",
            24: "Elder Statesman",
            25: "Jesuit Missionary",
            26: "Veteran Solder"
        }
        self.image_path = {
            0: r"data\images\groundunits\undefined.png",
            1: r"data\images\groundunits\indianConvert.png",
            2: r"data\images\groundunits\pettyCriminal.png",
            3: r"data\images\groundunits\indenturedServant.png",
            4: r"data\images\groundunits\freeColonist.png",
            5: r"data\images\groundunits\undefined.png",
            6: r"data\images\groundunits\undefined.png",
            7: r"data\images\groundunits\undefined.png",
            8: r"data\images\groundunits\undefined.png",
            9: r"data\images\groundunits\undefined.png",
            10: r"data\images\groundunits\undefined.png",
            11: r"data\images\groundunits\undefined.png",
            12: r"data\images\groundunits\undefined.png",
            13: r"data\images\groundunits\undefined.png",
            14: r"data\images\groundunits\undefined.png",
            15: r"data\images\groundunits\undefined.png",
            16: r"data\images\groundunits\undefined.png",
            17: r"data\images\groundunits\undefined.png",
            18: r"data\images\groundunits\undefined.png",
            19: r"data\images\groundunits\undefined.png",
            20: r"data\images\groundunits\undefined.png",
            21: r"data\images\groundunits\undefined.png",
            22: r"data\images\groundunits\undefined.png",
            23: r"data\images\groundunits\undefined.png",
            24: r"data\images\groundunits\undefined.png",
            25: r"data\images\groundunits\undefined.png",
            26: r"data\images\groundunits\undefined.png",
            27: r"data\images\groundunits\undefined.png",
            28: r"data\images\groundunits\undefined.png",
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
        self.unit_images = {}
        self.load_images()

    def load_images(self):
        for key in self.image_path.keys():
            self.unit_images[key] = pg.image.load(
                self.image_path[key]
            )
    ...

