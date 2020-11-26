import math 
#print(int('01010', 2))    

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

#oeste,este,norte,sur
dicciones = [math.pi, 0, math.pi/2, -math.pi/2]

class Abeja:
    def __init__(self,padre=None,madre=None):
        if padre==None or madre==None:
            desviacionMaxima=random
            direccionFavorita=random(ra)
            colorFavorito=(0,0,255)
            toleranciaAlColor=0
            anguloDesviacion=math.pi
            recorrido=[(200,200),2] #2=random
            nectar_recolectado=[]
            self.desviacionMaxima=desviacionMaxima
            self.direccionFavorita=direccionFavorita
            self.colorFavorito=colorFavorito
            self.toleranciaAlColor=toleranciaAlColor
            self.anguloDesviacion=anguloDesviacion
            self.recorrido=recorrido
            self.nectar_recolectado=nectar_recolectado
        else:
            reproducir a papá y mamá XD
    def cruce(self,otraAbeja):
        
    def simularRecorrido(self,)

class Flor:
    def __init__(self,pRadio,pAngulo,pMuestras):
        self.radio = pRadio
        self.anagulo = pAngulo
        self.muestras = pMuestras

## Papa
papa=Abeja(None,None)

## MAMA
mama=Abeja(None,None)

## 2 Hijos

Abeja(papa,mama)
Abeja(papa,mama)
