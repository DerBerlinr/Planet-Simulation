from ursina import *
import threading
from calc import Calc


class FirstPersonController(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.speed = 5

        self.camera_pivot = Entity(parent=self, y=2)
        self.cursor = Entity(parent=camera.ui, model='quad', color=color.pink, scale=.008, rotation_z=45)

        camera.parent = self.camera_pivot
        camera.position = (0, 0, 0)
        camera.rotation = (0, 0, 0)
        camera.fov = 90
        mouse.locked = True
        self.mouse_sensitivity = Vec2(40, 40)
        self.target_smoothing = 100
        self.smoothing = self.target_smoothing
        self.time = 0
        self.timediff = 1200
        self.c = Calc(pos=np.array([140699825958.8049, -54738590238.00282, 2510791.537005455]), vel=np.array([10308.531985820431, 27640.154010970804, -0.7364511260199437]))#, timediff=self.timediff
        self.counter = 0
        self.a = Text(origin=(-1, -1))


    def update(self):
        if mouse.locked:
            for i in buttons:
                i.enabled = False
            # CAMERA ROTATION ------------------------------------------------------
            self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity[1]

            self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[0]
            self.camera_pivot.rotation_x = clamp(self.camera_pivot.rotation_x, -90, 90)

            # CAMERA POSITION ------------------------------------------------------
            self.direction = Vec3(self.forward * (held_keys['w'] - held_keys['s']) +
                                  self.right * (held_keys['d'] - held_keys['a']) +
                                  self.up * (held_keys['space'] - held_keys['shift'])
                                  ).normalized()

            self.position += self.direction/2 * self.speed * time.dt
            #print(self.position)
            #self.a.update_text(str(self.position[0]) + str(self.position[1]) + str(self.position[2]))

            # PLANET POS -----------------------------------------------------------
            old_x, old_y, old_z = self.c.get_coords(self.time)
            thread = Thread(target=self.c.get_coords, args=(self.time,))
            thread.start()
            return_value = thread.join()
            #print('POS: x=', old_x, '; y=', old_y, '; z=', old_z)
            a = self.c.v
            #print('SPEED: ', a)
            if self.counter == 1000:
                x = old_x/10000000000
                y = old_y/10000000000
                z = old_z/10000000000
                print('New_POS: x=', x, '; y=', y, '; z=', z)
                planet.set_coords(x, y, z)
                self.counter = 0
            self.counter += 1
            self.time += 1200 #self.timediff


        # EXIT FPC -----------------------------------------------------------------
        if held_keys['escape']:
            for i in buttons:
                i.enabled = True
            mouse.locked = False

if __name__ == "__main__":
    fpc = FirstPersonController()
    x = threading.Thread(target=fpc.update)
    x.start()
