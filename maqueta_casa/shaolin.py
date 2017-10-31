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
        if abs(shao.x-self.x)<50 and not self.prendida:
            self.prender()
        if abs(shao.x-self.x)>=50 and self.prendida:
            self.apagar()

pilas = pilasengine.iniciar()
#shaolin
shao = pilas.actores.Shaolin()
shao.y = -240
shao.x = -240
shao.escala = 1.0
#luces
luces =[Luz(pilas),Luz(pilas),Luz(pilas)]
luces[0].x = -150
luces[0].y = -50
luces[1].y = -50
luces[2].x = 150
luces[2].y = -50
#escenario
pilas.fondos.Volley()
pilas.ejecutar()
