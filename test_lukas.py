from calc import Calc
import numpy as np

c = Calc(posx=140699825958.8049, posy=-54738590238.00282, posz=2510791.537005455, velx=10308.531985820431, vely=27640.154010970804, velz=-0.7364511260199437)
a = 0
x = 0
for i in range(0, 31536000, 600):
    c.a = c.acc()
    if c.counter == 0:
        c.vel = c.vel + c.a * c.dt / 2
    else:
        c.v = c.vel_new(i)
    x = c.pos_new()
print(x[0], x[1], x[2])
