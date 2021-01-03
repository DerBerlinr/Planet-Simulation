import numpy as np
from ursina import *
from planet import Planet

class Calc:
    # Calculates positions for one planet
    def __init__(self, planet):
        # g -> gravitational force; m_s -> Mass of Sun
        self.g = np.array([-6.67430 * 10 ** -11, -6.67430 * 10 ** -11, -6.67430 * 10 ** -11])
        self.m_s = np.array([1.9885 * 10 ** 30, 1.9885 * 10 ** 30, 1.9885 * 10 ** 30])

        posx, posy, posz = planet.get_coords()
        self.pos = [int(posx), int(posy), int(posz)]
        velx, vely, velz = planet.get_vel()
        self.vel = [int(velx), int(vely), int(velz)]

        self.dt = 60
        self.acceleration = None
        self.counter = 0
        self.velocity = None
        self.vel_old = 0

    def acc(self):
        # calculates the acceleration-vector
        vec = self.mul_scalar(self.pos, -1)
        vec_power_2 = self.len_power_2(vec)
        scalar = -1 * self.g * self.m_s / vec_power_2
        return self.mul_scalar(self.vec_norm(vec), scalar[0])

    def get_coords(self, planet):
        # This function gets called as a thread
        # Appends new positions to planet.poslist
        time = 0
        while True:
            self.acceleration = self.acc()
            if time == 0:
                self.vel = self.add_vec(self.vel, self.mul_scalar(self.acceleration, self.dt / 2))
            else:
                self.vel = self.add_vec(self.vel, self.mul_scalar(self.acceleration, self.dt))
            self.pos = self.add_vec(self.pos, self.mul_scalar(self.vel, self.dt))

            planet.set_coords(self.pos[0], self.pos[1], self.pos[2], self.vel[0], self.vel[1], self.vel[2])

            if held_keys['shift'] and held_keys['q']:
                exit()
            time += self.dt

    def mul_scalar(self, vec, scalar):
        # multiplies a vector by a scalar
        return [vec[0] * scalar, vec[1] * scalar, vec[2] * scalar]

    def div_scalar(self, vec, scalar):
        # divides a vector by a scalar
        return [vec[0] / scalar, vec[1] / scalar, vec[2] / scalar]

    def vec_len(self, vec):
        # calculates the length of a vector
        return math.sqrt(self.len_power_2(vec))

    def add_vec(self, v1, v2):
        # adds two vectors
        return [v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]]

    def sub_vec(self, v1, v2):
        # subtracts two vectors
        return [v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]]

    def vec_dot(self, v1, v2):
        # calculates the dot product of two vectors
        return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

    def len_power_2(self, vec):
        # retuns the dot product of one vector with himself
        return self.vec_dot(vec, vec)

    def vec_norm(self, vec):
        # returns the normalized vector
        return self.div_scalar(vec, self.vec_len(vec))
