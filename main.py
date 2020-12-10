from ursina import *

app = Ursina()  # App erstellen

window.title = 'Planetensimulation'  # 'Meta-Daten' der App setzen
window.borderless = True
window.fullscreen = True
window.exit_button.visible = True
window.fps_counter.enabled = True


class Planet(Entity):
    def __init__(self, color, speed=1, mass=1, diameter=1, x=0, y=0,
                 z=0):  # Entity wird erstellt, indem die init-Methode der Entity-Klasse aufgerufen wird
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

# FIRST PERSON CONTROLLER +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


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

            self.position += self.direction * self.speed * time.dt

        # EXIT FPC -----------------------------------------------------------------
        if held_keys['escape']:
            for i in buttons:
                i.enabled = True
            mouse.locked = False


# BUTTONS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
buttons = []

# BUTTON FUNCS ---------------------------------------------------------------------

def reenter_game():
    mouse.locked = True


def add_Planet():
    for i in buttons:
        i.enabled = False

# BUTTONS --------------------------------------------------------------------------

bu_reenter = Button(position=(0, .25, 0), text='Reenter Game', scale=(.5, .07))
buttons.append(bu_reenter)
bu_reenter.on_click = reenter_game

bu_add = Button(position=(0, .15, 0), text='Add Planet', scale=(.5, .07))
buttons.append(bu_add)
bu_add.on_click = add_Planet

# SETUP +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

planet = Planet(color=color.orange)  # crate a planet
planet.set_coords(9, 0, 9)  # set Pos of planet

fpc = FirstPersonController()

app.run()
