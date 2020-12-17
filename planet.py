from ursina import *
import time


class Planet(Entity):
    def __init__(self, col, name, speed=1, mass=1, diameter=1, a=0, y=0, z=0):
        super().__init__(
            model='sphere',
            color=col,
            collision=True,
            collider='sphere'
            # TODO: add Textures
        )
        self.name = name
        self.speed = speed
        self.mass = mass
        self.scale = Vec3(diameter, diameter, diameter)

        print('a', name , a)
        self.x = a
        print('Das self.x', name, self.x)
        self.y = y
        self.z = z

    def set_coords(self, x, y, z):  # set coordinates of planet
        self.x = x / 100000000000
        self.y = y / 100000000000
        self.z = z / 100000000000

    def get_coords(self):
        print("Getcoords: ", self.x)
        return self.x, self.y, self.z
