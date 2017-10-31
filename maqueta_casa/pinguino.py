# coding: utf-8
import pilasengine

class Luz(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "apagada.png"
        self.escala = 0.5
        self.prendida = False
    def prender(self):
        self.imagen = "prendida.png"
        self.prendida = True
    def apagar(self):
        self.imagen = "apagada.png"
        self.prendida = False
    def actualizar(self):
        global pingu
        if abs(pingu.x-self.x)<50 and not self.prendida:
            self.prender()
        if abs(pingu.x-self.x)>=50 and self.prendida:
            self.apagar()

pilas = pilasengine.iniciar()
#pinguino
pingu = pilas.actores.Pingu()
pingu.y = -240
pingu.x = -240
pingu.escala = 1.0
#luces
luces =[Luz(pilas),Luz(pilas),Luz(pilas)]
luces[0].x = -150
luces[0].y = -75
luces[1].y = -75
luces[2].x = 150
luces[2].y = -75
#escenario
pilas.fondos.Tarde()
pilas.ejecutar()
