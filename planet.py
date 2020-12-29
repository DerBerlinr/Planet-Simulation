from ursina import *
import time


class Planet(Button):
    def __init__(self, file_name, planet_name, plannr, vel_x=0, vel_y=0, vel_z=0, planet_mass=1, planet_diameter=1, coord_x=0, coord_y=0, coord_z=0):
        super().__init__(
            collision=True,
            model='sphere',
            texture=file_name,
            parent = scene,
            position = [(coord_x, coord_y, coord_z)],
            color = color.white
        )
        self.plannr = plannr
        self.tooltip_input = "0"
        self.planet_name = planet_name
        self.planet_mass = planet_mass
        self.scale = Vec3(planet_diameter, planet_diameter, planet_diameter)
        self.planet_diameter = planet_diameter

        self.poslist = [] # (time, x, y, z, velx, vely, velz)


        self.coord_x = coord_x
        self.coord_y = coord_y
        self.coord_z = coord_z

        self.vel_x = vel_x
        self.vel_y = vel_y
        self.vel_z = vel_z

        self.x = 0
        self.y = 0
        self.z = 0

        self.pressedd = False

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                self.pressedd = True


    def set_coords(self, x, y, z, vx, vy, vz):  # set coordinates of planet
        self.poslist.append((x, y, z, vx, vy, vz))

    def get_coords(self):
        return self.coord_x, self.coord_y, self.coord_z

    def get_vel(self):
        return self.vel_x, self.vel_y, self.vel_z


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            color = color.dark_gray,
            scale = 150,
            double_sided = True
        )
