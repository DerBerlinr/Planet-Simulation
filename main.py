import threading
import ursina
import numpy as np
from calc import *
from gui import FirstPersonController
from planet import Planet


class Main:
    def __init__(self):
        # gets called at beginning of program

        self.app = ursina.Ursina()

        ursina.window.title = 'planet simulation'  # set meta data for app
        ursina.window.borderless = True
        ursina.window.fullscreen = True
        ursina.window.exit_button.visible = True
        ursina.window.fps_counter.enabled = True

        self.planet_list = []  # list of all planets in the simulation

        planet = Planet(col=ursina.color.orange, name="planet1", diameter=.1,
                        speed=[10308.531985820431, 27640.154010970804, -0.7364511260199437],
                        a=140699825958.8049,
                        y=-54738590238.00282,
                        z=2510791.537005455)  # create a planet
        self.planet_list.append(planet)

        planet2 = Planet(col=ursina.color.red, name='planet2', diameter=.1, a=140699825958.8049, y=-54738590238.00282, z=2510791.537005455)
        # self.planet_list.append(planet2)

        Planet(col=ursina.color.yellow, name="sun", diameter=.5)



        for i in self.planet_list:
            # For every planet, there is a thread, which calculates the current Position of its planet
            a, b, c = i.get_coords()
            print("a = ", a)
            c = Calc(posx=a, posy=b, posz=c)
            temp = threading.Thread(target=c.get_coords, args=(i,))
            temp.start()

        FirstPersonController()

        self.app.run()


if __name__ == '__main__':
    main = Main()
