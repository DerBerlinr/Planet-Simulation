from ursina import *

app = Ursina()

window.title = 'planet simulation'  # set meta data for app
window.borderless = True
window.fullscreen = True
window.exit_button.visible = True
window.fps_counter.enabled = True


class Planet(Entity):
    def __init__(self, color, name, speed=1, mass=1, diameter=1, x=0, y=0, z=0):
        super().__init__(
            model='sphere',
            color=color,
            collision=True,
            collider='sphere'
            # TODO: add Textures
        )
        self.name = name
        self.speed = speed
        self.mass = mass
        self.scale = Vec3(diameter, diameter, diameter)
        self.x = x
        self.y = y
        self.z = z

    def set_coords(self, x, y, z):  # set coordinates of planet
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


planet_data_temp = []


def add_planet():
    for i in buttons:
        i.enabled = False

    name_field = InputField(name='name_field')
    mass_field = InputField(name='mass_field')
    speed_field = InputField(name='speed_field')
    pos_x_field = InputField(name='pos_x_field')
    pos_y_field = InputField(name='pos_y_field')
    pos_z_field = InputField(name='pos_z_field')

    planet_data_temp.append(name_field)
    planet_data_temp.append(mass_field)
    planet_data_temp.append(speed_field)
    planet_data_temp.append(pos_x_field)
    planet_data_temp.append(pos_y_field)
    planet_data_temp.append(pos_z_field)

    win = WindowPanel(
        title='add planet',
        content=(
            Text('name:'),
            name_field,
            Text('mass in kg:'),
            mass_field,
            Text('speed in m/s:'),
            speed_field,
            Text('x-position:'),
            pos_x_field,
            Text('y-position:'),
            pos_y_field,
            Text('z-position:'),
            pos_z_field,
            Button(text='Submit', color=color.azure, on_click=submit_planet_data)
        ),
    )
    planet_data_temp.append(win)


def submit_planet_data():
    '''
    name = planet_data_temp[0].text
    mass = int(planet_data_temp[1].text)
    speed = int(planet_data_temp[2].text)
    pos_x = int(planet_data_temp[3].text)
    pos_y = int(planet_data_temp[4].text)
    pos_z = int(planet_data_temp[5].text)
    temp = Planet(color=color.blue, name=name, speed=speed, mass=mass, x=pos_x, y=pos_y, z=pos_z)
    planet_data_temp[6].close()
    mouse.locked = True
    '''
    exit()


# BUTTONS --------------------------------------------------------------------------

bu_reenter = Button(position=(0, .25, 0), text='Reenter Game', scale=(.5, .07))
buttons.append(bu_reenter)
bu_reenter.on_click = reenter_game

bu_add = Button(position=(0, .15, 0), text='Add Planet', scale=(.5, .07))
buttons.append(bu_add)
bu_add.on_click = add_planet

# SETUP +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

planet = Planet(color=color.orange, name="planet1")  # crate a planet
planet.set_coords(9, 0, 9)  # set Pos of planet

fpc = FirstPersonController()

app.run()
