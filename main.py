import pygame
from pygame.locals import *
import threading
import statistics
from math import pi,sin,cos,sqrt, pow
from random import random, choices,randint,uniform,seed,choice

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
        self.distanciaRecorrida=0
        self.madre=None
        self.padre=None
    def __str__(self):
        return "Abeja( DirecFav="+self.getDireccionFavoritaStr()+", MaxDesv="+str(self.angulo_desviacion)+", MaxDist="+str(self.distancia_maxima)+", ColorFav="+strColor(self.color_favorito)+" )"
    def getDireccionFavoritaStr(self):
        return str(self.direccion_favorita)
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
    def toleraColorFeo(self):
        return random() < self.tolerancia_al_color
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
    def getCodigoGenetico(self):
        listaGenesBits = ''

        direccion_favorita = self.direccion_favorita
        color_favorito = self.color_favorito
        tolerancia_al_color = self.tolerancia_al_color
        angulo_desviacion = self.angulo_desviacion
        distancia_maxima = self.distancia_maxima

        codGeneticoDirFav = int(0xffff*direccion_favorita/(2*pi))
        codGeneticoTolerancia = int(0xff*tolerancia_al_color)
        codGeneticoAnguloDesviacion = int(0xffff*angulo_desviacion/(2*pi))
        codGeneticoDistanciaMaxima = int(0xff*distancia_maxima/70.71)
        codGenRec=int(0xff*self.recorrido/3)

        listaGenesBits += bin(codGeneticoDirFav).replace("-","")[2:].zfill(PARAM_SIZE_1)
        listaGenesBits += bin(codGeneticoTolerancia)[2:].zfill(PARAM_SIZE_2)
        listaGenesBits += f'{bin(color_favorito[0])[2:].zfill(PARAM_SIZE_2)}{bin(color_favorito[1])[2:].zfill(PARAM_SIZE_2)}{bin(color_favorito[2])[2:].zfill(PARAM_SIZE_2)}'
        listaGenesBits += bin(codGeneticoAnguloDesviacion)[2:].zfill(PARAM_SIZE_1)
        listaGenesBits += bin(codGeneticoDistanciaMaxima)[2:].zfill(PARAM_SIZE_2)
        listaGenesBits += bin(codGenRec)[2:].zfill(PARAM_SIZE_2)
        return listaGenesBits
    def cruzarAbejas(self, abeja_madre):
        lista_padre = self.getCodigoGenetico()
        lista_madre = abeja_madre.getCodigoGenetico()
        pivote_random = randint(0, len(lista_padre)-1)
        genoma_hijo_1 = lista_padre[:pivote_random]+lista_madre[pivote_random:]
        genoma_hijo_2 = lista_madre[:pivote_random]+lista_padre[pivote_random:]

        a=[Abeja.transformarEnAbeja(genoma_hijo_1),Abeja.transformarEnAbeja(genoma_hijo_2)]
        for abeja in a:
            abeja.madre=abeja_madre
            abeja.padre=self
        print('Padre: '+lista_padre,'Madre: '+lista_madre,f'Pivote: {pivote_random}',
            'Hijo1: '+genoma_hijo_1[:pivote_random]+' '+genoma_hijo_1[pivote_random:],
            'Hijo2: '+genoma_hijo_2[:pivote_random]+' '+genoma_hijo_2[pivote_random:],sep='\n' )
        return a

    def transformarEnAbeja(genoma):
        codGeneticoColorFav=genoma[24:48]
        a=Abeja(
            int(genoma[:16],2)/0xffff*2*pi,
            (int(codGeneticoColorFav[:8],2), int(codGeneticoColorFav[8:16],2), int(codGeneticoColorFav[16:],2)),
            int(genoma[16:24],2)/0xff,
            int(genoma[48:64], 2)/0xffff*2*pi,
            int(genoma[64:72], 2)/0xff*70.71,
            int(genoma[72:],2)*3/0xff)
        return a
class Flor:
    def __init__(self,pColor, pRadio, pAngulo):
        self.color = pColor
        self.radio = pRadio
        self.angulo = pAngulo
        self.muestras = []#pMuestras
    def __str__(self):
        return "Flor( Color="+strColor(self.color)+", Posicion="+XYfromPolar(CX,CY,self.radio,self.angulo)[2]+" )"
    def getMuestra(self):
        return self.muestras

    def creoListaDeBitsFlor(self):
        return self.getCodigoGenetico()
    def getCodigoGenetico(self):
        listaGenesBits = ''

        codGeneticoRadio = int(0xff*self.radio)
        codGeneticoAngulo = int(0xffff*self.angulo/(2*pi))

        listaGenesBits += f'{bin(self.color[0]).replace("-", "")[2:].zfill(PARAM_SIZE_2)}{bin(self.color[1])[2:].zfill(PARAM_SIZE_2)}{bin(self.color[2])[2:].zfill(PARAM_SIZE_2)}'
        listaGenesBits += bin(codGeneticoRadio)[2:].zfill(PARAM_SIZE_2)
        listaGenesBits += bin(codGeneticoAngulo)[2:].zfill(PARAM_SIZE_1)

        return listaGenesBits

    def reproducir(self):
        if len(self.muestras)==0:
            return crearFlor()
        madre=choice(self.muestras)
        return Flor.transformarEnFlor(self, Flor.cruzarFlores(self,madre))

    def cruzarFlores(self, flor_madre):
        lista_padre = self.getCodigoGenetico()
        lista_madre = Flor.getCodigoGenetico(flor_madre)

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

def crearFlor():
    limite =  int(sqrt(pow(CX, 2) + pow(CY, 2)))
    return Flor(
        choice(COLORES_FAVORITOS),
        randint(0, 71),
        uniform(0, 1)*2*pi
    )
def creoAbeja():
    return Abeja(
        choice(DIRECCIONES_FAVORITAS), 
        choice(COLORES_FAVORITOS), 
        uniform(0, 1), 
        random()*pi/6, 
        randint(0, 71),
        randint(0,2))
def frange(inicio,fin,step):
    return [inicio + i*step for i in range(int((fin-inicio)/step))]
def XYfromPolar(oriX,oriY,r,a):
    """
    Desde el punto de origen (oriX,oriY), se calcula un punto a distancia R y a angulo A
    """
    x=int(oriX+sin(a)*r)
    y=int(oriY+cos(a)*r)
    return (x, y, f'( {x}, {y} )')
def randompos(r,fav,mistake):
    distanciaDesdeElCentro=random()*r
    angulo=(fav-mistake)+random()*(2*mistake)
    return XYfromPolar(CX,CY,distanciaDesdeElCentro,angulo)

def distancia(p1,p2):
    return pow(pow(p1[0]-p2[0],2)+pow(p1[1]-p2[1],2),1/2)
def mismoColor(c1,c2):
    return pow(pow(c1[0]-c2[0],2)+pow(c1[1]-c2[1],2)+pow(c1[2]-c2[2],2),1/2)<C
def strLista(lista):
    if len(lista)>7:return f"[ len = {len(lista)} ]"
    r=""
    for element in lista:
        r+="\t"+str(element)+"\n"
    return r
def imprimirFlor(flor):
    for i in range(len(flor)):
        print("Variables de flor: \n Color: %s \n Radio: %s \n Angulo: %s \n Muestras: %s \n" % (flor[i].color, flor[i].radio, flor[i].angulo, flor[i].muestras))
def jardin():
    """
    Esta función simula el comportamiento el jardín atravez de las
    generaciones de abejas y el respectivo comportamiento de las
    flores.
    """    
    def getFlor(punto,flores):
        for flor in flores:
            if distancia(XYfromPolar(CX,CY,flor.radio,flor.angulo),punto)<R:
                flores.remove(flor)
                return flor
        return None
    def calificacionBruta(abeja):
        """
        Esta función busca calificar cada abeja pero recordando si ya
        se calificó una abeja con estos resultados de recorrido
    Guarda el historial de todas las generaciones para consultarlo después.
        @param abeja: la abeja de la que se desea saber la calificacion
        @return: la calificación de esta abeja
        """
        nonlocal cacheCalif
        if abeja not in cacheCalif.keys():
            if abeja.cantFlores==0 or abeja.distanciaRecorrida==0:cacheCalif[abeja]=0
            else:
                cacheCalif[abeja]=(Q*abeja.cantFlores)/(K*abeja.distanciaRecorrida) 
        return cacheCalif[abeja]
    def calcularCalificacionRelativa(abejas,sumCalifGener):
        for abeja in abejas:
            cacheNormalizedFitness[abeja]=calificacionBruta(abeja)/sumCalifGener
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
        for _ in range(CANT_ABEJAS//2):
            abejaPadre,abejaMadre=choices(
                abejas,
                weights=pesos,
                k=2)
            nuevasAbejas+=abejaPadre.cruzarAbejas(abejaMadre)
        assert len(nuevasAbejas)==CANT_ABEJAS
        return nuevasAbejas

    cacheNormalizedFitness={}
    cacheCalif={}
    abejas=[
        creoAbeja()
        for _ in range(CANT_ABEJAS)
    ]
    flores=[
        crearFlor()
        for _ in range(CANT_FLORES)
    ]
    for g in range(CANT_GENERACIONES):
        print("Generación #"+str(g))
        pintarFlores(flores)
        sumCalifGener=0
        totalGener=[]
        #nuevas_abejas = []
        for abeja in abejas:
            recorrido=abeja.calcularRecorrido()
            tmpFlores=list(flores)
            puntoAnterior=(CX,CY)
            for punto in recorrido:
                flor=getFlor(punto,tmpFlores)
                if flor!=None and (mismoColor(flor.color,abeja.color_favorito) or abeja.toleraColorFeo()):
                    print("La abeja "+str(abeja)+" se ha encontrado con la flor "+str(flor))
                    flor.muestras+=abeja.polen
                    abeja.polen.append(flor)
                    abeja.cantFlores+=1
                    
                    print(f"Nuevo polen de la abeja: \n{strLista(abeja.polen)}")
                    print(f"Nuevas muestras de la flor: \n{strLista([str(muestra)for muestra in flor.muestras])}")
                    print(f"Cantidad flores visitadas por esta abeja: {str(abeja.cantFlores)}")
                abeja.distanciaRecorrida+=distancia(puntoAnterior,punto)
                puntoAnterior=punto
            sumCalifGener+=calificacionBruta(abeja)
        calcularCalificacionRelativa(abejas,sumCalifGener)
        abejas=reproducirAbejas(abejas)
        totalGener.append(sumCalifGener)
        nuevasFlores=[
            flor.reproducir()
            for flor in flores
        ]
        
        if probabilidadAdaptabilidad(totalGener) == True:
            break
        flores=nuevasFlores
        despintarViejasFlores()

def PDU(abejas):
    generacion_escogidaStr = input("Generacion: ")
    abeja_escogidaStr = input("Abeja: ")
    generacion_escogida = int(generacion_escogidaStr)
    abeja_escogida = int(abeja_escogidaStr)
    abejas = baseDeDatos[generacion_escogida]
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
"""
Setup
"""
#GENETIC ALGORITHM PARAMETERS
#                  rojo,    naranja         amarillo       verde        celeste        azul         morado        fuchsia
COLORES_FAVORITOS = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (127, 0, 255), (255, 0, 255)]
DIRECCIONES_FAVORITAS = [i/4*pi for i in range(8)]
CANT_GENERACIONES=200
CANT_ABEJAS=20
CANT_FLORES=50
Q=1
K=1
R=5 #Distancia a la que se acepta que la abeja llegó a la flor
C=10 #Distancia a la que un color es igual a otro
PROB_MUTACION=0.0015
CX=50
CY=50
#PYGAME PARAMETERS

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

pygame.init()
screen = pygame.display.set_mode((ancho, alto))
screen.fill((0, 0, 0))
px = pygame.PixelArray(screen)
pygame.display.set_caption("La colmena")
clock = pygame.time.Clock()
seed()
def strColor(color):
    return f"({str(color[0]).zfill(3)},{str(color[1]).zfill(3)},{str(color[2]).zfill(3)})"
def pintarFlores(flores):
    global px
    for flor in flores:
        x,y,name=XYfromPolar(CX,CY,flor.radio,flor.angulo)
        print("Pintando flor de color "+strColor(flor.color)+" en el punto: "+name)
        if x<100 and x>=0 and y<100 and y>=0:
            px[x][y]=flor.color
def despintarViejasFlores():
    screen.fill((0, 0, 0))
    px[CX][CY] = (255, 0, 0)
#Colmena
px[CX][CY] = (255, 0, 0)

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
