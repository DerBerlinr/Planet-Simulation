import math
import numpy as np
from threading import Thread
from neu.main import *

class Calc():
    def __init__(self, pos=np.array([500000, 1000000000, 75000000]), vel=np.array([-500, 1000, -300])):
        self.G = np.array([-6.67430*10**-11, -6.67430*10**-11, -6.67430*10**-11])
        self.mS = np.array([1.9885*10**30, 1.9885*10**30, 1.9885*10**30])
        self.pos = pos
        self.vel = vel
        self.dt = 1200
        self.a = None
        self.counter = 0
        self.v = None

    def mul_vec(self, vec1, vec2):
        # a simple function for multiplying vectors
        x = vec1[0] * vec2[0]
        y = vec1[1] * vec2[1]
        z = vec1[2] * vec2[2]
        return np.array([x, y, z])

    def acc(self, t):
        # calculation of the acceleration
        a = self.mul_vec(self.mul_vec(self.G, self.mS), self.pos) * 1/(np.linalg.norm(self.pos))**3
        return a

    def vel_new(self, t):
        v = self.vel_old(t) + self.a * self.dt
        return v

    def vel_old(self, t):
        self.vel_old = self.vel

    def pos_new(self, t):
        x = self.pos + self.vel * self.dt * 20
        return x

    def get_coords(self, planet):
        t = 0
        while True:
            self.a = self.acc(t)
            if self.counter == 0:
                self.vel = self.vel + self.a * self.dt/2
            else:
                self.v = self.vel_new(t)
            x = self.pos_new(t)

            planet.set_coords(x[0], x[1], x[2])
            if not t % 180000:
                print(x[0], x[1], x[2])
            t += 60
