import numpy as np
from ursina import *
from planet import Planet

class Calc:
    def __init__(self, planet):
        # G -> gravitational force; mS -> Mass of Sun
        self.G = np.array([-6.67430 * 10 ** -11, -6.67430 * 10 ** -11, -6.67430 * 10 ** -11])
        self.mS = np.array([1.9885 * 10 ** 30, 1.9885 * 10 ** 30, 1.9885 * 10 ** 30])
        posx, posy, posz = planet.get_coords()
        self.pos = np.array([posx, posy, posz])
        velx, vely, velz = planet.get_vel()
        self.vel = np.array([velx, vely, velz])
        print(self.pos)
        self.dt = 60
        self.a = None
        self.counter = 0
        self.v = None
        self.vel_o = 0

    def acc(self):
        vec = self.pos * -1
        vec_power_2 = self.pos[0] ** 2 + self.pos[1] ** 2 + self.pos[2] ** 2
        # G -> Gravitationskonstante
        # mS -> Masse der Sonne
        scalar = -self.G * self.mS / vec_power_2
        return vec / np.linalg.norm(vec) * scalar

    def get_coords(self, planet):
        # This function gets called as a thread
        t = 0
        counter = 0
        while True:
            self.a = self.acc()
            if t == 0:
                self.vel = self.vel + self.a * self.dt / 2
            else:
                self.vel = self.vel + self.a * self.dt
            self.pos = self.pos + self.vel * self.dt

            planet.set_coords(self.pos[0], self.pos[1], self.pos[2], self.vel[0], self.vel[1], self.vel[2])

            if not t % 31536000:
                #print(self.pos[0], self.pos[1], self.pos[2], "Jahr: ", counter, "Planet: ", planet.planet_name)
                counter += 1
            if held_keys['shift'] and held_keys['q']:
                exit()
            t += self.dt
            
if __name__ == '__main__':
    p = Planet(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    c = Calc(p)
    c.get_coords(p)
