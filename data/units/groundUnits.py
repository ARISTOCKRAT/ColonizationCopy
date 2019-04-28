"""

"""


from data.units import unitsClass


class Colonist(unitsClass.Unit):

    def __init__(self, owner):
        unitsClass.Unit.__init__(self)

        self.type = "Colonist"
        self.owner = owner

        # self.move = 1
        # self.power = 0

        self.image = None

        ...


class GroundUnit(unitsClass.Unit):

    def __init__(self, unit_type, owner, st):

        unitsClass.Unit.__init__(self)

        self.unit_type = unit_type
        self.name = st.groundunit_names[unit_type]
        self.owner = owner

        # self.move = 1
        # self.power = 0

        self.image = None

        ...


def prepare(unit):

    ...


if __name__ == '__main__':
    from data.settings.settings import SettingsClass
    st = SettingsClass()
    a = GroundUnit(4, 4, st)
    print(a, a.name)
