import threading
import ursina
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
                        speed=(10308.531985820431, 27640.154010970804, -0.7364511260199437))  # crate a planet
        planet.set_coords(140699825958.8049, -54738590238.00282, 2510791.537005455)  # set Pos of planet
        self.planet_list.append(planet)

        planet2 = Planet(col=ursina.color.red, name='planet2', diameter=.1)
        planet2.set_coords(140699825958.8049, -54738590238.00282, 2510791.537005455)
        # self.planet_list.append(planet2)

        Planet(col=ursina.color.yellow, name="sun", diameter=.5)

        FirstPersonController()

        for i in self.planet_list:
            # For every planet, there is a thread, which calculates the current Position of its planet
            c = Calc()
            temp = threading.Thread(target=c.get_coords, args=(i,))
            temp.start()

        self.app.run()


if __name__ == '__main__':
    main = Main()
