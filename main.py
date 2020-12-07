from ursina import *
# from ursina.prefabs.first_person_controller import FirstPersonController
from first_person import FirstPersonController

app = Ursina()  # App erstellen

window.title = 'Planetensimulation'  # 'Meta-Daten' der App setzen
window.borderless = True
window.fullscreen = True
window.exit_button.visible = True
window.fps_counter.enabled = True


class Planet(Entity):
    def __init__(self, color, speed=1, mass=1, diameter=1, x=0, y=0, z=0):  # Entity wird erstellt, indem die init-Methode der Entity-Klasse aufgerufen wird
        super().__init__(
            model='sphere',  # Planet soll ballförmig sein
            color=color,  # farbe des Planeten wird festgelegt
            collision=True,
            collider='sphere'
            # TODO: add Textures
        )
        self.speed = speed
        self.mass = mass
        self.scale = Vec3(diameter, diameter, diameter)
        self.x = x
        self.y = y
        self.z = z

    def set_coords(self, x, y, z):  # Koordinaten eines Planeten setzen
        self.x = x
        self.y = y
        self.z = z

class FirstPersonController(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.speed = 5

        self.camera_pivot = Entity(parent=self, y=2)
        self.cursor = Entity(parent=camera.ui, model='quad', color=color.pink, scale=.008, rotation_z=45)

        camera.parent = self.camera_pivot
        camera.position = (0,0,0)
        camera.rotation = (0,0,0)
        camera.fov = 90
        mouse.locked = True
        self.mouse_sensitivity = Vec2(40, 40)
        self.target_smoothing = 100
        self.smoothing = self.target_smoothing

button = Button(position=(-.5, .25, 0), text='button_text')
button.scale *= .2
button.text_entity.scale /= .2
button.tooltip = Tooltip('tooltip text')


planet = Planet(color=color.orange)  # crate a planet
planet.set_coords(9,0,9)  # set Pos of planet

cam = FirstPersonController() # FPC wird erstellt

def update_camera():
    # CAMERA ROTATION ---------------------------------------------------------------
    cam.rotation_y += mouse.velocity[0] * cam.mouse_sensitivity[1]

    cam.camera_pivot.rotation_x -= mouse.velocity[1] * cam.mouse_sensitivity[0]
    cam.camera_pivot.rotation_x = clamp(cam.camera_pivot.rotation_x, -90, 90)

    # CAMERA POSITION ---------------------------------------------------------------
    cam.direction = Vec3(cam.forward * (held_keys['w'] - held_keys['s']) +
                          cam.right * (held_keys['d'] - held_keys['a']) +
                          cam.up * (held_keys['space'] - held_keys['shift'])
                          ).normalized()

    cam.position += cam.direction * cam.speed * time.dt

    # EXIT FPC ---------------------------------------------------------------------

    if held_keys['escape']:
        mouse.locked = False

cam.update = update_camera

app.run()
