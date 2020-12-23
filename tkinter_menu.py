from tkinter import *
from planet import Planet
import ursina
from main import Main
from functools import partial

class GUI_Startup(Tk):
    def __init__(self, planetlist=[]):
        Tk.__init__(self)
        self.app = ursina.Ursina()

        self.title("Main Menu")

        rahmen1 = Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        farbe = "#878789"

        abstand_x = 3
        abstand_y = 3

        groesse = 20

        self.bu1 = Button(rahmen1, text="Own config", width=groesse, command=self.own_planets)
        self.bu1.grid(row=1, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2 = Button(rahmen1, text="2 Planets", width=groesse, command=self.two_planets)
        self.bu2.grid(row=2, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu3 = Button(rahmen1, text="viel", width=groesse, command=self.solar_sys)
        self.bu3.grid(row=3, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.planet_list = planetlist


    def own_planets(self):
        pass

    def two_planets(self):
        planet = Planet(file_name='/textures/planet_1',planet_name="planet1", planet_diameter=1, plannr=1,
                        planet_speed=[10308.531985820431, 27640.154010970804, -0.7364511260199437],
                        coord_x=140699825958.8049,
                        coord_y=-54738590238.00282,
                        coord_z=2510791.537005455)  # create a planet
        self.planet_list.append(planet)

        planet2 = Planet(file_name='/textures/planet_2',planet_name='planet2', planet_diameter=1, plannr=2,
                         planet_speed=[10308.531985820431, -27640.154010970804, -0.7364511260199437],
                         coord_x=140699825958.8049,
                         coord_y=-54738590238.00282,
                         coord_z=-2510791.537005455)  # create a planet

        self.planet_list.append(planet2)

        start = Main(self.app, self.planet_list)


    def solar_sys(self):
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


        planet3 = Planet(file_name='/textures/planet_3', planet_name='planet3', planet_diameter=1,
                         planet_speed=[10308.531985820431, -27640.154010970804, 0.7364511260199437],
                         coord_x=140699825958.8049,
                         coord_y=-50738590238.00282,
                         coord_z=2510791.537005455)
        self.planet_list.append(planet3)

        planet4 = Planet(file_name='/textures/planet_4', planet_name='planet4', planet_diameter=1,
                         planet_speed=[-10308.531985820431, 27640.154010970804, 0.7364511260199437],
                         coord_x=-140699825958.8049,
                         coord_y=-50738590238.00282,
                         coord_z=2510791.537005455)
        self.planet_list.append(planet4)

        start = Main(self.app, self.planet_list)


class GUI_add_Planet(Tk):
    def __init__(self, name="", mass="", vx="", vy="", vz="", x="", y="", z=""):
        Tk.__init__(self)

        self.title("Add Planet")

        rahmen1 = Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        farbe = "#878787"

        abstand_x = 3
        abstand_y = 3

        groesse = 24

        self.la1_text = StringVar()
        self.la1_text.set("Name:")
        self.la1 = Label(rahmen1, textvariable=self.la1_text, width=groesse, bg=farbe, justify=CENTER)
        self.la1.grid(row=0, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.en1_text = StringVar()
        self.en1_text.set(name)
        self.en1 = Entry(rahmen1, width=groesse+9, textvariable=self.en1_text)
        self.en1.grid(row=0, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la2_text = StringVar()
        self.la2_text.set("Mass in kg:")
        self.la2 = Label(rahmen1, textvariable=self.la2_text, width=groesse, bg=farbe, justify=CENTER)
        self.la2.grid(row=1, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.en2_text = StringVar()
        self.en2_text.set(mass)
        self.en2 = Entry(rahmen1, width=groesse+9, textvariable=self.en2_text)
        self.en2.grid(row=1, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la3_text = StringVar()
        self.la3_text.set("Speed in m/s (x;y;z):")
        self.la3 = Label(rahmen1, textvariable=self.la3_text, width=groesse, bg=farbe, justify=CENTER)
        self.la3.grid(row=2, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.en3_1_text = StringVar()
        self.en3_1_text.set(vx)
        self.en3_1 = Entry(rahmen1, width=round(groesse / 3), textvariable=self.en3_1_text)
        self.en3_1.grid(row=3, column=1, sticky=W, padx=abstand_x, pady=abstand_y)

        self.en3_2_text = StringVar()
        self.en3_2_text.set(vy)
        self.en3_2 = Entry(rahmen1, width=round(groesse / 3), textvariable=self.en3_2_text)
        self.en3_2.grid(row=3, column=1, padx=abstand_x, pady=abstand_y)

        self.en3_3_text = StringVar()
        self.en3_3_text.set(vz)
        self.en3_3 = Entry(rahmen1, width=round(groesse / 3), textvariable=self.en3_3_text)
        self.en3_3.grid(row=3, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la4_text = StringVar()
        self.la4_text.set("Position (x;y;z):")
        self.la4 = Label(rahmen1, textvariable=self.la4_text, width=groesse, bg=farbe, justify=CENTER)
        self.la4.grid(row=3, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.en4_1_text = StringVar()
        self.en4_1_text.set(x)
        self.en4_1 = Entry(rahmen1, width=round(groesse/3), textvariable=self.en4_1_text)
        self.en4_1.grid(row=3, column=1, sticky=W, padx=abstand_x, pady=abstand_y)

        self.en4_2_text = StringVar()
        self.en4_2_text.set(y)
        self.en4_2 = Entry(rahmen1, width=round(groesse/3), textvariable=self.en4_2_text)
        self.en4_2.grid(row=3, column=1, padx=abstand_x, pady=abstand_y)

        self.en4_3_text = StringVar()
        self.en4_3_text.set(z)
        self.en4_3 = Entry(rahmen1, width=round(groesse/3), textvariable=self.en4_3_text)
        self.en4_3.grid(row=3, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu1 = Button(rahmen1, text="Submit", width=groesse+3, command=self.submit)
        self.bu1.grid(row=4, column=1, padx=abstand_x, pady=abstand_y)

        #self.la4_text = StringVar()
        #self.la4_text.set("Position (x;y;z):")
        #self.la4 = Label(rahmen1, textvariable=self.la2_text, width=groesse, bg=farbe, justify=CENTER)
        #self.la4.grid(row=3, column=0, columnspan=2, padx=abstand_x, pady=abstand_y)

        self.planet_list = []

    def submit(self):
        while 1:
            if self.en1_text.get() and self.en2_text and self.en3_text and self.en4_1_text and self.en4_2_text and self.en4_3_text:
                self.destroy()
                return self.en1_text, self.en2_text, self.en3_text, self.en4_1_text, self.en4_2_text, self.en4_3_text
            else:
                print(HELLO)

class GUI_Planet_Overview(Tk):
    def __init__(self, planetlist=[]):
        Tk.__init__(self)
        self.app = ursina.Ursina()

        self.title("Planet Overview")

        rahmen1 = Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        farbe = "#878789"

        abstand_x = 3
        abstand_y = 3

        groesse = 20

        while len(planetlist) < 8:
            planetlist.append(None)

        bu_1 = Button(rahmen1, image="", width=groesse, command=partial(self.plan,planetlist[1]))
        bu_1.grid(row=1, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_2 = Button(rahmen1, image="", width=groesse, command=partial(self.plan,planetlist[2]))
        bu_2.grid(row=2, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_3 = Button(rahmen1, image="", width=groesse, command=partial(self.plan,planetlist[3]))
        bu_3.grid(row=3, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_4 = Button(rahmen1, image="", width=groesse, command=partial(self.plan,planetlist[4]))
        bu_4.grid(row=4, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_5 = Button(rahmen1, image="", width=groesse, command=partial(self.plan,planetlist[5]))
        bu_5.grid(row=1, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_6 = Button(rahmen1, image="", width=groesse, command=partial(self.plan,planetlist[6]))
        bu_6.grid(row=2, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_7 = Button(rahmen1, image="", width=groesse, command=partial(self.plan,planetlist[7]))
        bu_7.grid(row=3, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_8 = Button(rahmen1, image="", width=groesse, command=partial(self.plan,planetlist[8]))
        bu_8.grid(row=4, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

    def plan(self, planet):
        if planet == None:
            gui_add = GUI_add_Planet()
            new_planet = Planet()



if __name__ == '__main__':
    gui = GUI_Startup()
    mainloop()
