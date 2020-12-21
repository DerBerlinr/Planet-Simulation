import threading
import ursina
import numpy as np
from calc import *
from gui import FirstPersonController
from planet import Planet


class Main:
    def __init__(self, planet_list=[]):
        # gets called at beginning of program

        self.app = ursina.Ursina()

        ursina.window.title = 'planet simulation'  # set meta data for app
        ursina.window.borderless = True
        ursina.window.fullscreen = True
        ursina.window.exit_button.visible = True
        ursina.window.fps_counter.enabled = True

        self.planet_list = planet_list  # list of all planets in the simulation

        Planet(planet_col=ursina.color.yellow, planet_name="sun", planet_diameter=2.5)

        fpc = FirstPersonController()

        for i in self.planet_list:
            # For every planet, there is a thread, which calculates the current Position of its planet
            coord_x, coord_y, coord_z = i.get_coords()
            calc = Calc(posx=coord_x, posy=coord_y, posz=coord_z)
            temp = threading.Thread(target=calc.get_coords, args=(i,))
            temp.start()


        self.app.run()


if __name__ == '__main__':
    main = Main()
