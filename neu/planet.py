from ursina import *

class Planet(Entity):
    def __init__(self, color, name, speed=1, mass=1, diameter=1, x=0, y=0, z=0):
        super().__init__(
            model='sphere',
            color=color,
            collision=True,
            collider='sphere'
            # TODO: add Textures
        )
        self.name = name
        self.speed = speed
        self.mass = mass
        self.scale = Vec3(diameter, diameter, diameter)
        self.x = x
        self.y = y
        self.z = z

    def set_coords(self, x, y, z):  # set coordinates of planet
        self.x = x
        self.y = y
        self.z = z
        print(x, y, z)

    def get_coords(self):
        return (self.x, self.y, self.z)
