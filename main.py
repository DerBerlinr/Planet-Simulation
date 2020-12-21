import threading
import ursina
import numpy as np
from calc import *
from gui import FirstPersonController
from planet import Planet, Sky
import sqlite3



class Main:
    def __init__(self,  app,  planet_list=[]):
        # gets called at beginning of program
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        self.app = app


        #self.app = ursina.Ursina()

        ursina.window.title = 'planet simulation'  # set meta data for app
        ursina.window.borderless = True
        ursina.window.fullscreen = True
        ursina.window.exit_button.visible = True
        ursina.window.fps_counter.enabled = True

        self.planet_list = planet_list  # list of all planets in the simulation


        sun = Planet(file_name='/textures/sun', planet_name="sun", planet_diameter=2.5)
        c.execute('''INSERT INTO planets VALUES
            (?,?,?,0,0,0,0,0,0)''', (sun.planet_name, sun.planet_diameter, sun.planet_mass))

        sky = Sky()

        fpc = FirstPersonController(self.planet_list)

        for i in self.planet_list:
            # For every planet, there is a thread, which calculates the current Position of its planet
            coord_x, coord_y, coord_z = i.get_coords()
            calc = Calc(posx=coord_x, posy=coord_y, posz=coord_z, velx=i.planet_speed[0], vely=i.planet_speed[1], velz=i.planet_speed[2])
            temp = threading.Thread(target=calc.get_coords, args=(i,))
            temp.start()


        self.app.run()


if __name__ == '__main__':
    main = Main()
