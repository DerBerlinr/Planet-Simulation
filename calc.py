import numpy as np
from ursina import *
from planet import Planet

class Calc:
    def __init__(self, planet):
        # G -> gravitational force; mS -> Mass of Sun
        self.G = np.array([-6.67430 * 10 ** -11, -6.67430 * 10 ** -11, -6.67430 * 10 ** -11])
        self.mS = np.array([1.9885 * 10 ** 30, 1.9885 * 10 ** 30, 1.9885 * 10 ** 30])
        posx, posy, posz = planet.get_coords()
        self.pos = [int(posx), int(posy), int(posz)]
        velx, vely, velz = planet.get_vel()
        self.vel = [int(velx), int(vely), int(velz)]
        print(self.pos)
        self.dt = 60
        self.a = None
        self.counter = 0
        self.v = None
        self.vel_o = 0

    def acc(self):
        vec = self.mul_scalar(self.pos, 1)
        vec_power_2 = self.pos[0] ** 2 + self.pos[1] ** 2 + self.pos[2] ** 2
        # G -> Gravitationskonstante
        # mS -> Masse der Sonne
        scalar = -self.G * self.mS / vec_power_2
        return self.div_scalar(vec, self.vec_len(vec) * scalar[0])

    def mul_scalar(self, vec, scalar):
        # multiplies a vector by a scalar
        return [vec[0]*scalar, vec[1]*scalar, vec[2]*scalar]

    def div_scalar(self, vec, scalar):
        # divides a vector by a scalar
        return [vec[0]/scalar, vec[1]/scalar, vec[2]/scalar]

    def vec_len(self, vec):
        # calculates the length of a vector
        return math.sqrt(vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2)

    def add_vec(self, v1, v2):
        # adds two vectors
        return [v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2]]


    def get_coords(self, planet):
        # This function gets called as a thread
        t = 0
        counter = 0
        while True:
            self.a = self.acc()
            if t == 0:
                self.vel = self.add_vec(self.vel, self.mul_scalar(self.a, self.dt / 2))
            else:
                self.vel = self.add_vec(self.vel, self.mul_scalar(self.a, self.dt))
            self.pos = self.add_vec(self.pos, self.mul_scalar(self.vel, self.dt))

            planet.set_coords(self.pos[0], self.pos[1], self.pos[2], self.vel[0], self.vel[1], self.vel[2])
            #if planet.plannr == 2:
                #print(self.pos[0], self.pos[1], self.pos[2], "Jahr: ", counter, "Planet: ", planet.planet_name)

            if not t % 31536000:
                # print(self.pos[0], self.pos[1], self.pos[2], "Jahr: ", counter, "Planet: ", planet.planet_name)
                counter += 1
            if held_keys['shift'] and held_keys['q']:
                exit()
            t += self.dt
            
if __name__ == '__main__':
    p = Planet(file_name='/textures/planet_2', planet_name='planet2', planet_diameter=1, plannr=2,
                         vel_x=10308.531985820431, vel_y=-27640.154010970804, vel_z=-0.7364511260199437,
                         coord_x=140699825958.8049, coord_y=-54738590238.00282, coord_z=-2510791.537005455)
    c = Calc(p)
    c.get_coords(p)
