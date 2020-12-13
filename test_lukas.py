from calc import Calc
import numpy as np
c = Calc(pos=np.array([140699825958.8049, -54738590238.00282, 2510791.537005455]), vel=np.array([10308.531985820431, 27640.154010970804, -0.7364511260199437]))
a = 0
for i in range(0, 31536000, 60):
    a = c.get_coords(i)
print(a)
