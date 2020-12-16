from calc import Calc
import numpy as np
import pygame

pygame.init()
pygame.display.set_mode((640, 480))
s = pygame.Surface((500,500))
c = Calc(pos=np.array([140699825958.8049, -54738590238.00282, 2510791.537005455]), vel=np.array([10308.531985820431, 27640.154010970804, -0.7364511260199437]))
a = 0
for i in range(0, 31536000, 60):
    a = c.get_coords(i)
    pygame.draw.circle(surface=s, center=(a[0], a[1]), color='blue', radius=1)
print(a)
