from ursina import *
import time


class Planet(Entity):
    def __init__(self, file_name, planet_name, planet_speed=1, planet_mass=1, planet_diameter=1, coord_x=0, coord_y=0, coord_z=0):
        super().__init__(
            collision=True,
            model='sphere',
            texture=file_name,
            # TODO: add Textures
        )
        self.planet_name = planet_name
        self.planet_speed = planet_speed
        self.planet_mass = planet_mass
        self.scale = Vec3(planet_diameter, planet_diameter, planet_diameter)
        self.planet_diameter = planet_diameter


        self.coord_x = coord_x
        self.coord_y = coord_y
        self.coord_z = coord_z




    def set_coords(self, x, y, z):  # set coordinates of planet
        self.x = x / 10000000000
        self.y = y / 10000000000
        self.z = z / 10000000000

    def get_coords(self):
        return self.coord_x, self.coord_y, self.coord_z
