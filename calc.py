import numpy as np
from ursina import *


class Calc:
    def __init__(self, posx=500000, posy=1000000000, posz=75000000, velx=-500, vely=1000, velz=-300):
        # G -> gravitational force; mS -> Mass of Sun
        self.G = np.array([-6.67430 * 10 ** -11, -6.67430 * 10 ** -11, -6.67430 * 10 ** -11])
        self.mS = np.array([1.9885 * 10 ** 30, 1.9885 * 10 ** 30, 1.9885 * 10 ** 30])
        self.pos = np.array([posx, posy, posz])
        self.vel = np.array([velx, vely, velz])
        self.dt = 1200
        self.a = None
        self.counter = 0
        self.v = None
        self.vel_old = 0

    @staticmethod
    def mul_vec(vec1, vec2):
        # a simple function for multiplying vectors
        x = vec1[0] * vec2[0]
        y = vec1[1] * vec2[1]
        z = vec1[2] * vec2[2]
        return np.array([x, y, z])

    def acc(self):
        # calculation of the acceleration
        a = self.mul_vec(self.mul_vec(self.G, self.mS), self.pos) * 1 / (np.linalg.norm(self.pos)) ** 3
        return a

    def vel_new(self, t):
        v = self.vel_old(t) + self.a * self.dt
        return v

    def vel_old(self):
        self.vel_old = self.vel

    def pos_new(self):
        x = self.pos + self.vel * self.dt * 20
        return x

    def get_coords(self, planet):
        # This function gets called as a thread
        t = 0
        while True:
            self.a = self.acc()
            if self.counter == 0:
                self.vel = self.vel + self.a * self.dt / 2
            else:
                self.v = self.vel_new(t)
            x = self.pos_new()

            planet.set_coords(x[0], x[1], x[2])
            if not t % 180000:
                pass
                #print(x[0] / 1000000000000, x[1] / 1000000000000, x[2] / 1000000000000)
            if held_keys['shift'] and held_keys['q']:
                exit()
            t += 60
