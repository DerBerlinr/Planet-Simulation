import threading
import ursina
import numpy as np
from calc import *
from gui import FirstPersonController
from planet import Planet, Sky
import sqlite3



class Main:
    def __init__(self,  app,  planet_list=[]):
        # SET BASIC VARIABLES FOR ursina -------------------------------------------------------
        self.app = app

        ursina.window.title = 'planet simulation'  # set meta data for app
        ursina.window.borderless = True
        ursina.window.fullscreen = True
        ursina.window.exit_button.visible = True
        ursina.window.fps_counter.enabled = True

        self.planet_list = planet_list  # list of all planets in the simulation

        # CREATION OF SUN AND INSERTION INTO DATABASE ---------------------------------------------

        conn = sqlite3.connect('example.db')
        c = conn.cursor()

        sun = Planet(file_name='/textures/sun', planet_name="sun", planet_diameter=2.5)

        self.c.execute('''INSERT INTO planets VALUES (0,?,?,?)''',
                       (sun.planet_name, sun.planet_dsunameter, sun.planet_mass))

        self.conn.commit()
        self.c.close()

        # CREATION OF SKY ----------------------------------------------------------------------

        sky = Sky()

        fpc = FirstPersonController(self.planet_list)

        for i in self.planet_list:
            # For every planet, there is a thread, which calculates the current Position of its planet
            calc = Calc(i)
            temp = threading.Thread(target=calc.get_coords, args=(i,))
            temp.start()


        self.app.run()


if __name__ == '__main__':
    main = Main()
