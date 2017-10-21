# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

pilas.fondos.Cesped()

mono = pilas.actores.Mono()
mono.x = -50
mono.y = 0

cantidad_bananas = 0

banana = pilas.actores.Banana()
banana.x = 100
banana.y = 0
cantidad_bananas = cantidad_bananas+1

otra_banana = pilas.actores.Banana()
otra_banana.x = 100
otra_banana.y = 50
cantidad_bananas = cantidad_bananas+1

mono.decir("Tengo "+str(cantidad_bananas)+" bananas")
mono.sonreir()

pilas.ejecutar()
