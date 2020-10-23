from ursina import *

app = Ursina()  # App erstellen

window.title = 'Planetensimulation'  # 'Meta-Daten' der App setzen
window.borderless = True
window.fullscreen = True
window.exit_button.visible = True
window.fps_counter.enabled = True

planets = []


class Planet(Entity):
    def __init__(self, that_color):  # Entity wird erstellt, indem die init-Methode der Entity-Klasse aufgerufen wird
        super().__init__(
            model='cube',  # Planet soll ballförmig sein
            color=that_color,  # farbe des Planeten wird festgelegt
        )
        planets.append(self)

    def set_coords(self, x, y, z):  # Koordinaten eines Planeten setzen
        self.x = x
        self.y = y
        self.z = z

    def update(self):   # testen zum herumbewegen eines Planeten
        self.x += held_keys['d'] * .1
        self.x -= held_keys['a'] * .1
        self.y += held_keys['w'] * .1
        self.y -= held_keys['s'] * .1
        self.z += held_keys['q'] * .1
        self.z -= held_keys['e'] * .1


p = Planet(color.orange)

app.run()   # opens a window and starts the game.
