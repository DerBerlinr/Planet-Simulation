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


        while len(planetlist) < 10:
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
        self.la16_text.set("Planet Overview")
        self.la16 = Label(rahmen1, textvariable=self.la16_text, width=groesse, justify=CENTER)
        self.la16.grid(row=1, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la17_text = StringVar()
        self.la17_text.set("-")
        self.la17 = Label(rahmen1, textvariable=self.la17_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la17.grid(row=0, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la18_text = StringVar()
        self.la18_text.set("-2")
        self.la18 = Label(rahmen1, textvariable=self.la18_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la18.grid(row=3, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la19_text = StringVar()
        self.la19_text.set("-")
        self.la19 = Label(rahmen1, textvariable=self.la19_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la19.grid(row=4, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la20_text = StringVar()
        self.la20_text.set("-")
        self.la20 = Label(rahmen1, textvariable=self.la20_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la20.grid(row=5, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la21_text = StringVar()
        self.la21_text.set("Status")
        self.la21 = Label(rahmen1, textvariable=self.la21_text, width=groesse, bg="light green", justify=CENTER)
        self.la21.grid(row=4, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la22_text = StringVar()
        self.la22_text.set("-")
        self.la22 = Label(rahmen1, textvariable=self.la22_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la22.grid(row=6, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la23_text = StringVar()
        self.la23_text.set("-")
        self.la23 = Label(rahmen1, textvariable=self.la23_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la23.grid(row=7, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la24_text = StringVar()
        self.la24_text.set("-")
        self.la24 = Label(rahmen1, textvariable=self.la24_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la24.grid(row=8, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la25_text = StringVar()
        self.la25_text.set("Status")
        self.la25 = Label(rahmen1, textvariable=self.la25_text, width=groesse, bg="light green", justify=CENTER)
        self.la25.grid(row=8, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la26_text = StringVar()
        self.la26_text.set("Status")
        self.la26 = Label(rahmen1, textvariable=self.la26_text, width=groesse, bg="indian red", justify=CENTER)
        self.la26.grid(row=12, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la27_text = StringVar()
        self.la27_text.set("Status")
        self.la27 = Label(rahmen1, textvariable=self.la27_text, width=groesse, bg="indian red", justify=CENTER)
        self.la27.grid(row=16, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la28_text = StringVar()
        self.la28_text.set("-")
        self.la28 = Label(rahmen1, textvariable=self.la28_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la28.grid(row=9, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la29_text = StringVar()
        self.la29_text.set("-")
        self.la29 = Label(rahmen1, textvariable=self.la29_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la29.grid(row=10, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la30_text = StringVar()
        self.la30_text.set("-")
        self.la30 = Label(rahmen1, textvariable=self.la30_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la30.grid(row=11, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la31_text = StringVar()
        self.la31_text.set("-")
        self.la31 = Label(rahmen1, textvariable=self.la31_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la31.grid(row=12, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la32_text = StringVar()
        self.la32_text.set("-")
        self.la32 = Label(rahmen1, textvariable=self.la32_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la32.grid(row=13, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la33_text = StringVar()
        self.la33_text.set("-")
        self.la33 = Label(rahmen1, textvariable=self.la33_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la33.grid(row=14, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la34_text = StringVar()
        self.la34_text.set("-")
        self.la34 = Label(rahmen1, textvariable=self.la34_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la34.grid(row=15, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la35_text = StringVar()
        self.la35_text.set("-")
        self.la35 = Label(rahmen1, textvariable=self.la35_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la35.grid(row=16, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la36_text = StringVar()
        self.la36_text.set("-")
        self.la36 = Label(rahmen1, textvariable=self.la36_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la36.grid(row=17, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la37_text = StringVar()
        self.la37_text.set("-")
        self.la37 = Label(rahmen1, textvariable=self.la37_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la37.grid(row=18, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la38_text = StringVar()
        self.la38_text.set("-")
        self.la38 = Label(rahmen1, textvariable=self.la38_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la38.grid(row=19, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu1 = Button(rahmen1, text="Return", width=groesse, command=self.return_to_gui())
        self.bu1.grid(row=24, column=4, padx=abstand_x, pady=abstand_y)

        self.la39_text = StringVar()
        self.la39_text.set("Status")
        self.la39 = Label(rahmen1, textvariable=self.la39_text, width=groesse, bg="light green", justify=CENTER)
        self.la39.grid(row=4, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la40_text = StringVar()
        self.la40_text.set("Status")
        self.la40 = Label(rahmen1, textvariable=self.la40_text, width=groesse, bg="indian red", justify=CENTER)
        self.la40.grid(row=8, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la41_text = StringVar()
        self.la41_text.set("Status")
        self.la41 = Label(rahmen1, textvariable=self.la41_text, width=groesse, bg="indian red", justify=CENTER)
        self.la41.grid(row=12, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la42_text = StringVar()
        self.la42_text.set("Status")
        self.la42 = Label(rahmen1, textvariable=self.la42_text, width=groesse, bg="indian red", justify=CENTER)
        self.la42.grid(row=16, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la43_text = StringVar()
        self.la43_text.set("Status")
        self.la43 = Label(rahmen1, textvariable=self.la43_text, width=groesse, bg="indian red", justify=CENTER)
        self.la43.grid(row=20, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la44_text = StringVar()
        self.la44_text.set("Status")
        self.la44 = Label(rahmen1, textvariable=self.la44_text, width=groesse, bg="indian red", justify=CENTER)
        self.la44.grid(row=20, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la45_text = StringVar()
        self.la45_text.set("-")
        self.la45 = Label(rahmen1, textvariable=self.la45_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la45.grid(row=21, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la46_text = StringVar()
        self.la46_text.set("-")
        self.la46 = Label(rahmen1, textvariable=self.la46_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la46.grid(row=22, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la47_text = StringVar()
        self.la47_text.set("-")
        self.la47 = Label(rahmen1, textvariable=self.la47_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la47.grid(row=23, column=2, sticky=E, padx=abstand_x, pady=abstand_y)









        load1 = Image.open("textures/rendered_sun_scaled.png")        #code snippet from https://pythonbasics.org/tkinter-image/
        render = ImageTk.PhotoImage(load1)

        img1 = Label(root2, image=render)
        img1.image = render
        img1.place(x=30, y=90)

        load3 = Image.open("textures/rendered_planet_2_scaled.png")
        render = ImageTk.PhotoImage(load3)

        img3 = Label(root2, image=render)
        img3.image = render
        img3.place(x=30, y=205)

        load5 = Image.open("textures/rendered_planet_4_scaled.png")
        render = ImageTk.PhotoImage(load5)

        img5 = Label(root2, image=render)
        img5.image = render
        img5.place(x=30, y=320)

        load7 = Image.open("textures/rendered_planet_6_scaled.png")
        render = ImageTk.PhotoImage(load7)

        img7 = Label(root2, image=render)
        img7.image = render
        img7.place(x=30, y=435)

        load9 = Image.open("textures/rendered_planet_8_scaled.png")
        render = ImageTk.PhotoImage(load9)

        img9 = Label(root2, image=render)
        img9.image = render
        img9.place(x=30, y=550)

        load2 = Image.open(
            "textures/rendered_planet_1_scaled.png")  # code snippet from https://pythonbasics.org/tkinter-image/
        render = ImageTk.PhotoImage(load2)

        img2 = Label(root2, image=render)
        img2.image = render
        img2.place(x=490, y=90)

        load4 = Image.open("textures/rendered_planet_3_scaled.png")
        render = ImageTk.PhotoImage(load4)

        img4 = Label(root2, image=render)
        img4.image = render
        img4.place(x=490, y=205)

        load6 = Image.open("textures/rendered_planet_5_scaled.png")
        render = ImageTk.PhotoImage(load6)

        img6 = Label(root2, image=render)
        img6.image = render
        img6.place(x=490, y=320)

        load8 = Image.open("textures/rendered_planet_7_scaled.png")
        render = ImageTk.PhotoImage(load8)

        img8 = Label(root2, image=render)
        img8.image = render
        img8.place(x=490, y=435)

        load10 = Image.open("textures/rendered_planet_9_scaled.png")
        render = ImageTk.PhotoImage(load10)

        img10 = Label(root2, image=render)
        img10.image = render
        img10.place(x=490, y=550)









        bu_1 = Button(rahmen1, text="Add planet", width=groesse, command=partial(self.plan,planetlist[0]))
        bu_1.grid(row=5, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_3 = Button(rahmen1, text="Add planet", image="", width=groesse, command=partial(self.plan,planetlist[1]))
        bu_3.grid(row=9, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_5 = Button(rahmen1, text="Add planet", image="", width=groesse, command=partial(self.plan,planetlist[2]))
        bu_5.grid(row=13, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_7 = Button(rahmen1, text="Add planet", image="", width=groesse, command=partial(self.plan,planetlist[3]))
        bu_7.grid(row=17, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_2 = Button(rahmen1, text="Add planet", image="", width=groesse, command=partial(self.plan,planetlist[4]))
        bu_2.grid(row=5, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_4 = Button(rahmen1, text="Add planet", image="", width=groesse, command=partial(self.plan,planetlist[5]))
        bu_4.grid(row=9, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_6 = Button(rahmen1, text="Add planet", image="", width=groesse, command=partial(self.plan,planetlist[6]))
        bu_6.grid(row=13, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_8 = Button(rahmen1, text="Add planet", image="", width=groesse, command=partial(self.plan,planetlist[7]))
        bu_8.grid(row=17, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_9 = Button(rahmen1, text="Add planet", image="", width=groesse, command=partial(self.plan, planetlist[8]))
        bu_9.grid(row=21, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_10 = Button(rahmen1, text="Add planet", image="", width=groesse, command=partial(self.plan, planetlist[9]))
        bu_10.grid(row=21, column=4, sticky=E, padx=abstand_x, pady=abstand_y)


    def return_to_gui(self):
        pass

    def plan(self, planet):
        if planet == None:
            gui_add = GUI_add_Planet()
            new_planet = Planet()



if __name__ == '__main__':
    gui = GUI_Startup()
    mainloop()
