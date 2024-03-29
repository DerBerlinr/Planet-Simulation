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
        # creates planet object
        self.trace = None
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

        self.button_pressed = False

        self.counter = 0

    def input(self, key):
        # checks if a button(planet) gets clicked
        if self.hovered:
            if key == 'left mouse down':
                self.button_pressed = True


    def set_coords(self, x, y, z, vx, vy, vz):
        # appends coordinates and velocities to poslist
        if self.counter == 4:
            if len(self.poslist) > 1000000:
                self.poslist[0] = None
            self.poslist.append((x, y, z, vx, vy, vz))
            self.counter = 0
        else:
            self.counter += 1


    def get_coords(self):
        # returns coords
        return self.coord_x, self.coord_y, self.coord_z

    def get_vel(self):
        # return velocity
        return self.vel_x, self.vel_y, self.vel_z


class Sky(Entity):
    # creates giant sphere which allows to change the background of the simulation
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture='textures/sky',
            scale = 1500,
            double_sided = True
        )
