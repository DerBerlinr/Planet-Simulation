import threading
import ursina
import numpy as np
from calc import *
from gui import FirstPersonController
from planet import Planet
import ursina.prefabs.sky as Sky


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

        #Sky()

        planet = Planet(file_name='/textures/planet_1', planet_name="planet1", planet_diameter=1,
                        planet_speed=[10308.531985820431, 27640.154010970804, -0.7364511260199437],
                        coord_x=140699825958.8049,
                        coord_y=-54738590238.00282,
                        coord_z=2510791.537005455)  # create a planet
        self.planet_list.append(planet)

        planet2 = Planet(file_name='/textures/planet_2', planet_name='planet2', planet_diameter=1,
                         planet_speed=[-10308.531985820431, -27640.154010970804, 0.7364511260199437],
                         coord_x=140699825958.8049,
                         coord_y=-50738590238.00282,
                         coord_z=2510791.537005455)
        self.planet_list.append(planet2)


        planet3 = Planet(file_name='/textures/planet_3', planet_name='planet2', planet_diameter=1,
                         planet_speed=[10308.531985820431, -27640.154010970804, 0.7364511260199437],
                         coord_x=140699825958.8049,
                         coord_y=-50738590238.00282,
                         coord_z=2510791.537005455)
        self.planet_list.append(planet3)

        planet4 = Planet(file_name='/textures/planet_4', planet_name='planet2', planet_diameter=1,
                         planet_speed=[-10308.531985820431, 27640.154010970804, 0.7364511260199437],
                         coord_x=-140699825958.8049,
                         coord_y=-50738590238.00282,
                         coord_z=2510791.537005455)
        self.planet_list.append(planet4)




        Planet(file_name='/textures/sun', planet_name="sun", planet_diameter=2.5)




        FirstPersonController()


        for i in self.planet_list:
            # For every planet, there is a thread, which calculates the current Position of its planet
            coord_x, coord_y, coord_z = i.get_coords()
            calc = Calc(posx=coord_x, posy=coord_y, posz=coord_z, velx=i.planet_speed[0], vely=i.planet_speed[1], velz=i.planet_speed[2])
            temp = threading.Thread(target=calc.get_coords, args=(i,))
            temp.start()


        self.app.run()


if __name__ == '__main__':
    main = Main()
