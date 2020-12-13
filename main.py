import pygame
from pygame.locals import *
import threading
import statistics
from math import pi,sin,cos,sqrt, pow
from random import random, choices,randint,uniform,seed,choice
from abc import abstractmethod

"""
Genetic Logic
"""
class Abeja:
    def __init__(self, pDireccion_favorita, pColor_favorito, pTolerancia_al_color, pAngulo_desviacion, pDistancia_maxima,r):
        self.direccion_favorita = pDireccion_favorita
        self.color_favorito = pColor_favorito
        self.tolerancia_al_color = pTolerancia_al_color
        self.angulo_desviacion = pAngulo_desviacion
        self.distancia_maxima = pDistancia_maxima
        self.recorrido=r
        self.polen=[]
        self.cantFlores=0
        self.madre=None
        self.padre=None
    def cmpRecorrido(self,objetivo):
        return self.recorrido%3==objetivo
    def esAnchura(self):
        return self.cmpRecorrido(0)
    def esRandom(self):
        return self.cmpRecorrido(1)
    def esProfundo(self):
        return self.cmpRecorrido(2)
    def randompos(self):
        return randompos(self.distancia_maxima,self.direccion_favorita,self.angulo_desviacion)
    def izq(self):
        return self.direccion_favorita-self.angulo_desviacion
    def der(self):
        return self.direccion_favorita+self.angulo_desviacion
    def calcularRecorrido(self):
        """
        Crea una lista de puntos sobre los que hipotéticamente pasará
        la abeja
        """
        puntos=set()
        if self.esProfundo():
            for a in frange(self.izq(),self.der(),0.01):
                for r in range(int(self.distancia_maxima)):
                    puntos.add(XYfromPolar(CX,CY,r,a))
        elif self.esRandom():
            for _ in range(150):
                puntos.add(self.randompos())
        else:
            for r in range(int(self.distancia_maxima)):
                for a in frange(self.izq(),self.der(),0.01):
                    puntos.add(XYfromPolar(CX,CY,r,a))
        return puntos

    def cruce(self,otraAbeja):
        return 0
"""
Garden Logic
"""
class Flor:
    def __init__(self,pColor, pRadio, pAngulo):
        self.color = pColor
        self.radio = pRadio
        self.angulo = pAngulo
        self.muestras = []#pMuestras
    
    def getMuestra(self):
        return self.muestras

    def creoListaDeBitsFlor(self):
        listaGenesBits = ''

        color = self.color
        radio = self.radio
        angulo = self.angulo

        codGeneticoRadio = int(0xff*radio)
        codGeneticoAngulo = int(0xffff*angulo/(2*pi))

        listaGenesBits += f'{bin(color[0]).replace("-", "")[2:].zfill(PARAM_SIZE_2)}{bin(color[1])[2:].zfill(PARAM_SIZE_2)}{bin(color[2])[2:].zfill(PARAM_SIZE_2)}'
        listaGenesBits += bin(codGeneticoRadio)[2:].zfill(PARAM_SIZE_2)
        listaGenesBits += bin(codGeneticoAngulo)[2:].zfill(PARAM_SIZE_1)

        return listaGenesBits

    def reproducir(self):
        if len(self.muestras)==0:
            return crearFlor()
        madre=choice(self.muestras)
        return Flor.transformarEnFlor(self, Flor.cruzarFlores(self,madre))

    def cruzarFlores(flor_padre, flor_madre):
        lista_padre = Flor.creoListaDeBitsFlor(flor_padre)
        lista_madre = Flor.creoListaDeBitsFlor(flor_madre)

        pivote_random = randint(0, len(lista_padre)-1)

        binario_hijo_1 = lista_padre[:pivote_random] + \
            lista_madre[pivote_random:]
        return binario_hijo_1

    def transformarEnFlor(self,genoma):
        codGeneticoColor = genoma[:24]
        codGeneticoRadio = genoma[24:32]
        codGeneticoAngulo = genoma[32:48]
        return Flor(
            (int(codGeneticoColor[:8],2), int(codGeneticoColor[8:16],2), int(codGeneticoColor[16:],2)),
            int(codGeneticoRadio, 2)/0xff*self.radio,
            int(codGeneticoAngulo, 2)/0xffff*self.angulo/(2*pi)
        )

        
class Cruce():

    def creoListaDeBits(abeja):
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
        codGeneticoDistanciaMaxima = int(0xff*distancia_maxima/limite)
        codGenRec=int(0xff*abeja.recorrido/3)
        listaGenesBits += bin(codGeneticoDirFav).replace("-","")[2:].zfill(PARAM_SIZE_1)
        listaGenesBits += bin(codGeneticoTolerancia)[2:].zfill(PARAM_SIZE_2)
        listaGenesBits += f'{bin(color_favorito[0])[2:].zfill(PARAM_SIZE_2)}{bin(color_favorito[1])[2:].zfill(PARAM_SIZE_2)}{bin(color_favorito[2])[2:].zfill(PARAM_SIZE_2)}'
        listaGenesBits += bin(codGeneticoAnguloDesviacion)[2:].zfill(PARAM_SIZE_1)
        listaGenesBits += bin(codGeneticoDistanciaMaxima)[2:].zfill(PARAM_SIZE_2)
        listaGenesBits += bin(codGenRec)[2:].zfill(PARAM_SIZE_2)

        return listaGenesBits

    def cruzarAbejas(abeja_padre, abeja_madre):
        lista_padre = Cruce.creoListaDeBits(abeja_padre)
        lista_madre = Cruce.creoListaDeBits(abeja_madre)

        pivote_random = randint(0, len(lista_padre)-1)
        
        binario_hijo_1 = lista_padre[:pivote_random]+lista_madre[pivote_random:]
        binario_hijo_2 = lista_madre[:pivote_random]+lista_padre[pivote_random:]

        print("Padre %s" % lista_padre)
        print("Madre %s" % lista_madre)
        print("Pivote %s" % pivote_random)
        print("Hijo1 %s" % binario_hijo_1)
        print("Hijo2 %s" % binario_hijo_2)

        a=[Cruce.transformarEnAbeja(binario_hijo_1),Cruce.transformarEnAbeja(binario_hijo_2)]
        for abeja in a:
            abeja.madre=abeja_madre
            abeja.padre=abeja_padre
        return a

    def transformarEnAbeja(genoma):
        codGeneticoDirFav=genoma[:16]
        codGeneticoTolerancia=genoma[16:24]
        codGeneticoColorFav=genoma[24:48]
        codGeneticoAnguloDesviacion=genoma[48:64]
        codGeneticoDistanciaMaxima=genoma[64:72]
        codGenRec=genoma[72:]
        a=Abeja(
            int(codGeneticoDirFav,2)/0xffff*2*pi,
            (int(codGeneticoColorFav[:8],2), int(codGeneticoColorFav[8:16],2), int(codGeneticoColorFav[16:],2)),
            int(codGeneticoTolerancia,2)/0xff,
            int(codGeneticoAnguloDesviacion, 2)/0xffff*2*pi,
            int(codGeneticoDistanciaMaxima, 2)/0xff*limite,
            int(codGenRec,2)%3)

        return a

def crearFlor():
    return Flor(
        colores_rgb[randint(0, largo_colores_rgb)],
        randint(0, limite),
        uniform(0, 1)*2*pi
    )

def creoAbeja():
    direccion_random_indice = randint(0, largo_angulos_posibles)
    direccion_random = angulos_direcciones[direccion_random_indice]
    color_random_indice = randint(0, largo_colores_rgb)
    color_random = colores_rgb[color_random_indice]

    direccion_favorita = direccion_random
    color_favorito = color_random
    tolerancia_al_color = uniform(0, 1)
    angulo_desviacion = random()*pi/6
    distancia_maxima = randint(0, 71)
    r=randint(0,3)

    return Abeja(direccion_favorita, color_favorito, tolerancia_al_color, angulo_desviacion, distancia_maxima,r)


def XYfromPolar(oriX,oriY,r,a):
    """
    Desde el punto de origen (oriX,oriY), se calcula un punto a distancia R y a angulo A
    """
    return (int(oriX+sin(a)*r),  int(oriY+cos(a)*r))

def randompos(r,fav,mistake):
    distanciaDesdeElCentro=random()*r
    angulo=(fav-mistake)+random()*(2*mistake)
    return XYfromPolar(CX,CY,distanciaDesdeElCentro,angulo)

def distancia(p1,p2):
    return pow(pow(p1[0]-p2[0],2)+pow(p1[1]-p2[1],2),1/2)

def frange(inicio, fin, step):
    return [inicio + i*step for i in range(int((fin-inicio)/step))]

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
    suma = 0
    for abeja in abejas:
        suma += pow(pow(calificacion(abeja.padre)-calificacion(abeja), 2) +
                    pow(calificacion(abeja.madre)-calificacion(abeja), 2), 0.5)
    return suma/CANT_ABEJAS > MARGEN_EVOLUCION


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
            nuevasAbejas+=Cruce.cruzarAbejas(abejaPadre,abejaMadre)
          
        return nuevasAbejas

    cacheNormalizedFitness={}
    cacheCalif={}
    #Aquí comienza lo bueno#
    def getFlor(punto):
        nonlocal flores
        for flor in flores:
            x,y=XYfromPolar(CX,CY,flor.radio,flor.angulo)
            if int(x)==punto[0] and int(y)==punto[1]:
                return flor
        return None
    abejas=[
        creoAbeja()
        for _ in range(CANT_ABEJAS)
    ]
    flores=[
        crearFlor()
        for _ in range(CANT_FLORES)
    ]
    #imprimirFlores(flores)
    for g in range(CANT_GENERACIONES):
        print("Generacion #%s" % g)
        pintarFlores(flores)
        sumCalifGener=0
        totalGener=[]
        #nuevas_abejas = []
        for abeja in abejas:
            recorrido=abeja.calcularRecorrido()
            puntoAnterior=(CX,CY)
            distanciaRecorrida=0
            for punto in recorrido:
                #pintarRecorrido(abeja,punto)
                flor=getFlor(punto)
                if flor!=None:#Simular Interaccion entre la abeja y la flor
                    flor.muestras+=abeja.polen
                    abeja.polen.append(flor)
                    abeja.cantFlores+=1
                    distanciaRecorrida+=distancia(puntoAnterior,punto)#¡Duda!#
                puntoAnterior=punto
            cacheCalif[abeja]=K*distanciaRecorrida/Q*abeja.cantFlores #Calificación bruta
            sumCalifGener+=cacheCalif[abeja]
            totalGener.append(sumCalifGener)
            #nuevas_abejas.append(abeja)

        
        #for abeja in nuevas_abejas:
        for abeja in abejas:
            if sumCalifGener != 0:
                cacheNormalizedFitness[abeja]=calificacion(abeja)/sumCalifGener #Calificacion relativa
            else:
                cacheNormalizedFitness[abeja]=1

        #baseDeDatos.append(nuevas_abejas)
        baseDeDatos.append(abejas)

        #abejas = reproducirAbejas(nuevas_abejas)
        abejas = reproducirAbejas(abejas)

        nuevasFlores=[
            flor.reproducir()
            for flor in flores
        ]
        
        #imprimirAbejas(abejas)
        #imprimirFlores(nuevasFlores)   

        if probabilidadAdaptabilidad(totalGener) == True:
            break

        despintarViejasFlores()
        flores=nuevasFlores

    despintarViejasFlores()
    #Escoger que generacion y que abeja quiere mostrar su camino.
    generacion_escogidaStr = input("Generacion: ")
    abeja_escogidaStr = input("Abeja: ")
    generacion_escogida = int(generacion_escogidaStr)
    abeja_escogida = int(abeja_escogidaStr)
    abejas = baseDeDatos[generacion_escogida]

    imprimirAbeja(abejas[abeja_escogida])
    imprimirFlores(abejas[abeja_escogida].polen)
    #pintarFlores(abejas[abeja_escogida].polen)


def probabilidadAdaptabilidad(totalGener):
    lista = []

    if len(totalGener) < 5:
        for i in range(len(totalGener)-1):
            lista.append(totalGener[i])
        devEstandarAnterior = statistics.stdev(lista)
    else:
        for i in range(len(totalGener)-4, len(totalGener)-1):
            lista.append(totalGener[i])
        devEstandarAnterior = statistics.stdev(lista)

    lista = []

    if len(totalGener) < 5:
        for i in range(len(totalGener)):
            lista.append(totalGener[i])
        devEstandar = statistics.stdev(lista)
    else:
        for i in range(len(totalGener)-4, len(totalGener)):
            lista.append(totalGener[i])
        devEstandar = statistics.stdev(lista)

    promedio = abs(devEstandarAnterior-devEstandar)

#    if promedio < 1.5 and promedio > 0.1:
    if promedio < 2:
        print("devEstandarAnterior %s" % devEstandarAnterior)
        print("devEstandar %s" % devEstandar)
        return True
    else:
        return False

def pintarFlores(flores):
    global px
    for flor in flores:
        x,y=XYfromPolar(CX,CY,flor.radio,flor.angulo)
        x=abs(x)
        y=abs(y)
        print("Flor de color %s y posicion (%s,%s)" % (flor.color,x,y))
        if x<800 and x>=0 and y<800 and y>=0:
            px[x][y]=flor.color

def despintarViejasFlores():
    screen.fill((0, 0, 0))

def imprimirFlores(flor):
    for i in range(len(flor)):
        print("Variables de flor: \n Color: %s \n Radio: %s \n Angulo: %s \n Muestras: %s \n" % (
            flor[i].color, flor[i].radio, flor[i].angulo, flor[i].muestras))

def imprimirAbejas(abeja_hijo):
    for j in range(len(abeja_hijo)):
        print("Variables hijo: \n Direccion favorita: %s \n Color favorito: %s \n Tolerancia al color: %s \n Angulo desviacion: %s \n Distancia maxima: %s" % (
            abeja_hijo[j].direccion_favorita, abeja_hijo[j].color_favorito, abeja_hijo[j].tolerancia_al_color, abeja_hijo[j].angulo_desviacion, abeja_hijo[j].distancia_maxima))

def imprimirAbeja(abeja_hijo):
    print("Variables hijo: \n Direccion favorita: %s \n Color favorito: %s \n Tolerancia al color: %s \n Angulo desviacion: %s \n Distancia maxima: %s" % (
        abeja_hijo.direccion_favorita, abeja_hijo.color_favorito, abeja_hijo.tolerancia_al_color, abeja_hijo.angulo_desviacion, abeja_hijo.distancia_maxima))



"""
Setup
"""
baseDeDatos = []

anchoStr = input("Cuanto de Ancho y largo gusta su interfaz??? Porfavor digite un numero par >>> ")
ancho = int(anchoStr)
alto = ancho
mitadAncho = int(ancho/2)
limite =  round(sqrt(pow(mitadAncho, 2) + pow(mitadAncho, 2)))

PARAM_SIZE_1 = 16
PARAM_SIZE_2 = 8

CX = mitadAncho
CY = mitadAncho

CANT_GENERACIONES = 200
CANT_ABEJAS = 20
CANT_FLORES = 50
Q = 1
K = 1
MARGEN_EVOLUCION = 2

#oeste,este,norte,sur
angulos_direcciones = [0, pi*3/4, pi/2, pi/4, pi, -pi/4, -pi/2, -pi*3/4]
largo_angulos_posibles = len(angulos_direcciones)-1

#                  rojo,    naranja         amarillo       verde        celeste        blanco         morado        fuchsia
colores_rgb = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (255, 255, 255), (127, 0, 255), (255, 0, 255)]
largo_colores_rgb = len(colores_rgb)-1

pygame.init()
screen = pygame.display.set_mode((ancho, alto))
screen.fill((0, 0, 0))
px = pygame.PixelArray(screen)
pygame.display.set_caption("La colmena")
clock = pygame.time.Clock()
seed()

#Colmena
px[mitadAncho][mitadAncho] = (255, 0, 0)

t = threading.Thread(target=jardin)
t.setDaemon(True)
t.start()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            donde = True
        if event.type == pygame.KEYDOWN:
            pass
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
