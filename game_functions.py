
import pygame as pg
import sys


def terminate():
    pg.quit()
    sys.exit()


def wait4action(st):
    # while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()

            direction = 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:  # Нажатие ESC осуществляет выход.
                    terminate()
                elif event.key == pg.K_KP1:
                    direction = 1
                elif event.key == pg.K_KP2 or event.key == pg.K_DOWN:
                    direction = 2
                elif event.key == pg.K_KP3:
                    direction = 3
                elif event.key == pg.K_KP4 or event.key == pg.K_LEFT:
                    direction = 4
                # elif event.key == pg.K_KP5:
                #     direction = 0
                elif event.key == pg.K_KP6 or event.key == pg.K_RIGHT:
                    direction = 6
                elif event.key == pg.K_KP7:
                    direction = 7
                elif event.key == pg.K_KP8 or event.key == pg.K_UP:
                    direction = 8
                elif event.key == pg.K_KP9:
                    direction = 9

                if direction:
                    move(st, direction)

        return


def check4move(st, selected_unit, direction):
    """ Check for possibility move for selected_unit into target cell

    :param selected_unit: (unit_id, owner_id)
    :param target:        (x, y)  map cell
    :return:              # 0 = No, 1 = Yes, 2 = Enemy, 3 = impossible ...
    """
    return 1


def move(st, direction):
    # from data.settings.settings import SettingsClass
    # st = SettingsClass()
    v = check4move(st, st.selected, direction)
    if v:
        target = st.selected
        if direction in (1, 4, 7): target = target[0]-1, target[1]
        if direction in (3, 6, 9): target = target[0]+1, target[1]
        if direction in (1, 2, 3): target = target[0],   target[1]+1
        if direction in (7, 8, 9): target = target[0],   target[1]-1

        if v == 1:
            st.game_map.game_map[3][st.selected[0], st.selected[1]] = 0
            st.game_map.game_map[3][target[0], target[1]] = 1

            st.selected = target

    else:
        return v
    ...


def select():
    ...


if __name__ == "__main__":
    from data.settings.settings import SettingsClass
    st = SettingsClass
    print('You are at game_function')