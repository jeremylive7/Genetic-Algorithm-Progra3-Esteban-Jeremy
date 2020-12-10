import math 
from math import pi,sin,cos
from random import random, choices
from abc import abstractmethod

#oeste,este,norte,sur
angulos_direcciones = [0, pi*3/4, pi/2, pi/4, pi, -pi/4, -pi/2, -pi*3/4]
largo_angulos_posibles = len(angulos_direcciones)-1
inicial_random_indice = random.randint(0, largo_angulos_posibles)
inicial_random = angulos_direcciones[inicial_random_indice]
def frange(inicio,fin,step):
    return [inicio + i*step for i in range((fin-inicio)/step)]
"""
Genetic Logic
"""
class Abeja:
    def __init__(self,padre=None,madre=None):
        if padre==None or madre==None:
            desviacionMaxima=0
            direccionFavorita=inicial_random
            colorFavorito=(0,0,255)
            toleranciaAlColor=0
            anguloDesviacion=0
            recorrido=random()*(2**8-1)#2=random
            nectar_recolectado=[]
            #distanciaMaxima=distanciaMax(lado_escogido)
            distanciaMaxima=random.randint(0,71)
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
    def cmpRecorrido(self,objetivo):
        return self.recorrido%3==objetivo
    def esAnchura(self):
        return self.cmpRecorrido(0)
    def esRandom(self):
        return self.cmpRecorrido(1)
    def esProfundo(self):
        return self.cmpRecorrido(2)
    def randompos(self):
        return randompos(self.distanciaMaxima,self.direccionFavorita,self.desviacionMaxima)
    def izq(self):
        return self.direccionFavorita-self.desviacionMaxima
    def der(self):
        return self.direccionFavorita+self.desviacionMaxima
    def calcularRecorrido(self):
        """
        Crea una lista de puntos sobre los que hipotéticamente pasará
        la abeja
        """
        puntos=set()
        if self.esAnchura():
            for a in frange(self.izq(),self.der(),0.01):
                for r in range(self.distanciaMaxima):
                    puntos.add(XYfromPolar(CX,CY,r,a))
        elif self.esRandom():
            for _ in range(150):
                puntos.add(self.randompos())
        else:
            for r in range(self.distanciaMaxima):
                for a in frange(self.izq(),self.der(),0.01):
                    puntos.add(XYfromPolar(CX,CY,r,a))
        return puntos

    def cruce(self,otraAbeja):
        return 0
"""
Garden Logic
"""
class Flor:
    def __init__(self,pRadio,pAngulo,pMuestras):
        self.radio = pRadio
        self.angulo = pAngulo
        self.muestras = pMuestras
        self.x=int(random()*100)
        self.y=int(random()*100)
CANT_GENERACIONES=200
CANT_ABEJAS=20
CANT_FLORES=50
MARGEN_EVOLUCION=2
CX=50
CY=50
def XYfromPolar(oriX,oriY,r,a):
    """
    Desde el punto de origen (oriX,oriY), se calcula un punto a distancia R y a angulo A
    """
    return (oriX+sin(a)*r,  oriY+cos(a)*r)
def randompos(r,fav,mistake):
    distanciaDesdeElCentro=random()*r
    angulo=(fav-mistake)+random()*(2*mistake)
    return XYfromPolar(CX,CY,distanciaDesdeElCentro,angulo);
def distancia(p1,p2):
    return pow(pow(p1[0]-p2[0],2)+pow(p1[1]-p2[1],2),1/2)
def jardin():
    """
    Esta función simula el comportamiento el jardín atravez de las
    generaciones de abejas y el respectivo comportamiento de las
    flores.
    """
    def calificacion(abeja):
        """
        Esta función busca calificar cada abeja pero recordando si ya
        se calificó una abeja con estos resultados de recorrido
    Guarda el historial de todas las generaciones para consultarlo después.
        @param abeja: la abeja de la que se desea saber la calificacion
        @return: la calificación de esta abeja
        """
        nonlocal cacheCalif
        return cacheCalif[abeja]
    def reproducirAbejas(abejas):
        """
        Esta función reproducirá las abejas según su calificación
        normalizada (cacheCalificaciones), retornando la nueva
        lista de abejas
        @param abejas: la población que se va a reproducir
        """
        nonlocal cacheNormalizedFitness
        nuevasAbejas=[]
        pesos=[
            cacheNormalizedFitness[abeja] 
            for abeja in abejas
        ]
        for _ in range(CANT_ABEJAS):
            abejaPadre,abejaMadre=choices(
                abejas,
                weights=pesos,
                k=2)
            nuevasAbejas.append(Abeja(abejaPadre,abejaMadre))
        return nuevasAbejas

    cacheNormalizedFitness={}
    cacheCalif={}
    #Aquí comienza lo bueno#
    def getFlor(punto):
        nonlocal flores
        for flor in flores:
            if flor.x==punto[0] and flor.y==punto[1]:
                return flor
        return None
    abejas=[
        Abeja()
        for _ in range(CANT_ABEJAS)
    ]
    flores=[
        Flor()
        for _ in range(CANT_FLORES)
    ]
    for g in range(CANT_GENERACIONES):
        #pintarFlores()
        sumCalifGener=0
        for abeja in abejas:
            recorrido=abeja.calcularRecorrido()
            puntoAnterior=(CX,CY)
            distanciaRecorrida=0
            for punto in recorrido:
                #pintarRecorrido(abeja,punto)
                flor=getFlor(punto)
                if flor!=None:#Simular Interaccion entre la abeja y la flor
                    flor.muestras+=abeja.polen
                    abeja.polen+=[flor.getMuestra()]
                    abeja.cantFlores+=1
                    distanciaRecorrida+=distancia(puntoAnterior,punto)#¡Duda!#
                puntoAnterior=punto
            cacheCalif[abeja]=K*distanciaRecorrida/Q*abeja.cantFlores #Calificación bruta
            sumCalifGener+=cacheCalif[abeja]
        for abeja in abejas:
            cacheNormalizedFitness[abeja]=calificacion(abeja)/sumCalifGener #Calificacion relativa
        abejas=reproducirAbejas(abejas)
        nuevasFlores=[
            flor.reproducir()
            for flor in flores
        ]
        flores=nuevasFlores
        #despintarViejasFlores()

        

"""
Setup
"""
ancho, alto = 100





def convertColorIntToBinario(pColor:int):
    return int(str(pColor),2)

def convertColorBinarioToInt(pColor:int):
    return int(str(pColor),2)

def createColor(pColor):
    colorBinario = []
    for i in pColor:
        colorBinario.append(convertColorIntToBinario(i))

    for j in colorBinario:
        print("ColorBinario-%s"%colorBinario[j])
    
    #Hacer el cruce y mutacion.
    #...

def prueba1():
    createColor((0,0,255))

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

def hayEvolucion(abejas):
    """ @deprecated
    Esta función determina si la generación actual de abejas
    ha mejorado lo suficiente respecto de la generación anterior
    Sacando la calificación promedio de las abejas de esta 
    generación y comparandola con las calificaciones de la 
    generación anterior
    @param abejas: La lista de abejas a las que se le consultará
    la diferencia con los papás para determinar la mejoría
    entre generaciones.
    @return: Un booleano que indica si la población completa 
    continúa evolucionando. 
    """
    suma=0
    for abeja in abejas:
        suma+=pow(pow(calificacion(abeja.padre)-calificacion(abeja),2)+
            pow(calificacion(abeja.madre)-calificacion(abeja),2),0.5)
    return suma/CANT_ABEJAS>MARGEN_EVOLUCION