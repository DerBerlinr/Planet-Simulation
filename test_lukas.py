from calc import Calc
import numpy as np
import math

c = Calc(posx=140699825958.8049, posy=-54738590238.00282, posz=2510791.537005455,
         velx=10308.531985820431, vely=27640.154010970804, velz=-0.7364511260199437)

def acc():
    vec = c.pos * -1
    vecc = c.pos[0]**2+c.pos[1]**2+c.pos[2]**2
    # G -> Gravitationskonstante
    # mS -> Masse der Sonne
    scalar = -c.G * c.mS / vecc
    return vec / np.linalg.norm(vec) * scalar


for i in range(0, 31536000, 60):
    c.a = acc()
    if i == 0:
        c.vel += c.a * c.dt / 2
        print("v:", c.vel)
    else:
        c.vel += c.a * c.dt
    c.pos += c.vel * c.dt
print(c.pos[0], c.pos[1], c.pos[2])
