import math

class Calc:
    def __init__(self, x0=500000, vx0=-500, y0=1000000000, vy0=1000, z0=75000000, vz0=-300):
        self.listx = []
        self.listy = []
        self.listz = []
        self.listvx = []
        self.listvy = []
        self.listvz = []
        self.listax = []
        self.listay = []
        self.listaz = []


        self.x0 = x0
        self.vx0 = vx0

        self.y0 = y0
        self.vy0 = vy0

        self.z0 = z0
        self.vz0 = vz0

        self.G = 6.675*10**-11
        self.mS = 1.989*10**30
        self.mE = 5.972*10**24

        self.dt = 60


        self.sqrt_xyz = math.sqrt(self.x0 ** 2 + self.y0 ** 2 + self.z0 ** 2)

        self.listx.append(self.x0)
        self.listy.append(self.y0)
        self.listz.append(self.z0)
        self.listvx.append(self.vx0)
        self.listvy.append(self.vy0)
        self.listvz.append(self.vz0)



    def ax_t(self, t):
        ax = -self.G*self.mS*(self.x_t(t))/(self.sqrt_xyz)**3
        self.listax.append(ax)
        return ax
    def x_t(self, t):
        x = self.listx[self.list_counter]
        return x
    def vx_t(self, t):
        vx = self.listvx[self.list_counter] + self.listax[self.list_counter]*self.dt/2
        self.listvx.append(vx)
        return vx


    def ay_t(self, t):
        ay = -self.G*self.mS*(self.y_t(t))/(self.sqrt_xyz)**3
        self.listay.append(ay)
        return ay
    def y_t(self, t):
        y = self.listy[self.list_counter]
        return y
    def vy_t(self, t):
        vy = self.listvy[self.list_counter] + self.listay[self.list_counter]*self.dt/2
        self.listvy.append(vy)
        return vy


    def az_t(self, t):
        az = -self.G*self.mS*(self.z_t(t))/(self.sqrt_xyz)**3
        self.listaz.append(az)
        return az
    def z_t(self, t):
        z = self.listz[self.list_counter]
        return z
    def vz_t(self, t):
        vz = self.listvz[self.list_counter] + self.listaz[self.list_counter]*self.dt/2
        self.listvz.append(vz)
        return vz


    def get_coords(self, t):

        self.list_counter = int(t/60)


        self.ax = self.ax_t(t)
        if len(self.listvx) == 1:
            self.vx = self.vx0 + self.ax_t(t)*self.dt/2
        else:
            self.vx = self.vx_t(t+self.dt/2) + self.ax_t(t)*self.dt
        self.x = self.x_t(t) + self.vx_t(t+self.dt/2)*self.dt
        self.listx.append(self.x)


        self.ay = self.ay_t(t)
        if len(self.listvy) == 1:
            self.vy = self.vy0 + self.ay_t(t) * self.dt / 2
        else:
            self.vy = self.vy_t(t + self.dt / 2) + self.ay_t(t)*self.dt
        self.y = self.y_t(t) + self.vy_t(t + self.dt / 2) * self.dt
        self.listy.append(self.y)


        self.az = self.az_t(t)
        if len(self.listvz) == 1:
            self.vz = self.vz0 + self.az_t(t) * self.dt / 2
        else:
            self.vz = self.vz_t(t + self.dt / 2) + self.az_t(t)*self.dt
        self.z = self.z_t(t) + self.vz_t(t + self.dt / 2) * self.dt
        self.listz.append(self.z)

        self.sqrt_xyz = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

        return self.listx[self.list_counter], self.listy[self.list_counter], self.listz[self.list_counter]
