import math 
from math import pi,sin,cos
import random


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

"""
def ladoEscogido(pLenAngulo: int):
        if pLenAngulo == 0 or pLenAngulo == 1 or pLenAngulo == 7:
            return 1
        if pLenAngulo == 3 or pLenAngulo == 4 or pLenAngulo == 5:
            return 0

def distanciaMax():

    return 0
"""
#oeste,este,norte,sur
angulos_direcciones = [0, pi*3/4, pi/2, pi/4, pi, -pi/4, -pi/2, -pi*3/4]
largo_angulos_posibles = len(angulos_direcciones)-1
inicial_random_indice = random.randint(0, largo_angulos_posibles)
inicial_random = angulos_direcciones[inicial_random_indice]

#lado_escogido = ladoEscogido(inicial_random_indice) #A cual lado debo mandar el rango si a la der o izq para encontrar la distanciaMaxima

"""
Generic Logic
"""
class Abeja:
    def __init__(self,padre=None,madre=None):
        if padre==None or madre==None:
            desviacionMaxima=0
            direccionFavorita=inicial_random
            colorFavorito=(0,0,255)
            toleranciaAlColor=0
            anguloDesviacion=0
            recorrido=[(200,200),2] #2=random
            nectar_recolectado=[]
            #distanciaMaxima=distanciaMax(lado_escogido)
            distanciaMaxima=0
            self.desviacionMaxima=desviacionMaxima
            self.direccionFavorita=direccionFavorita
            self.colorFavorito=colorFavorito
            self.toleranciaAlColor=toleranciaAlColor
            self.anguloDesviacion=anguloDesviacion
            self.recorrido=recorrido
            self.nectar_recolectado=nectar_recolectado
            self.distanciaMaxima=distanciaMaxima
        else:
            return 0
            #reproducir a papá y mamá XD
    def cruce(self,otraAbeja):
        return 0
    def simularRecorrido(self):
        #para el recorrido random
        distanciaDesdeElCentro=random()*self.distanciaMaxima
        angulo=random.randint(self.direccionFavorita-self.desviacionMaxima,self.direccionFavorita+self.desviacionMaxima)
        x=50+sin(angulo)*distanciaDesdeElCentro
        y=50+cos(angulo)*distanciaDesdeElCentro


        #para anchura:
        #for r in range(0,self.dis)
        #return 0
"""
Garden Logic
"""
class Flor:
    def __init__(self,pRadio,pAngulo,pMuestras):
        self.radio = pRadio
        self.anagulo = pAngulo
        self.muestras = pMuestras


"""
Setup
"""
ancho, alto = 100



"""
Pasar de un binario a entero.
print(int('01010', 2))
"""
