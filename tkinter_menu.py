from tkinter import *
from planet import Planet
import ursina
from main import Main
from PIL import Image, ImageTk
import os
import ctypes


class GUI_Startup(Tk):
    def __init__(self, planetlist=[]):
        # main menu to choose your preset/own config
        self.root=Tk()
        self.app=ursina.Ursina()

        self.root.title("Main Menu")
        self.root.geometry("750x300")
        self.root.resizable(True, True)

        rahmen1=Frame(self.root, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        farbe="#878789"

        abstand_x=3
        abstand_y=3

        groesse=25

        self.bu1=Button(rahmen1, text="Run Custom setup", width=groesse, highlightbackground='#3E4149', command=self.own_planets)
        self.bu1.grid(row=4, column=3, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2=Button(rahmen1, text="Run Pre-setup (2 Planets)", width=groesse, highlightbackground='#3E4149', command=self.two_planets)
        self.bu2.grid(row=6, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu3=Button(rahmen1, text="Run Pre-setup (4 Planets)", width=groesse, highlightbackground='#3E4149', command=self.solar_sys)
        self.bu3.grid(row=6, column=3, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu4=Button(rahmen1, text="Customize Planets", width=groesse, highlightbackground='#3E4149', command=self.ov)
        self.bu4.grid(row=4, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu5=Button(rahmen1, text="Exit", width=groesse, highlightbackground='#3E4149', command=self.exit)
        self.bu5.grid(row=9, column=3, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu6=Button(rahmen1, text="Copyright", width=groesse, highlightbackground='#3E4149', command=self.copyright)
        self.bu6.grid(row=9, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Create a Custom Simulation:")
        self.la1=Label(rahmen1, textvariable=self.la1_text, width=groesse, justify=CENTER)
        self.la1.grid(row=4, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la2_text=StringVar()
        self.la2_text.set("Run a Pre-setup Simulation:")
        self.la2=Label(rahmen1, textvariable=self.la2_text, width=groesse, justify=CENTER)
        self.la2.grid(row=6, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la12_text=StringVar()
        self.la12_text.set("-----------------------------------------")
        self.la12=Label(rahmen1, textvariable=self.la12_text, width=groesse, justify=CENTER)
        self.la12.grid(row=2, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la13_text=StringVar()
        self.la13_text.set("-----------------------------------------")
        self.la13=Label(rahmen1, textvariable=self.la13_text, width=groesse, justify=CENTER)
        self.la13.grid(row=2, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la14_text=StringVar()
        self.la14_text.set("-----------------------------------------")
        self.la14=Label(rahmen1, textvariable=self.la14_text, width=groesse, justify=CENTER)
        self.la14.grid(row=2, column=3, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la16_text=StringVar()
        self.la16_text.set("Initialise a Simulation")
        self.la16=Label(rahmen1, textvariable=self.la16_text, bg="light grey", width=groesse, justify=CENTER)
        self.la16.grid(row=1, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la17_text=StringVar()
        self.la17_text.set("-")
        self.la17=Label(rahmen1, textvariable=self.la17_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la17.grid(row=3, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la18_text=StringVar()
        self.la18_text.set("-")
        self.la18=Label(rahmen1, textvariable=self.la18_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la18.grid(row=5, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la19_text=StringVar()
        self.la19_text.set("-")
        self.la19=Label(rahmen1, textvariable=self.la19_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la19.grid(row=7, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la20_text=StringVar()
        self.la20_text.set("-")
        self.la20=Label(rahmen1, textvariable=self.la20_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la20.grid(row=8, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.planet_list=planetlist

    def exit(self):
        # closes the program
        exit()

    def ov(self):
        # opens planet overview
        try:
            a=self.ov.farbe
            try:
                self.ov.root2.lift()
            except:
                self.ov.deiconfy()
        except:
            self.ov=GUI_Planet_Overview(self, self.planet_list)

    def copyright(self):
        # opens license.txt
        os.system('start " " license.txt')

    def own_planets(self):
        # Initialises your own config
        self.planet_list=self.rem_none(self.planet_list)
        Main(self.app, self.planet_list)

    def rem_none(self, list):
        # Removes all None-items from list so only planet objects remain
        c=0
        temp=[]
        for element in list:
            if element != None:
                temp.append(element)
            c += 1
        return temp

    def two_planets(self):
        # preset for 2 planets
        self.planet_list=[]
        planet=Planet(file_name='/textures/planet_1', planet_name="planet1", planet_diameter=1, plannr=1,
                        vel_x=10308.531985820431,
                        vel_y=27640.154010970804,
                        vel_z=-0.7364511260199437,
                        coord_x=140699825958.8049,
                        coord_y=-54738590238.00282,
                        coord_z=2510791.537005455)  # create a planet
        self.planet_list.append(planet)

        planet2=Planet(file_name='/textures/planet_2', planet_name='planet2', planet_diameter=1, plannr=2,
                         vel_x=40300.531985820431,
                         vel_y=-26764.154010970804,
                         vel_z=-50000.7364511260199437,
                         coord_x=-9510791.537005455,
                         coord_y=-12473859023.00282,
                         coord_z=44069982595.8049)  # create a planet

        self.planet_list.append(planet2)

        start=Main(self.app, self.planet_list)

    def solar_sys(self):
        # preset for 4 planets
        self.planet_list=[]
        planet=Planet(file_name='/textures/planet_1', planet_name="planet1", planet_diameter=1, plannr=1,
                        vel_x=10308.531985820431,
                        vel_y=27640.154010970804,
                        vel_z=-10000.7364511260199437,
                        coord_x=140699825958.8049,
                        coord_y=-54738590238.00282,
                        coord_z=2710791.537005455)  # create a planet
        self.planet_list.append(planet)

        planet2=Planet(file_name='/textures/planet_2', planet_name='planet2', planet_diameter=1, plannr=2,
                         vel_x=-10308.531985820431,
                         vel_y=-20640.154010970804,
                         vel_z=0.7364511260199437,
                         coord_x=240699825958.8049,
                         coord_y=-50738590238.00282,
                         coord_z=2110791.537005455)
        self.planet_list.append(planet2)

        planet3=Planet(file_name='/textures/planet_3', planet_name='planet3', planet_diameter=1, plannr=3,
                         vel_x=9308.531985820431,
                         vel_y=-0.154010970804,
                         vel_z=20000.7364511260199437,
                         coord_x=190699825958.8049,
                         coord_y=-50738590238.00282,
                         coord_z=2510791.537005455)
        self.planet_list.append(planet3)

        planet4=Planet(file_name='/textures/planet_4', planet_name='planet4', planet_diameter=1, plannr=4,
                         vel_x=-15308.531985820431,
                         vel_y=21640.154010970804,
                         vel_z=0.7364511260199437,
                         coord_x=-140699825958.8049,
                         coord_y=-50738590238.00282,
                         coord_z=2510791.537005455)
        self.planet_list.append(planet4)

        start=Main(self.app, self.planet_list)


class GUI_add_Planet(Tk):
    def __init__(self, planet_number, overview, name="Planet", mass="10000", vx="-30000", vy="30000", vz="30000", x="-16070000000", y="-65040000000", z="3500800"):
        # window to insert planet data and to save data for later usage
        self.root=Toplevel()
        self.lock=False

        self.root.title("Edit planet: " + name)

        self.planet_number=planet_number

        rahmen1=Frame(self.root, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        farbe="light grey"
        self.overview=overview

        abstand_x=3
        abstand_y=3

        groesse=24

        self.la1_text=StringVar()
        self.la1_text.set("Name:")
        self.la1=Label(rahmen1, textvariable=self.la1_text, width=groesse, bg=farbe, justify=CENTER)
        self.la1.grid(row=0, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.en1_text=StringVar()
        self.en1_text.set(name)
        self.en1=Entry(rahmen1, width=groesse + 9, textvariable=self.en1_text)
        self.en1.grid(row=0, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la2_text=StringVar()
        self.la2_text.set("Mass in kg:")
        self.la2=Label(rahmen1, textvariable=self.la2_text, width=groesse, bg=farbe, justify=CENTER)
        self.la2.grid(row=1, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.en2_text=StringVar()
        self.en2_text.set(mass)
        self.en2=Entry(rahmen1, width=groesse + 9, textvariable=self.en2_text)
        self.en2.grid(row=1, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la3_text=StringVar()
        self.la3_text.set("Velocity in m/s (x;y;z):")
        self.la3=Label(rahmen1, textvariable=self.la3_text, width=groesse, bg=farbe, justify=CENTER)
        self.la3.grid(row=2, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.en3_1_text=StringVar()
        self.en3_1_text.set(vx)
        self.en3_1=Entry(rahmen1, width=round(groesse / 3), textvariable=self.en3_1_text)
        self.en3_1.grid(row=2, column=1, sticky=W, padx=abstand_x, pady=abstand_y)

        self.en3_2_text=StringVar()
        self.en3_2_text.set(vy)
        self.en3_2=Entry(rahmen1, width=round(groesse / 3), textvariable=self.en3_2_text)
        self.en3_2.grid(row=2, column=1, padx=abstand_x, pady=abstand_y)

        self.en3_3_text=StringVar()
        self.en3_3_text.set(vz)
        self.en3_3=Entry(rahmen1, width=round(groesse / 3), textvariable=self.en3_3_text)
        self.en3_3.grid(row=2, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la4_text=StringVar()
        self.la4_text.set("Position (x;y;z):")
        self.la4=Label(rahmen1, textvariable=self.la4_text, width=groesse, bg=farbe, justify=CENTER)
        self.la4.grid(row=3, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.en4_1_text=StringVar()
        self.en4_1_text.set(x)
        self.en4_1=Entry(rahmen1, width=round(groesse / 3), textvariable=self.en4_1_text)
        self.en4_1.grid(row=3, column=1, sticky=W, padx=abstand_x, pady=abstand_y)

        self.en4_2_text=StringVar()
        self.en4_2_text.set(y)
        self.en4_2=Entry(rahmen1, width=round(groesse / 3), textvariable=self.en4_2_text)
        self.en4_2.grid(row=3, column=1, padx=abstand_x, pady=abstand_y)

        self.en4_3_text=StringVar()
        self.en4_3_text.set(z)
        self.en4_3=Entry(rahmen1, width=round(groesse / 3), textvariable=self.en4_3_text)
        self.en4_3.grid(row=3, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu1=Button(rahmen1, text="Submit", width=groesse + 3, highlightbackground='#3E4149', command=lambda: self.submit(1))
        self.bu1.grid(row=4, column=1, padx=abstand_x, pady=abstand_y)

        self.bu1=Button(rahmen1, text="Clear", width=groesse + 3, highlightbackground='#3E4149', command=self.clear)
        self.bu1.grid(row=4, column=0, padx=abstand_x, pady=abstand_y)

        if self.overview.data_list[self.planet_number - 1] != None:
            data_texture, data_name, data_mass, data_vx, data_vy, data_vz, data_x, data_y, data_z=\
            self.overview.data_list[
                self.planet_number - 1].split("#")

            self.en1_text.set(data_name)
            self.en2_text.set(data_mass)
            self.en3_1_text.set(data_vx)
            self.en3_2_text.set(data_vy)
            self.en3_3_text.set(data_vz)
            self.en4_1_text.set(data_x)
            self.en4_2_text.set(data_y)
            self.en4_3_text.set(data_z)


        elif self.overview.lines[self.planet_number - 1] == str(self.planet_number):
            self.en1_text.set(name)
            self.en2_text.set(mass)
            self.en3_1_text.set(vx)
            self.en3_2_text.set(vy)
            self.en3_3_text.set(vz)
            self.en4_1_text.set(x)
            self.en4_2_text.set(y)
            self.en4_3_text.set(z)

            self.submit()

        elif self.overview.lines[self.planet_number - 1] != str(self.planet_number):
            data_texture, data_name, data_mass, data_vx, data_vy, data_vz, data_x, data_y, data_z=self.overview.lines[self.planet_number - 1].split("#")

            self.en1_text.set(data_name)
            self.en2_text.set(data_mass)
            self.en3_1_text.set(data_vx)
            self.en3_2_text.set(data_vy)
            self.en3_3_text.set(data_vz)
            self.en4_1_text.set(data_x)
            self.en4_2_text.set(data_y)
            self.en4_3_text.set(data_z)

            self.submit()

        self.planet_list=[]

    def clear(self):
        # clears all entries of the GUI_add_Planet-window
        self.en1_text.set("")
        self.en2_text.set("")
        self.en3_1_text.set("")
        self.en3_2_text.set("")
        self.en3_3_text.set("")
        self.en4_1_text.set("")
        self.en4_2_text.set("")
        self.en4_3_text.set("")
        self.submit()

    def submit(self, button=0):
        # reads entries, stores the data and creates a planet object
        if self.planet_number != 0:
            name=self.en1_text.get()
            mass=self.en2_text.get()
            vx=self.en3_1_text.get()
            vy=self.en3_2_text.get()
            vz=self.en3_3_text.get()
            x=self.en4_1_text.get()
            y=self.en4_2_text.get()
            z=self.en4_3_text.get()
            try:
                # if all entries exept for the name are convertible to int, this code gets executed
                mass=int(mass)
                vx=int(vx)
                vy=int(vy)
                vz=int(vz)
                x=int(x)
                y=int(y)
                z=int(z)

                fn="textures/planet_" + str(self.planet_number - 1) + ".jpg"

                self.overview.data_list[self.planet_number - 1]=str(fn) + "#" + str(name) + "#" + str(
                    mass) + "#" + str(vx) + "#" + str(vy) + "#" + str(vz) + "#" + str(x) + "#" + str(y) + "#" + str(z)

                self.planet=Planet(file_name=fn, planet_name=name, plannr=self.planet_number, planet_mass=mass,
                                     vel_x=vx, vel_y=vy, vel_z=vz, coord_x=x, coord_y=y, coord_z=z)

                self.overview.planetlist[self.planet_number - 1]=self.planet
                self.overview.planetlist_all[self.planet_number - 1]=self.planet
                if button == 1:
                    self.root.destroy()
            except:
                # if one of the variables mentioned above isn'n convertible, an error-window pops up and notifies the user
                ctypes.windll.user32.MessageBoxW(None, u"One of your Inputs had unknown charakters in it. \nPlease only use Numbers for mass, velocity, and position", u"ERROR", 0)





class GUI_Planet_Overview(Tk):
    # overview of all added planets and if they will appear in the simulation
    lock=0
    def __init__(self, mm, planetlist=[]):
        root2=Toplevel()
        # self.app=ursina.Ursina()
        self.mm=mm # Main-menu
        f=open("planet_data.txt", "r")


        root2.title("Customize Planets")
        root2.geometry("945x785")
        root2.resizable(False, False)

        rahmen1=Frame(root2, relief=SUNKEN, borderwidth=7)
        rahmen1.pack()

        root2.columnconfigure(0, weight=1)
        root2.columnconfigure(1, weight=2)

        farbe="light grey"

        abstand_x=3
        abstand_y=3

        groesse=20

        while len(planetlist) < 10:
            planetlist.append(None)
        self.data_list=[]

        while len(self.data_list) < 10:
            self.data_list.append(None)
        temp=planetlist[:]

        self.planetlist=temp[:]
        self.planetlist_all=temp[:]

        f=open("planet_data.txt", "r")
        self.lines=[line.rstrip('\n') for line in f]
        for i in range(len(self.lines) - 1):
            if str(i + 1) == self.lines[i]:
                pass
            else:
                data_texture, data_name, data_mass, data_vx, data_vy, data_vz, data_x, data_y, data_z=self.lines[i].split("#")

                self.planet=Planet(file_name=data_texture, planet_name=data_name, plannr=i, planet_mass=data_mass,
                                    vel_x=data_vx, vel_y=data_vy, vel_z=data_vz, coord_x=data_x, coord_y=data_y, coord_z=data_z)

                self.planetlist[i - 1]=self.planet
                self.planetlist_all[i - 1]=self.planet

        f.close()

        if GUI_Planet_Overview.lock == 0:

            self.col_positive='light green'
            self.col_negative='indian red'

            self.state_plan1=self.col_positive
            self.state_plan2=self.col_negative
            self.state_plan3=self.col_negative
            self.state_plan4=self.col_negative
            self.state_plan5=self.col_negative
            self.state_plan6=self.col_negative
            self.state_plan7=self.col_negative
            self.state_plan8=self.col_negative
            self.state_plan9=self.col_negative
            self.state_plan10=self.col_negative

            self.txt_positive='Active'
            self.txt_negative='Inactive'

            self.text_plan1=self.txt_positive
            self.text_plan2=self.txt_negative
            self.text_plan3=self.txt_negative
            self.text_plan4=self.txt_negative
            self.text_plan5=self.txt_negative
            self.text_plan6=self.txt_negative
            self.text_plan7=self.txt_negative
            self.text_plan8=self.txt_negative
            self.text_plan9=self.txt_negative
            self.text_plan10=self.txt_negative

            GUI_Planet_Overview.lock=1

        self.la1_text=StringVar()
        self.la1_text.set("Read Help for Usage")
        self.la1=Label(rahmen1, textvariable=self.la1_text, bg=farbe,  width=groesse, justify=CENTER, )
        self.la1.grid(row=1, column=0, sticky=E, padx=abstand_x, pady=abstand_y)


        self.la11_text=StringVar()
        self.la11_text.set("-----------------------------")
        self.la11=Label(rahmen1, textvariable=self.la11_text, width=groesse, justify=CENTER)
        self.la11.grid(row=2, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la12_text=StringVar()
        self.la12_text.set("-----------------------------")
        self.la12=Label(rahmen1, textvariable=self.la12_text, width=groesse, justify=CENTER)
        self.la12.grid(row=2, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la13_text=StringVar()
        self.la13_text.set("-----------------------------")
        self.la13=Label(rahmen1, textvariable=self.la13_text, width=groesse, justify=CENTER)
        self.la13.grid(row=2, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la14_text=StringVar()
        self.la14_text.set("-----------------------------")
        self.la14=Label(rahmen1, textvariable=self.la14_text, width=groesse, justify=CENTER)
        self.la14.grid(row=2, column=3, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la15_text=StringVar()
        self.la15_text.set("-----------------------------")
        self.la15=Label(rahmen1, textvariable=self.la15_text, width=groesse, justify=CENTER)
        self.la15.grid(row=2, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la16_text=StringVar()
        self.la16_text.set("Planet Overview")
        self.la16=Label(rahmen1, textvariable=self.la16_text, bg="light grey", width=groesse, justify=CENTER)
        self.la16.grid(row=1, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la17_text=StringVar()
        self.la17_text.set("-")
        self.la17=Label(rahmen1, textvariable=self.la17_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la17.grid(row=0, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la18_text=StringVar()
        self.la18_text.set("-")
        self.la18=Label(rahmen1, textvariable=self.la18_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la18.grid(row=3, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la19_text=StringVar()
        self.la19_text.set("-")
        self.la19=Label(rahmen1, textvariable=self.la19_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la19.grid(row=4, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la20_text=StringVar()
        self.la20_text.set("-")
        self.la20=Label(rahmen1, textvariable=self.la20_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la20.grid(row=5, column=2, sticky=E, padx=abstand_x, pady=abstand_y)


        self.bu21=Button(rahmen1, text=self.text_plan1, width=groesse, highlightbackground=self.state_plan1, justify=CENTER, command=self.activ_plan1)
        self.bu21.grid(row=4, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la22_text=StringVar()
        self.la22_text.set("-")
        self.la22=Label(rahmen1, textvariable=self.la22_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la22.grid(row=6, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la23_text=StringVar()
        self.la23_text.set("-")
        self.la23=Label(rahmen1, textvariable=self.la23_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la23.grid(row=7, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la24_text=StringVar()
        self.la24_text.set("-")
        self.la24=Label(rahmen1, textvariable=self.la24_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la24.grid(row=8, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu22=Button(rahmen1, text=self.text_plan3, width=groesse, highlightbackground=self.state_plan3, justify=CENTER, command=self.activ_plan3)
        self.bu22.grid(row=8, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu23=Button(rahmen1, text=self.text_plan5, width=groesse, highlightbackground=self.state_plan5, justify=CENTER,
                           command=self.activ_plan5)
        self.bu23.grid(row=12, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu24=Button(rahmen1, text=self.text_plan7, width=groesse, highlightbackground=self.state_plan7, justify=CENTER,
                           command=self.activ_plan7)
        self.bu24.grid(row=16, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la28_text=StringVar()
        self.la28_text.set("-")
        self.la28=Label(rahmen1, textvariable=self.la28_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la28.grid(row=9, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la29_text=StringVar()
        self.la29_text.set("-")
        self.la29=Label(rahmen1, textvariable=self.la29_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la29.grid(row=10, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la30_text=StringVar()
        self.la30_text.set("-")
        self.la30=Label(rahmen1, textvariable=self.la30_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la30.grid(row=11, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la31_text=StringVar()
        self.la31_text.set("-")
        self.la31=Label(rahmen1, textvariable=self.la31_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la31.grid(row=12, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la32_text=StringVar()
        self.la32_text.set("-")
        self.la32=Label(rahmen1, textvariable=self.la32_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la32.grid(row=13, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la33_text=StringVar()
        self.la33_text.set("-")
        self.la33=Label(rahmen1, textvariable=self.la33_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la33.grid(row=14, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la34_text=StringVar()
        self.la34_text.set("-")
        self.la34=Label(rahmen1, textvariable=self.la34_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la34.grid(row=15, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la35_text=StringVar()
        self.la35_text.set("-")
        self.la35=Label(rahmen1, textvariable=self.la35_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la35.grid(row=16, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la36_text=StringVar()
        self.la36_text.set("-")
        self.la36=Label(rahmen1, textvariable=self.la36_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la36.grid(row=17, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la37_text=StringVar()
        self.la37_text.set("-")
        self.la37=Label(rahmen1, textvariable=self.la37_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la37.grid(row=18, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la38_text=StringVar()
        self.la38_text.set("-")
        self.la38=Label(rahmen1, textvariable=self.la38_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la38.grid(row=19, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu1=Button(rahmen1, text="Save Changes", width=groesse, highlightbackground='#3E4149', command=self.return_to_gui)
        self.bu1.grid(row=24, column=4, padx=abstand_x, pady=abstand_y)

        self.bu2=Button(rahmen1, text="Help", width=groesse, highlightbackground='#3E4149', command=self.help)
        self.bu2.grid(row=24, column=0, padx=abstand_x, pady=abstand_y)

        self.bu25=Button(rahmen1, text=self.text_plan2, width=groesse, highlightbackground=self.state_plan2, justify=CENTER,
                           command=self.activ_plan2)
        self.bu25.grid(row=4, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu26=Button(rahmen1, text=self.text_plan4, width=groesse, highlightbackground=self.state_plan4, justify=CENTER,
                           command=self.activ_plan4)
        self.bu26.grid(row=8, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu27=Button(rahmen1, text=self.text_plan6, width=groesse, highlightbackground=self.state_plan6, justify=CENTER,
                           command=self.activ_plan6)
        self.bu27.grid(row=12, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu28=Button(rahmen1, text=self.text_plan8, width=groesse, highlightbackground=self.state_plan8, justify=CENTER,
                           command=self.activ_plan8)
        self.bu28.grid(row=16, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu29=Button(rahmen1, text=self.text_plan9, width=groesse, highlightbackground=self.state_plan9, justify=CENTER,
                           command=self.activ_plan9)
        self.bu29.grid(row=20, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu30=Button(rahmen1, text=self.text_plan10, width=groesse, highlightbackground=self.state_plan10, justify=CENTER,
                           command=self.activ_plan10)
        self.bu30.grid(row=20, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la45_text=StringVar()
        self.la45_text.set("-")
        self.la45=Label(rahmen1, textvariable=self.la45_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la45.grid(row=21, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la46_text=StringVar()
        self.la46_text.set("-")
        self.la46=Label(rahmen1, textvariable=self.la46_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la46.grid(row=22, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la47_text=StringVar()
        self.la47_text.set("-")
        self.la47=Label(rahmen1, textvariable=self.la47_text, width=groesse, fg='#F0F0F0', justify=CENTER)
        self.la47.grid(row=23, column=2, sticky=E, padx=abstand_x, pady=abstand_y)

        # IMAGES -------------------------------------------------------------------------------------------------------
        load1=Image.open("textures/rendered_sun_scaled.png")
        render=ImageTk.PhotoImage(load1)

        img1=Label(root2, image=render)
        img1.image=render
        img1.place(x=30, y=90)

        load2=Image.open("textures/rendered_planet_1_scaled.png")
        render=ImageTk.PhotoImage(load2)

        img2=Label(root2, image=render)
        img2.image=render
        img2.place(x=490, y=90)

        load3=Image.open("textures/rendered_planet_2_scaled.png")
        render=ImageTk.PhotoImage(load3)

        img3=Label(root2, image=render)
        img3.image=render
        img3.place(x=30, y=205)

        load4=Image.open("textures/rendered_planet_3_scaled.png")
        render=ImageTk.PhotoImage(load4)

        img4=Label(root2, image=render)
        img4.image=render
        img4.place(x=490, y=205)

        load5=Image.open("textures/rendered_planet_4_scaled.png")
        render=ImageTk.PhotoImage(load5)

        img5=Label(root2, image=render)
        img5.image=render
        img5.place(x=30, y=320)

        load6=Image.open("textures/rendered_planet_5_scaled.png")
        render=ImageTk.PhotoImage(load6)

        img6=Label(root2, image=render)
        img6.image=render
        img6.place(x=490, y=320)

        load7=Image.open("textures/rendered_planet_6_scaled.png")
        render=ImageTk.PhotoImage(load7)

        img7=Label(root2, image=render)
        img7.image=render
        img7.place(x=30, y=435)

        load8=Image.open("textures/rendered_planet_7_scaled.png")
        render=ImageTk.PhotoImage(load8)

        img8=Label(root2, image=render)
        img8.image=render
        img8.place(x=490, y=435)

        load9=Image.open("textures/rendered_planet_8_scaled.png")
        render=ImageTk.PhotoImage(load9)

        img9=Label(root2, image=render)
        img9.image=render
        img9.place(x=30, y=550)

        load10=Image.open("textures/rendered_planet_9_scaled.png")
        render=ImageTk.PhotoImage(load10)

        img10=Label(root2, image=render)
        img10.image=render
        img10.place(x=490, y=550)

        # BUTTONS ------------------------------------------------------------------------------------------------------
        bu_1=Button(rahmen1, text="Edit planet", width=groesse, highlightbackground='#3E4149',
                      command=lambda: self.plan(self.planetlist[0], 1))
        bu_1.grid(row=5, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_3=Button(rahmen1, text="Edit planet", image="", width=groesse, highlightbackground='#3E4149',
                      command=lambda: self.plan(self.planetlist[2], 3))
        bu_3.grid(row=9, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_5=Button(rahmen1, text="Edit planet", image="", width=groesse, highlightbackground='#3E4149',
                      command=lambda: self.plan(self.planetlist[4], 5))
        bu_5.grid(row=13, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_7=Button(rahmen1, text="Edit planet", image="", width=groesse, highlightbackground='#3E4149',
                      command=lambda: self.plan(self.planetlist[6], 7))
        bu_7.grid(row=17, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_2=Button(rahmen1, text="Edit planet", image="", width=groesse, highlightbackground='#3E4149',
                      command=lambda: self.plan(self.planetlist[1], 2))
        bu_2.grid(row=5, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_4=Button(rahmen1, text="Edit planet", image="", width=groesse, highlightbackground='#3E4149',
                      command=lambda: self.plan(self.planetlist[3], 4))
        bu_4.grid(row=9, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_6=Button(rahmen1, text="Edit planet", image="", width=groesse, highlightbackground='#3E4149',
                      command=lambda: self.plan(self.planetlist[5], 6))
        bu_6.grid(row=13, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_8=Button(rahmen1, text="Edit planet", image="", width=groesse, highlightbackground='#3E4149',
                      command=lambda: self.plan(self.planetlist[7], 8))
        bu_8.grid(row=17, column=4, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_9=Button(rahmen1, text="Edit planet", image="", width=groesse, highlightbackground='#3E4149',
                      command=lambda: self.plan(self.planetlist[8], 9))
        bu_9.grid(row=21, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        bu_10=Button(rahmen1, text="Edit planet", image="", width=groesse, highlightbackground='#3E4149',
                       command=lambda: self.plan(self.planetlist[9], 10))
        bu_10.grid(row=21, column=4, sticky=E, padx=abstand_x, pady=abstand_y)



    def activ_plan1(self):
        # the sun is always active
        pass

    def activ_plan2(self):
        # toggles activation of planet 2
        if self.text_plan2 == self.txt_positive:
            self.bu25.config(text=self.txt_negative, highlightbackground=self.col_negative)
            self.text_plan2=self.txt_negative
            self.planetlist[1]=None
        else:

            self.bu25.config(text=self.txt_positive, highlightbackground=self.col_positive)
            self.text_plan2=self.txt_positive
            self.planetlist[1]=self.planetlist_all[1]

    def activ_plan3(self):
        # toggles activation of planet 3
        if self.text_plan3 == self.txt_positive:
            self.bu22.config(text=self.txt_negative, highlightbackground=self.col_negative)
            self.text_plan3=self.txt_negative
            self.planetlist[2]=None
        else:
            self.bu22.config(text=self.txt_positive, highlightbackground=self.col_positive)
            self.text_plan3=self.txt_positive
            self.planetlist[2]=self.planetlist_all[2]

    def activ_plan4(self):
        # toggles activation of planet 4
        if self.text_plan4 == self.txt_positive:
            self.bu26.config(text=self.txt_negative, highlightbackground=self.col_negative)
            self.text_plan4=self.txt_negative
            self.planetlist[3]=None
        else:
            self.bu26.config(text=self.txt_positive, highlightbackground=self.col_positive)
            self.text_plan4=self.txt_positive
            self.planetlist[3]=self.planetlist_all[3]

    def activ_plan5(self):
        # toggles activation of planet 5
        if self.text_plan5 == self.txt_positive:
            self.bu23.config(text=self.txt_negative, highlightbackground=self.col_negative)
            self.text_plan5=self.txt_negative
            self.planetlist[4]=None
        else:
            self.bu23.config(text=self.txt_positive, highlightbackground=self.col_positive)
            self.text_plan5=self.txt_positive
            self.planetlist[4]=self.planetlist_all[4]

    def activ_plan6(self):
        # toggles activation of planet 6
        if self.text_plan6 == self.txt_positive:
            self.bu27.config(text=self.txt_negative, highlightbackground=self.col_negative)
            self.text_plan6=self.txt_negative
            self.planetlist[5]=None
        else:
            self.bu27.config(text=self.txt_positive, highlightbackground=self.col_positive)
            self.text_plan6=self.txt_positive
            self.planetlist[5]=self.planetlist_all[5]

    def activ_plan7(self):
        # toggles activation of planet 7
        if self.text_plan7 == self.txt_positive:
            self.bu24.config(text=self.txt_negative, highlightbackground=self.col_negative)
            self.text_plan7=self.txt_negative
            self.planetlist[6]=None
        else:
            self.bu24.config(text=self.txt_positive, highlightbackground=self.col_positive)
            self.text_plan7=self.txt_positive
            self.planetlist[6]=self.planetlist_all[6]

    def activ_plan8(self):
        # toggles activation of planet 8
        if self.text_plan8 == self.txt_positive:
            self.bu28.config(text=self.txt_negative, highlightbackground=self.col_negative)
            self.text_plan8=self.txt_negative
            self.planetlist[7]=None
        else:
            self.bu28.config(text=self.txt_positive, highlightbackground=self.col_positive)
            self.text_plan8=self.txt_positive
            self.planetlist[7]=self.planetlist_all[7]

    def activ_plan9(self):
        # toggles activation of planet 9
        if self.text_plan9 == self.txt_positive:
            self.bu29.config(text=self.txt_negative, highlightbackground=self.col_negative)
            self.text_plan9=self.txt_negative
            self.planetlist[8]=None
        else:
            self.bu29.config(text=self.txt_positive, highlightbackground=self.col_positive)
            self.text_plan9=self.txt_positive
            self.planetlist[8]=self.planetlist_all[8]

    def activ_plan10(self):
        # toggles activation of planet 10
        if self.text_plan10 == self.txt_positive:
            self.bu30.config(text=self.txt_negative, highlightbackground=self.col_negative)
            self.text_plan10=self.txt_negative
            self.planetlist[9]=None
        else:
            self.bu30.config(text=self.txt_positive, highlightbackground=self.col_positive)
            self.text_plan10=self.txt_positive
            self.planetlist[9]=self.planetlist_all[9]

    def return_to_gui(self):
        # stores planet data in a file
        self.mm.planet_list=self.planetlist[:]

        f=open('planet_data.txt', 'w').close()
        f=open("planet_data.txt", "a")

        for i in range(len(self.data_list)):
            if self.data_list[i] == None:
                f.write(str(i+1)+"\n")
            else:
                f.write(self.data_list[i]+"\n")
        self.mm.root.lift()


        f.close()

    def help(self):
        # opens the help file
        os.system('start " " help.txt')

    def plan(self, planet, plannr):
        # opens a GUI_add_Planet-window for the selected planet in the overview
        if planet == None:
            gui_add=GUI_add_Planet(plannr, overview=self)
        else:
            gui_add=GUI_add_Planet(name=planet.planet_name, mass=planet.planet_mass,
                                     x=planet.coord_x, y=planet.coord_y, z=planet.coord_z,
                                     vx=planet.vel_x, vy=planet.vel_y, vz=planet.vel_z, planet_number=plannr, overview=self)


if __name__ == '__main__':
    # initiates the GUI_Startup class and therefore starts the whole program
    gui=GUI_Startup()
    mainloop()
