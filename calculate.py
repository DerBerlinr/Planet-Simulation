import math

listx = []
listy = []
listz = []
listvx = []
listvy = []
listvz = []
listax = []
listay = []
listaz = []



x0 = 500000
vx0 = -500


y0 = 1000000000
vy0 = 1000


z0 = 75000000
vz0 = -300


G = 6.675*10**-11
mS = 1.989*10**30
mE = 5.972*10**24

t = 0
dt = 60
v=0

sqrt_xyz = math.sqrt(x0 ** 2 + y0 ** 2 + z0 ** 2)

listx.append(x0)
listy.append(y0)
listz.append(z0)
listvx.append(vx0)
listvy.append(vy0)
listvz.append(vz0)



def ax_t(t):
    ax = -G*mS*(x_t(t))/(sqrt_xyz)**3
    listax.append(ax)
    return ax
def x_t(t):
    x = listx[list_counter]
    return x
def vx_t(t):
    vx = listvx[list_counter] + listax[list_counter]*dt/2
    listvx.append(vx)
    return vx


def ay_t(t):
    ay = -G*mS*(y_t(t))/(sqrt_xyz)**3
    listay.append(ay)
    return ay
def y_t(t):
    y = listy[list_counter]
    return y
def vy_t(t):
    vy = listvy[list_counter] + listay[list_counter]*dt/2
    listvy.append(vy)
    return vy


def az_t(t):
    az = -G*mS*(z_t(t))/(sqrt_xyz)**3
    listaz.append(az)
    return az
def z_t(t):
    z = listz[list_counter]
    return z
def vz_t(t):
    vz = listvz[list_counter] + listaz[list_counter]*dt/2
    listvz.append(vz)
    return vz


while t != 6000:

    list_counter = int(t/60)

    ax = ax_t(t)
    if len(listvx) == 1:
        vx = vx0 + ax_t(t)*dt/2
    else:
        vx = vx_t(t+dt/2) + ax_t(t)*dt
    x = x_t(t) + vx_t(t+dt/2)*dt
    listx.append(x)


    ay = ay_t(t)
    if len(listvy) == 1:
        vy = vy0 + ay_t(t) * dt / 2
    else:
        vy = vy_t(t + dt / 2) + ay_t(t)*dt
    y = y_t(t) + vy_t(t + dt / 2) * dt
    listy.append(y)


    az = az_t(t)
    if len(listvz) == 1:
        vz = vz0 + az_t(t) * dt / 2
    else:
        vz = vz_t(t + dt / 2) + az_t(t)*dt
    print("vz,z_t,vz_t")
    print(vz)
    print(z_t(t))
    print(vz_t(t))
    z = z_t(t) + vz_t(t + dt / 2) * dt
    listz.append(z)

    sqrt_xyz = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    t = t + 60

print("Werte x:")
for i in listx:
    print(i)
print("Werte y:")
for i in listy:
    print(i)
print("Werte z:")
for i in listz:
    print(i)





