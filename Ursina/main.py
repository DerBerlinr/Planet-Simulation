from ursina import *

app = Ursina() # App erstellen

window.title = 'Planetensimulation'  # 'Meta-Daten' der App setzen
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

planets = []

class Planet(Entity):
    def __init__(self):
        super().__init__(
            model='sphere',
            color=color.orange,
        )
        planets.append(self)
    def update(self):   # update gets automatically called.
        self.x += held_keys['d'] * .1
        self.x -= held_keys['a'] * .1
        self.y += held_keys['w'] * .1
        self.y -= held_keys['s'] * .1
        self.z += held_keys['q'] * .1
        self.z -= held_keys['e'] * .1

planet1 = Planet()
app.run()   # opens a window and starts the game.
