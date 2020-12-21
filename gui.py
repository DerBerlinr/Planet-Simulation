import ursina
from direct.stdpy.file import execfile
from ursina import *
import calc as calc
import numpy as np
from planet import Planet
#from tkinter_menu import GUI_Startup
import threading


class GUI:
    def __init__(self):

        self.planet_list = []  # list of all planets in the simulation

        # IN-GAME-MENU -------------------------------------------------------------------------------------------------
        self.buttons_gm = []

        self.bu_reenter = Button(position=(0, .25, 0), text='Reenter Game', scale=(.5, .07))
        self.buttons_gm.append(self.bu_reenter)
        self.bu_reenter.on_click = self.reenter_game

        self.bu_add = Button(position=(0, .15, 0), text='Add Planet', scale=(.5, .07))
        self.buttons_gm.append(self.bu_add)
        self.bu_add.on_click = self.add_planet

        self.bu_menu = Button(position=(0, -.15, 0), text='Go to Menu', scale=(.5, .07))
        self.buttons_gm.append(self.bu_menu)
        self.bu_menu.on_click = self.go_to_menu

        self.planet_data_temp = []

    def go_to_menu(self):
        print("Anfang")
        execfile('tkinter_menu.py')
        exit()
        print("Ende")




    def reenter_game(self):
        mouse.locked = True

    def add_planet(self):
        # TODO: fix lag
        for i in self.buttons_gm:
            i.enabled = False

        name_field = InputField(name='name_field')
        mass_field = InputField(name='mass_field')
        speed_field = InputField(name='speed_field')
        pos_x_field = InputField(name='pos_x_field')
        pos_y_field = InputField(name='pos_y_field')
        pos_z_field = InputField(name='pos_z_field')

        self.planet_data_temp.append(name_field)
        self.planet_data_temp.append(mass_field)
        self.planet_data_temp.append(speed_field)
        self.planet_data_temp.append(pos_x_field)
        self.planet_data_temp.append(pos_y_field)
        self.planet_data_temp.append(pos_z_field)

        win = WindowPanel(
            title='add planet',
            content=(
                Text('name:'),
                name_field,
                Text('mass in kg:'),
                mass_field,
                Text('speed in m/s:'),
                speed_field,
                Text('x-position:'),
                pos_x_field,
                Text('y-position:'),
                pos_y_field,
                Text('z-position:'),
                pos_z_field,
                Button(text='Submit', color=color.azure, on_click=self.submit_planet_data)
            ),
        )
        self.planet_data_temp.append(win)

    @staticmethod
    def submit_planet_data():
        """
        name = planet_data_temp[0].text
        mass = int(planet_data_temp[1].text)
        speed = int(planet_data_temp[2].text)
        pos_x = int(planet_data_temp[3].text)
        pos_y = int(planet_data_temp[4].text)
        pos_z = int(planet_data_temp[5].text)
        temp = Planet(color=color.blue, name=name, speed=speed, mass=mass, x=pos_x, y=pos_y, z=pos_z)
        planet_data_temp[6].close()
        mouse.locked = True
        """
        exit()


class FirstPersonController(Entity):
    def __init__(self, planet_list):
        self.planet_list = planet_list
        super().__init__()


        self.speed = 5

        self.camera_pivot = Entity(parent=self, y=2)
        self.cursor = Entity(parent=camera.ui, model='quad', color=color.pink, scale=.008, rotation_z=45)

        camera.parent = self.camera_pivot
        camera.position = (0, 0, 0)
        camera.rotation = (0, 0, 0)
        camera.fov = 90
        mouse.locked = True
        self.direction = 0
        self.mouse_sensitivity = Vec2(40, 40)
        self.target_smoothing = 100
        self.smoothing = self.target_smoothing

        self.hud_coords = ''
        self.hud_text_coords = Text(text=self.hud_coords, origin=(0, 18))

        self.gui = GUI()

    def update(self):
        if mouse.locked:
            for i in self.gui.buttons_gm:
                i.enabled = False

            # CAMERA ROTATION ------------------------------------------------------
            self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity[1]

            self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[0]
            self.camera_pivot.rotation_x = clamp(self.camera_pivot.rotation_x, -90, 90)

            # CAMERA POSITION ------------------------------------------------------
            self.direction = Vec3(self.forward * (held_keys['w'] - held_keys['s']) +
                                  self.right * (held_keys['d'] - held_keys['a']) +
                                  self.up * (held_keys['space'] - held_keys['shift'])
                                  ).normalized()

            self.position += self.direction / 2 * self.speed * time.dt


            # print(self.position)
            # self.a.update_text(str(self.position[0]) + str(self.position[1]) + str(self.position[2]))

            # PLANET POS -----------------------------------------------------------
            self.hud_coords = "x: " + str(round(self.x)) + "     y: " + str(round(self.y)) + "     z: " + str(
                round(self.z))
            self.hud_text_coords.color = color.red
            for i in self.planet_list:
                if
                i.hud_text_coords.text = i.hud_coords

            # g, r, d = Main.planet_list[0].get_coords
            # Planet(planet_col=ursina.color.green, planet_name="", planet_diameter=.05,
            # planet_speed=0,
            # coord_x=g,
            # coord_y=r,
            # coord_z=d)

        # EXIT FPC -----------------------------------------------------------------
        if held_keys['escape']:
            for i in self.gui.buttons_gm:
                i.enabled = True
            mouse.locked = False
