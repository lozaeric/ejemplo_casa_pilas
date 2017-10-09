import pilasengine

class Casa(pilasengine.actores.Actor):
    def iniciar(self, luces):
        self.imagen = "casa.png"
        self.luces = luces
    def apagar_luces(self):
        for l in self.luces:
            l.apagar() 
    def prender_luces(self):
        for l in self.luces:
            l.prender()
class Luz(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "apagada.png"
    def prender(self):
        self.imagen = "prendida.png"
    def apagar(self):
        self.imagen = "apagada.png"

def cambio():
    global pilas,tarde,noche,casa
    if tarde:
        tarde = False
        noche = True
        pilas.fondos.Noche()
        casa.prender_luces()
    elif noche:
        tarde = True
        noche = False
        pilas.fondos.Tarde()
        casa.apagar_luces()
    return True

pilas = pilasengine.iniciar()
# Luces
luces = [Luz(pilas), Luz(pilas)]
luces[0].x = -50
luces[0].y = 20
luces[1].x = 50
luces[1].y = 20
# Casa
casa = Casa(pilas, luces=luces)
casa.y = -130
# Escenario
noche = False
tarde = True
pilas.fondos.Tarde()
pilas.tareas.agregar(3, cambio)