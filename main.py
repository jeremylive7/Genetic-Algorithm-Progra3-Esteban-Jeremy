import math
from math import pi, sin, cos
import random
from abc import abstractmethod

#oeste,este,norte,sur
angulos_direcciones = [0, pi*3/4, pi/2, pi/4, pi, -pi/4, -pi/2, -pi*3/4]
largo_angulos_posibles = len(angulos_direcciones)-1
inicial_random_indice = random.randint(0, largo_angulos_posibles)
inicial_random = angulos_direcciones[inicial_random_indice]

"""
Generic Logic
"""
class AbejaIndividuo:
    def __init__(self, padre=None, madre=None):
        if padre == None or madre == None:
            desviacionMaxima = 0
            direccionFavorita = inicial_random
            colorFavorito = (0, 0, 255)
            toleranciaAlColor = 0
            anguloDesviacion = 0
            recorrido = [(200, 200), 2]  # 2=random
            nectar_recolectado = []
            #distanciaMaxima=distanciaMax(lado_escogido)
            distanciaMaxima = random.randint(0, 71)
            self.desviacionMaxima = desviacionMaxima
            self.direccionFavorita = direccionFavorita
            self.colorFavorito = colorFavorito
            self.toleranciaAlColor = toleranciaAlColor
            self.anguloDesviacion = anguloDesviacion
            self.recorrido = recorrido
            self.nectar_recolectado = nectar_recolectado
            self.distanciaMaxima = distanciaMaxima
        else:
            return 0
            #reproducir a papá y mamá XD

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


CANT_ABEJAS = 20
CANT_FLORES = 50
MARGEN_EVOLUCION = 2


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


"""
Setup
"""
ancho = 100
alto = 100


def get_bin(x): return format(x, 'b')

def convertColorIntToBinario(pColor: int):
    return get_bin(pColor)


def convertColorBinarioToInt(pColor: int):
    return int(str(pColor), 2)


def createColor(pColor):
    colorBinario = []
    for i in pColor:
        colorBinario.append(convertColorIntToBinario(i))

    for j in range(len(colorBinario)):
        print("ColorBinario[%s]=%s" %(j,colorBinario[j]))

    #Hacer el cruce y mutacion.
    #...

def prueba1():
    createColor((0, 0, 255))

prueba1()




"""
Pasar de un binario a entero.
print(int('01010', 2))
"""


""" cromosomas de las abejas:
direccion favorita (norte, noreste, etc)
color favorito (rojo, anaranjado, etc)
0 FF/16 rojo
forma de recorrido (en anchura, aleatorio, en profundidad)
                    0 - FF/3, FF/3 - 2*FF/3, 2*FF/3 - FF
margen máximo de desviación

cromosomas de las flores:
 color
 posicion
"""
