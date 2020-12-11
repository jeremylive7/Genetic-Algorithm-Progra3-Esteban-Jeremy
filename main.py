from math import pi, sin, cos
import random
from abc import abstractmethod
from Cruce import Cruce

CANT_ABEJAS = 20
CANT_FLORES = 50
MARGEN_EVOLUCION = 2

"""
Generic Logic

Tipo de recorrido:
    1-) Random.
    2-) ...
    3-) ...
"""
class AbejaIndividuo:    

    def __init__(self, pDireccion_favorita, pColor_favorito, pTolerancia_al_color, pAngulo_desviacion, pDistancia_maxima):
        self.direccion_favorita = pDireccion_favorita
        self.color_favorito = pColor_favorito
        self.tolerancia_al_color = pTolerancia_al_color
        self.angulo_desviacion = pAngulo_desviacion
        self.distancia_maxima = pDistancia_maxima

      
    @abstractmethod
    def simularRecorrido(self):
        """
        Debe simular el recorrido y devolver la información necesaria 
        para hacer el cálculo de adaptabilidad
        """

    def cruce(self, otraAbeja):
        return 0

class AbejaRandom(AbejaIndividuo):
    def simularRecorrido(self):
        distanciaDesdeElCentro = random()*self.distanciaMaxima
        angulo = random.randint(self.direccionFavorita-self.desviacionMaxima,
                                self.direccionFavorita+self.desviacionMaxima)
        x = 50+sin(angulo)*distanciaDesdeElCentro
        y = 50+cos(angulo)*distanciaDesdeElCentro

class AbejaAnchura(AbejaIndividuo):
    def simularRecorrido(self):
        pass

class AbejaProfundidad(AbejaIndividuo):
    def simularRecorrido(self):
        pass

"""
Garden Logic
"""
class Flor:
    def __init__(self, pRadio, pAngulo, pMuestras):
        self.radio = pRadio
        self.anagulo = pAngulo
        self.muestras = pMuestras

def jardin():
    cacheCalificaciones = {}

    def hayEvolucion(abejas):
        """
        Esta función determina si la generación actual de abejas
        ha mejorado lo suficiente respecto de la generación anterior
        Sacando la calificación promedio de las abejas de esta 
        generación y comparandola con las calificaciones de la 
        generación anterior
        """
        suma = 0
        for abeja in abejas:
            suma += pow(pow(calificacion(abeja.padre)-calificacion(abeja), 2) +
                        pow(calificacion(abeja.madre)-calificacion(abeja), 2), 0.5)
        return suma/CANT_ABEJAS > MARGEN_EVOLUCION

    def calificarAbejas(abejas):
        nonlocal cacheCalificaciones
        suma = 0
        for abeja in abejas:
            suma += calificacion(abeja)
        cacheCalificaciones['total'] = suma
        for abeja in abejas:
            cacheCalificaciones[abeja] = calificacion(abeja)/suma

    def reproducirAbejas(abejas):
        nonlocal cacheCalificaciones
        nuevasAbejas = []
        for _ in range(CANT_ABEJAS):
            abejaPadre = 0
            abajaMadre = 0
            nuevasAbejas.append(Abeja(abejaMadre, abejaPadre))

    abejas = [
        AbejaIndividuo()
        for _ in range(CANT_ABEJAS)
    ]
    flores = [
        Flor()
        for _ in range(CANT_FLORES)
    ]
    while hayEvolucion(abejas):
        for abeja in abejas:
            abeja.simularRecorrido(flores)
        nuevasFlores = [
            flor.reproducir()  # nueva flor si su lista de muestras está vacía
            for flor in flores
        ]
        calificarAbejas(abejas)  # debe conservarse el linaje
        reproducirAbejas(abejas)  # debe conservarse el linaje
        flores = nuevasFlores

class Cruce():

    def creoListaDeBits(abeja):
        PARAM_SIZE_1 = 16
        PARAM_SIZE_2 = 8
        listaGenesBits = ''

        direccion_favorita = abeja.direccion_favorita
        color_favorito = abeja.color_favorito
        tolerancia_al_color = abeja.tolerancia_al_color
        angulo_desviacion = abeja.angulo_desviacion
        distancia_maxima = abeja.distancia_maxima

        # ! Debe estar entre 0 y 2*pi
        codGeneticoDirFav = int(0xffff*direccion_favorita/(2*pi))
        codGeneticoTolerancia = int(0xff*tolerancia_al_color)
        codGeneticoAnguloDesviacion = int(0xffff*angulo_desviacion/(2*pi))
        codGeneticoDistanciaMaxima = int(0xff*distancia_maxima/70.71)

        listaGenesBits += bin(codGeneticoDirFav).replace("-","")[2:].zfill(PARAM_SIZE_1)
        listaGenesBits += bin(codGeneticoTolerancia)[2:].zfill(PARAM_SIZE_2)
        listaGenesBits += f'{bin(color_favorito[0])[2:].zfill(PARAM_SIZE_2)}{bin(color_favorito[1])[2:].zfill(PARAM_SIZE_2)}{bin(color_favorito[2])[2:].zfill(PARAM_SIZE_2)}'
        listaGenesBits += bin(codGeneticoAnguloDesviacion)[
            2:].zfill(PARAM_SIZE_1)
        listaGenesBits += bin(codGeneticoDistanciaMaxima)[
            2:].zfill(PARAM_SIZE_2)

        return listaGenesBits

    def cruzarPadres(abeja_padre, abeja_madre):
        lista_padre = Cruce.creoListaDeBits(abeja_padre)
        lista_madre = Cruce.creoListaDeBits(abeja_madre)

        pivote_random = random.randint(0, len(lista_padre)-1)

        binario_hijo_1 = lista_padre[:pivote_random]+lista_madre[pivote_random:]
        binario_hijo_2 = lista_madre[:pivote_random]+lista_padre[pivote_random:]

        print("hijo1: %s" % binario_hijo_1)
        print("hijo2: %s" % binario_hijo_2)

        result = []
        result.append(Cruce.transformarEnAbeja(binario_hijo_1))
        result.append(Cruce.transformarEnAbeja(binario_hijo_2))

        return result

    def transformarEnAbeja(genoma):
        codGeneticoDirFav=genoma[1:16]
        codGeneticoTolerancia=genoma[16:24]
        codGeneticoColorFav=genoma[24:48]
        codGeneticoAnguloDesviacion=genoma[48:64]
        codGeneticoDistanciaMaxima=genoma[64:72]
        a=AbejaIndividuo(
            int(codGeneticoDirFav,2)/0xffff*2*pi,
            (int(codGeneticoColorFav[:8],2), int(codGeneticoColorFav[8:16],2), int(codGeneticoColorFav[16:],2)),
            int(codGeneticoTolerancia,2)/0xff,
            int(codGeneticoAnguloDesviacion, 2)/0xffff*2*pi,
            int(codGeneticoDistanciaMaxima, 2)/0xff*70.71)

        return a

def creoAbeja():

    direccion_random_indice = random.randint(0, largo_angulos_posibles)
    direccion_random = angulos_direcciones[direccion_random_indice]
    color_random_indice = random.randint(0, largo_colores_rgb)
    color_random = colores_rgb[color_random_indice]

    direccion_favorita = direccion_random
    color_favorito = color_random
    tolerancia_al_color = random.randint(0, 1)
    angulo_desviacion = random.randint(30, 40)
    distancia_maxima = random.randint(0, 71)

    return AbejaIndividuo(direccion_favorita, color_favorito, tolerancia_al_color, angulo_desviacion, distancia_maxima)


#oeste,este,norte,sur
angulos_direcciones = [0, pi*3/4, pi/2, pi/4, pi, -pi/4, -pi/2, -pi*3/4]
largo_angulos_posibles = len(angulos_direcciones)-1

#                  rojo,    naranja         amarillo       verde        celeste        azul         morado        fuchsia
colores_rgb = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (127, 0, 255), (255, 0, 255)]
largo_colores_rgb = len(colores_rgb)-1

#Inicializo abejas Padres
abeja1 = creoAbeja()
abeja2 = creoAbeja()
abeja_hijo = Cruce.cruzarPadres(abeja1, abeja2)

for j in range(len(abeja_hijo)):
    if j == 0:
        print("Variables hijo1: \n Direccion favorita: %s \n Color favorito: %s \n Tolerancia al color: %s \n Angulo desviacion: %s \n Distancia maxima: %s" % (
            abeja_hijo[j].direccion_favorita, abeja_hijo[j].color_favorito, abeja_hijo[j].tolerancia_al_color, abeja_hijo[j].angulo_desviacion, abeja_hijo[j].distancia_maxima))
    else:
        print("Variables hijo2: \n Direccion favorita: %s \n Color favorito: %s \n Tolerancia al color: %s \n Angulo desviacion: %s \n Distancia maxima: %s" % (
            abeja_hijo[j].direccion_favorita, abeja_hijo[j].color_favorito, abeja_hijo[j].tolerancia_al_color, abeja_hijo[j].angulo_desviacion, abeja_hijo[j].distancia_maxima))


"""
Setup
"""
ancho = 100
alto = 100
