from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()


class Planet(Entity):
    def __init__(self, color, speed=1, mass=1, diameter=1, x=0, y=0, z=0):  # Entity wird erstellt, indem die init-Methode der Entity-Klasse aufgerufen wird
        super().__init__(
            model='sphere',  # Planet soll ballförmig sein
            color=color,  # farbe des Planeten wird festgelegt
            collision=True,
            collider='sphere'
            # TODO: Texturen hinzufügen
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


planet = Planet(color=color.orange)
planet.set_coords(9,9,9)
player = FirstPersonController(jumping=False)
app.run()