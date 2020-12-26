from tkinter import *
from planet import Planet
import ursina
from main import Main
from functools import partial
from PIL import Image, ImageTk

class GUI_Startup(Tk):
    def __init__(self, planetlist=[]):
        self.root = Tk()
        self.app = ursina.Ursina()

        Overview = GUI_Planet_Overview

        self.root.title("Main Menu")

        rahmen1 = Frame(self.root, relief=SUNKEN, borderwidth=2)
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

        self.bu4 = Button(rahmen1, text="planet overview", width=groesse, command=Overview)
        self.bu4.grid(row=5, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

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
        root2=Toplevel()
        #self.app = ursina.Ursina()

        root2.title("Planet Overview")

        rahmen1 = Frame(root2, relief=SUNKEN, borderwidth=7)
        rahmen1.pack()

        root2.columnconfigure(0, weight=1)
        root2.columnconfigure(1, weight=2)

        farbe = "#878789"

        abstand_x = 3
        abstand_y = 3

        groesse = 20


        while len(planetlist) < 8:
            planetlist.append(None)


        self.la11_text = StringVar()
        self.la11_text.set("-----------------------------")
        self.la11 = Label(rahmen1, textvariable=self.la11_text, width=groesse, bg=farbe, justify=CENTER)
        self.la11.grid(row=2, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la12_text = StringVar()
        self.la12_text.set("-----------------------------")
        self.la12 = Label(rahmen1, textvariable=self.la12_text, width=groesse, bg=farbe, justify=CENTER)
        self.la12.grid(row=2, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la13_text = StringVar()
        self.la13_text.set("-----------------------------")
        self.la13 = Label(rahmen1, textvariable=self.la13_text, width=groesse, bg=farbe, justify=CENTER)
        self.la13.grid(row=2, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la14_text = StringVar()
        self.la14_text.set("-----------------------------")
        self.la14 = Label(rahmen1, textvariable=self.la14_text, width=groesse, bg=farbe, justify=CENTER)
        self.la14.grid(row=2, column=3, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la15_text = StringVar()
        self.la15_text.set("-----------------------------")
        self.la15 = Label(rahmen1, textvariable=self.la15_text, width=groesse, bg=farbe, justify=CENTER)
        self.la15.grid(row=2, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la16_text = StringVar()
        self.la16_text.set("Planet Overview1")
        self.la16 = Label(rahmen1, textvariable=self.la16_text, width=groesse, justify=CENTER)
        self.la16.grid(row=1, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la17_text = StringVar()
        self.la17_text.set("Planet Overview2")
        self.la17 = Label(rahmen1, textvariable=self.la17_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la17.grid(row=0, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la18_text = StringVar()
        self.la18_text.set("Planet Overview2")
        self.la18 = Label(rahmen1, textvariable=self.la18_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la18.grid(row=3, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la19_text = StringVar()
        self.la19_text.set("Planet Overview2")
        self.la19 = Label(rahmen1, textvariable=self.la19_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la19.grid(row=4, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la20_text = StringVar()
        self.la20_text.set("Planet Overview2")
        self.la20 = Label(rahmen1, textvariable=self.la20_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la20.grid(row=5, column=2, sticky=E, padx=abstand_x, pady=abstand_y)









        load = Image.open("textures/rendered_planet_2_scaled.png")        #code snippet from https://pythonbasics.org/tkinter-image/
        render = ImageTk.PhotoImage(load)

        img = Label(root2, image=render)
        img.image = render
        img.place(x=20, y=10)







        bu_1 = Button(rahmen1, text="add planet", width=groesse, command=partial(self.plan,planetlist[0]))
        bu_1.grid(row=3, column=1, sticky=E, padx=abstand_x, pady=abstand_y)
        ''''
        bu_2 = Button(rahmen1, image="", width=groesse, command=partial(self.plan,planetlist[1]))
        bu_2.grid(row=2, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_3 = Button(rahmen1, image="", width=groesse, command=partial(self.plan,planetlist[2]))
        bu_3.grid(row=3, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_4 = Button(rahmen1, image="", width=groesse, command=partial(self.plan,planetlist[3]))
        bu_4.grid(row=4, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_5 = Button(rahmen1, image="", width=groesse, command=partial(self.plan,planetlist[4]))
        bu_5.grid(row=1, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_6 = Button(rahmen1, image="", width=groesse, command=partial(self.plan,planetlist[5]))
        bu_6.grid(row=2, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_7 = Button(rahmen1, image="", width=groesse, command=partial(self.plan,planetlist[6]))
        bu_7.grid(row=3, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_8 = Button(rahmen1, image="", width=groesse, command=partial(self.plan,planetlist[7]))
        bu_8.grid(row=4, column=1, sticky=E, padx=abstand_x, pady=abstand_y)
        '''''


    def plan(self, planet):
        if planet == None:
            gui_add = GUI_add_Planet()
            new_planet = Planet()



if __name__ == '__main__':
    gui = GUI_Startup()
    mainloop()
