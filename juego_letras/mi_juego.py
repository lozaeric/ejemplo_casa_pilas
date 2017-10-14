# 4cod2848ing: utf-8
import pilasengine

pilas = pilasengine.iniciar()
palabras = (("casa","gato","cerdo","perro", "cielo","leon","tigre"),("conejo","teclado","edificio","planeta","automovil","jirafa"))
nivel = 0
nave = pilas.actores.Nave()
palabraUsuario = pilas.actores.Texto("")
nivelActual = pilas.actores.Texto("Nivel 1")
letras = []
palabra = ""
boton = pilas.interfaz.Boton ("Reiniciar Juego")

def nuevoJuego ():
    global palabra
    for let in letras:
        let.eliminar()
    palabra = palabras[nivel][pilas.azar(0,len(palabras[nivel])-1)]
    palabraUsuario.definir_texto ("")
    for i in range (0, len (palabra)):
        nuevaLetra = pilas.actores.Texto (palabra[i])
        nuevaLetra.y = pilas.azar(-175,200)
        nuevaLetra.x = pilas.azar(-200,200)
        nuevaLetra.etiquetas.agregar ("letra")
        letras.append (nuevaLetra)
    nave.x = 0
    nave.y = -190
    nave.decir ("A formar la palabra!")

def procesar (nave, letra):
    global palabra, nivel
    palabraUsuario.definir_texto (palabraUsuario.obtener_texto()+letra.obtener_texto())
    letra.eliminar ()
    letras.remove (letra)
    if len(letras)==0:
        if palabraUsuario.obtener_texto () == palabra:
            nave.decir ("Juego Ganado")
            nivel+=1
            if nivel>0:
                nivelActual.definir_texto ("Nivel 2")
            else:
                nivelActual.definir_texto ("Nivel 1")
        else:
            nave.decir ("Juego Perdido")
        pilas.tareas.agregar(5, nuevoJuego)  
        palabraUsuario.definir_texto ("")
        pilas.camara.vibrar()
pilas.fondos.Espacio()
boton.conectar (nuevoJuego)
nave.etiquetas.agregar ("nave")
boton.y = -200
boton.x = 250 
palabraUsuario.y = -180
palabraUsuario.x = -250
nivelActual.y = -220
nivelActual.x = -220
palabraUsuario.escala = 2
pilas.colisiones.agregar ("nave","letra", procesar)
nuevoJuego()

pilas.ejecutar()