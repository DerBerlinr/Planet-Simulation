import numpy as np
from ursina import *
import threading


class Calc:
    def __init__(self, posx=500000, posy=1000000000, posz=75000000, velx=-500, vely=1000, velz=-300):
        # G -> gravitational force; mS -> Mass of Sun
        self.G = np.array([-6.67430 * 10 ** -11, -6.67430 * 10 ** -11, -6.67430 * 10 ** -11])
        self.mS = np.array([1.9885 * 10 ** 30, 1.9885 * 10 ** 30, 1.9885 * 10 ** 30])
        self.pos = np.array([posx, posy, posz])
        #print("posx", posx)
        self.vel = np.array([velx, vely, velz])
        self.dt = 60
        self.a = None
        self.counter = 0
        self.v = None
        self.vel_o = 0

    def acc(self):
        vec = self.pos * -1
        vecc = self.pos[0] ** 2 + self.pos[1] ** 2 + self.pos[2] ** 2
        #print("vecc", vecc)
        #print("self.pos", self.pos[0])
        # G -> Gravitationskonstante
        # mS -> Masse der Sonne
        scalar = -self.G * self.mS / vecc
        return vec / np.linalg.norm(vec) * scalar

    def get_coords(self, planet):
        # This function gets called as a thread
        t = 0
        c = 0
        while True:
            self.a = self.acc()
            if t == 0:
                self.vel = self.vel + self.a * self.dt / 2
                #print("v:", self.vel)
            else:
                self.vel = self.vel + self.a * self.dt
            self.pos = self.pos + self.vel * self.dt

            planet.set_coords(self.pos[0], self.pos[1], self.pos[2])
            if not t % 31536000:
                print(t)
                print(self.pos[0], self.pos[1], self.pos[2], "Jahr: ", c, "Planet: ", planet.planet_name)
                c += 1
            if held_keys['shift'] and held_keys['q']:
                exit()
            t += self.dt
