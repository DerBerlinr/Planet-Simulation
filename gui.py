from direct.stdpy.file import execfile
from ursina import *
from time import perf_counter


class GUI:
    def __init__(self, fpc, planet_list):

        self.planet_list = planet_list  # list of all planets in the simulation
        self.fpc = fpc

        # IN-GAME-MENU -------------------------------------------------------------------------------------------------
        self.buttons_gm = []

        self.bu_reenter = Button(position=(0, .25), text='Return to Simulation', scale=(.5, .07))
        self.buttons_gm.append(self.bu_reenter)
        self.bu_reenter.on_click = self.reenter_game


        # Time Menu -------------------------------------------------------------------------------

        self.dt_slider = Slider(position=(-.2, -.15), min=-6000, max=6000, default=3000, step=240, height=Text.size, text='Speed:', dynamic=False)
        self.buttons_gm.append(self.dt_slider)
        '''
        self.time_input_label = Text(text="Set time to:", position=(0, -.25))
        self.buttons_gm.append(self.time_input_label)

        self.time_input = prefabs.input_field.InputField(position=(0, -.35), scale=(.5, .07))
        self.buttons_gm.append(self.time_input)

        self.bu_time_input_submit = Button(position=(0, -.45), text='Jump to given time', scale=(.5, .07))
        self.buttons_gm.append(self.bu_time_input_submit)
        self.bu_time_input_submit.on_click = self.time_input_submit
        '''
        # --------------------------------------------------------------------------------------------------------------

        self.planet_data_temp = []
    '''
    def time_input_submit(self):
        if self.time_input.text > 0 and self.time_input.text < len(self.planet_list[0].poslist):
            self.fpc.time = int(self.time_input.text) - int(self.time_input.text) % 60 
    '''



    def reenter_game(self):
        mouse.locked = True

    @staticmethod
    def submit_planet_data():
        """
        name = planet_data_temp[0].text
        mass = int(planet_data_temp[1].text)
        speed = int(planet_data_temp[2].text)
        pos_x = int(planet_data_temp[3].text)
        pos_y = int(planet_data_temp[4].text)
        pos_z = int(planet_data_temp[5].text)
        temp = Planet(color=color.blue, name=name, speed=speed, mass=mass, x=pos_x, y=pos_y, z=pos_z)
        planet_data_temp[6].close()
        mouse.locked = True
        """
        exit()


class FirstPersonController(Entity):
    def __init__(self, planet_list):
        self.planet_list = planet_list
        super().__init__()

        # CAMERA -------------------------------------------------------------------------------------------------------

        self.speed = 5
        self.camera_pivot = Entity(parent=self, y=2)
        self.cursor = Entity(parent=camera.ui, model='quad', color=color.pink, scale=.008, rotation_z=45)
        camera.parent = self.camera_pivot
        camera.position = (0, 0, 0)
        camera.rotation = (0, 0, 0)
        camera.fov = 90
        mouse.locked = True
        self.direction = 0
        self.mouse_sensitivity = Vec2(40, 40)
        self.target_smoothing = 100
        self.smoothing = self.target_smoothing

        # HUD ----------------------------------------------------------------------------------------------------------

        self.hud_name = ''
        self.hud_text_name = Text(text=self.hud_name, origin=(0, 17))

        self.hud_coords = ''
        self.hud_text_coords = Text(text=self.hud_coords, origin=(0, 18))

        self.hud_vel = ''
        self.hud_text_vel = Text(text=self.hud_vel, origin=(0, 19))

        self.time = 0
        self.dt = 6000

        self.sel_plan = 0


        self.gui = GUI(self, planet_list)

        self.count = 0

        # Code by Petter Amland (modified by Erik Haarländer)
        for i in self.planet_list:
            line_renderer = Entity(
                model=Mesh(
                    vertices=[Vec3(0, 0, 0) for i in range(6)],
                    colors=[lerp(color.clear, color.white, i / 6 * 2) for i in range(6)],
                    mode='line',
                    thickness=5,
                    static=False
                )
            )
            i.trace = line_renderer
        self.trace_time = 0
        self.trace_counter = 0

    def update(self):
        if mouse.locked:
            if self.count == 10:
                self.count = 0
            else:
                self.count += 1
            for gui_element in self.gui.buttons_gm:
                gui_element.enabled = False

            # CAMERA ROTATION ------------------------------------------------------
            self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity[1]

            self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[0]
            self.camera_pivot.rotation_x = clamp(self.camera_pivot.rotation_x, -90, 90)

            # CAMERA POSITION ------------------------------------------------------
            self.direction = Vec3(self.forward * (held_keys['w'] - held_keys['s']) +
                                  self.right * (held_keys['d'] - held_keys['a']) +
                                  self.up * (held_keys['space'] - held_keys['shift'])
                                  ).normalized()

            self.position += self.direction / 2 * self.speed * time.dt

            # PLANET POSITION ------------------------------------------------------
            if not (round(self.gui.dt_slider.value) == 0 or (self.time <= 0 and round(self.gui.dt_slider.value) <= 0)):
                for planet in self.planet_list:
                    planet.x = planet.poslist[round(self.time / 60)][0] / 10000000000
                    planet.y = planet.poslist[round(self.time / 60)][1] / 10000000000
                    planet.z = planet.poslist[round(self.time / 60)][2] / 10000000000

                    # TRACES -----------------------------------------------------------
                    # Code by Petter Amland (modified by Erik Haarländer)
                    if self.trace_time >= .025:
                        self.trace_time = 0
                        if self.trace_counter == 100:
                            planet.trace.model.vertices.pop(0)
                            self.trace_counter = 0
                        else:
                            self.trace_counter += 1
                        planet.trace.model.vertices.append(Vec3(planet.x, planet.y, planet.z))
                        planet.trace.model.generate()
                    self.trace_time += time.dt

                # HUD ------------------------------------------------------------------

                for planet in self.planet_list:
                    if planet.button_pressed:
                        self.sel_plan = planet
                        planet.button_pressed = False

                px = 0
                py = 0
                pz = 0
                vx = 0
                vy = 0
                vz = 0
                if self.check_instance(self.sel_plan):
                    px, py, pz, vx, vy, vz = self.sel_plan.poslist[round(self.time / 60)]

                    self.hud_name = "name: " + self.sel_plan.planet_name
                    self.hud_text_name.color = color.red
                    self.hud_text_name.text = self.hud_name

                self.hud_coords = "x: " + str(round(px)) + "     y: " + str(round(py)) + "     z: " + str(round(pz))
                self.hud_text_coords.color = color.red
                self.hud_text_coords.text = self.hud_coords

                self.hud_vel = "vx: " + str(round(vx)) + "    vy: " + str(round(vy)) + "    vz: " + str(round(vz))
                self.hud_text_vel.color = color.red
                self.hud_text_vel.text = self.hud_vel
            # ----------------------------------------------------------------------
            if not (self.time <= 0 and round(self.gui.dt_slider.value) <= 0):
                self.time += round(self.gui.dt_slider.value)

        # EXIT FPC -----------------------------------------------------------------
        if held_keys['escape']:
            for gui_element in self.gui.buttons_gm:
                gui_element.enabled = True
            mouse.locked = False

    def check_instance(self, obj):
        return hasattr(obj, '__dict__')

