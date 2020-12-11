from math import pi, sin, cos
import random
from abc import abstractmethod
from Cruce import Cruce

CANT_ABEJAS = 20
CANT_FLORES = 50
MARGEN_EVOLUCION = 2

#oeste,este,norte,sur
angulos_direcciones = [0, pi*3/4, pi/2, pi/4, pi, -pi/4, -pi/2, -pi*3/4]
largo_angulos_posibles = len(angulos_direcciones)-1

#                  rojo,    naranja         amarillo       verde        celeste        azul         morado        fuchsia
colores_rgb = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (127, 0, 255), (255, 0, 255)]
largo_colores_rgb = len(colores_rgb)-1

"""
Generic Logic

Tipo de recorrido:
    1-) Random.
    2-) ...
    3-) ...
"""
class AbejaIndividuo:    
    def __init__(self):
        direccion_random_indice = random.randint(0, largo_angulos_posibles)
        direccion_random = angulos_direcciones[direccion_random_indice]
        color_random_indice = random.randint(0, largo_colores_rgb)
        color_random = colores_rgb[color_random_indice]

        direccion_favorita = direccion_random
        color_favorito = color_random
        tolerancia_al_color = random.randint(0,1)
        angulo_desviacion = random.randint(30, 40)
        distancia_maxima = random.randint(0, 71)
   
        self.direccion_favorita = direccion_favorita
        self.color_favorito = color_favorito
        self.tolerancia_al_color = tolerancia_al_color
        self.angulo_desviacion = angulo_desviacion
        self.distancia_maxima = distancia_maxima
    """
    def __init__(self, padre=None, madre=None):
        direccion_random_indice = random.randint(0, largo_angulos_posibles)
        direccion_random = angulos_direcciones[direccion_random_indice]
        color_random_indice = random.randint(0, largo_colores_rgb)
        color_random = colores_rgb[color_random_indice]

        if padre == None or madre == None:
            #desviacionMaxima = random.randit(30, 40)
            direccion_favorita = direccion_random
            color_favorito = color_random
            tolerancia_al_color = random.randint(0, 1)
            angulo_desviacion = random.randint(30, 40)
            distancia_maxima = random.randint(0, 71)
            #recorrido_de_flores = []
            #nectar_recolectado = []

            #self.desviacionMaxima = desviacionMaxima
            self.direccion_favorita = direccion_favorita
            self.color_favorito = color_favorito
            self.tolerancia_al_color = tolerancia_al_color
            self.angulo_desviacion = angulo_desviacion
            self.distancia_maxima = distancia_maxima
            #self.recorrido = recorrido_de_flores
            #self.nectar_recolectado = nectar_recolectado

        else:
            return 0
            #reproducir a papá y mamá XD
    """
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


"""
Setup
"""
ancho = 100
alto = 100



"""
Prueba1 pasa todos los parametros de padre y madre a binario para hacer el cruce.
Agarra la primera mitad del padre y la segunda mitad de la madre.
"""

def prueba1(abeja_padre, abeja_madre):
    
    lista_padre = Cruce.creoListaDeBits(abeja_padre)
    lista_madre = Cruce.creoListaDeBits(abeja_madre)

    print("Padre: %s" % lista_padre)
    print("Madre: %s" % lista_madre)

    largo1 = len(lista_padre)
    largo2 = len(lista_madre)

    print("largo1 %s" % largo1)
    print("largo2 %s" % largo2)

    if largo1 <= largo2:
        rango_random_pivote = largo1
    else:
        rango_random_pivote = largo2

    pivote_random = random.randint(0, rango_random_pivote-1)
    print("Pivote: %s" % pivote_random)

    parte_del_padre = lista_padre[:pivote_random]
    parte_de_la_madre = lista_madre[pivote_random:]

    print("parte_del_padre %s" % parte_del_padre)
    print("parte_de_la_madre %s" % parte_de_la_madre)

    result = []
    binario_hijo_1 = ""
    binario_hijo_2 = ""

    binario_hijo_1 += parte_del_padre
    binario_hijo_1 += parte_de_la_madre
    
    binario_hijo_2 += parte_de_la_madre
    binario_hijo_2 += parte_del_padre

    result.append(binario_hijo_1)
    result.append(binario_hijo_2)

    return result


def ponerPuntoPosicion(pLista, pNum):
    lista = pLista[:pNum]+"."+pLista[pNum:]
    return lista

def obtengoNumerosEnteros(pLista):
    lista = []

    for i in range(len(pLista)):
        if i == 0 or i == 2 or i == 3:
            p1, p2 = pLista[i].split(".")
            r1 = int(p1, 2)
            r2 = int(p2, 2)
            rr = str(r1)+"."+str(r2)
            lista.append(float(rr))
        else:
            lista.append(int(pLista[i], 2))

    return lista

def sumaTotal(lista):
    result = 0
    for i in range(len(lista)):
        result += lista[i]

    return result

def resultadoHijo(binario_hijo_1, lista_largo_variables_hijo_1):
    resultado_hijo1 = []
    contador = 0
    conter = 0
    nueva_variable = ""
    tamano = 0
    largo_binario = len(binario_hijo_1)
    tamano_total = sumaTotal(lista_largo_variables_hijo_1)
    
    print("largo binario hijo 1: %s" % largo_binario)
    print("tamano total hijo 1: %s" % tamano_total)

    if tamano_total > largo_binario:
        tamano = tamano_total-largo_binario
        lista_largo_variables_hijo_1[len(lista_largo_variables_hijo_1)-1] -= tamano + 1
    elif tamano_total < largo_binario:
        tamano = largo_binario-tamano_total
        lista_largo_variables_hijo_1[len(lista_largo_variables_hijo_1)-1] += tamano - 1

    #hijo1=111010101010101111111111
    #largo_binario=25
    #4...1+9+6=23
    #nueva_variable="1110"
    #lista_largo_variables_hijo_1=[4,7,1,9,6]
    #lista_largo_variables_hijo_1[contador] = 4
    #resultado_hijo1=["1110","1010010","1","10101010101","1010101"]
    for i in range(largo_binario):
        variable = lista_largo_variables_hijo_1[contador]
        if i == 0:
            nueva_variable += binario_hijo_1[i]
            conter += 1
        elif conter == variable:
            contador += 1
            resultado_hijo1.append(nueva_variable)
            nueva_variable = binario_hijo_1[i]
            conter = 1
        else:
            nueva_variable += binario_hijo_1[i]
            conter += 1

            if conter == variable and i == largo_binario-1:
                resultado_hijo1.append(nueva_variable)

    return resultado_hijo1


#Inicializo abejas Padres
abeja1 = AbejaIndividuo()
abeja2 = AbejaIndividuo()

abeja_hijo = prueba1(abeja1, abeja2)

for j in range(len(abeja_hijo)):
    if j == 0:
        print("Variables hijo1: %s" % abeja_hijo[j])
        print("largo: %s" % len(abeja_hijo[j]))
    else:
        print("Variables hijo2: %s" % abeja_hijo[j])
        print("largo: %s" % len(abeja_hijo[j]))


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
