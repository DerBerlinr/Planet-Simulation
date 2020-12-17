from calc import Calc
import numpy as np

c = Calc(pos=np.array([140699825958.8049, -54738590238.00282, 2510791.537005455]), vel=np.array([10308.531985820431, 27640.154010970804, -0.7364511260199437]))
a = 0
x = 0
for i in range(0, 31536000, 60):
    c.a = c.acc()
    if c.counter == 0:
        c.vel = c.vel + c.a * c.dt / 2
    else:
        c.v = c.vel_new(i)
    x = c.pos_new()
print(x[0], x[1], x[2])
