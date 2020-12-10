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
    lista_madre = Cruce.creoListaDeBits2(abeja_madre)

    lista_de_bits_padre = lista_padre[0]
    lista_de_bits_madre = lista_madre[0]

    print("Padre: %s" % lista_de_bits_padre)
    print("Madre: %s" % lista_de_bits_madre)

    posicion_punto_direccion_padre = lista_padre[1]
    posicion_punto_direccion_madre = lista_madre[1]

    posicion_punto_desviacion_padre = lista_padre[2]
    posicion_punto_desviacion_madre = lista_madre[2]

    lista_largo_variables_padre_por_parametro = lista_padre[3]
    lista_largo_variables_madre_por_parametro = lista_madre[3]

    lista_largo_variables_padre = lista_padre[4]
    lista_largo_variables_madre = lista_madre[4]

    largo1 = len(lista_de_bits_padre)
    largo2 = len(lista_de_bits_madre)

    if largo1 <= largo2:
        rango_random_pivote = largo1
    else:
        rango_random_pivote = largo2

    pivote_random = random.randint(0, rango_random_pivote-1)
    print("Pivote: %s" % pivote_random)

    parte_del_padre = lista_de_bits_padre[:pivote_random]
    parte_de_la_madre = lista_de_bits_madre[pivote_random:]

    result = []
    binario_hijo_1 = ""
    binario_hijo_2 = ""
    lista_largo_variables_hijo_1 = []
    lista_largo_variables_hijo_2 = []
    punto_direccion_y_desviacion_1 = []
    punto_direccion_y_desviacion_2 = []

    if pivote_random == 0:
        binario_hijo_1 += lista_de_bits_padre
        lista_largo_variables_hijo_1 = lista_largo_variables_padre_por_parametro
        punto_direccion_y_desviacion_1.append(posicion_punto_direccion_padre)
        punto_direccion_y_desviacion_1.append(posicion_punto_desviacion_padre)
        binario_hijo_2 += lista_de_bits_madre
        lista_largo_variables_hijo_2 = lista_largo_variables_madre_por_parametro
        punto_direccion_y_desviacion_2.append(posicion_punto_direccion_madre)
        punto_direccion_y_desviacion_2.append(posicion_punto_desviacion_madre)
    elif pivote_random == rango_random_pivote-1:
        binario_hijo_1 += lista_de_bits_madre
        lista_largo_variables_hijo_2 = lista_largo_variables_madre_por_parametro
        punto_direccion_y_desviacion_2.append(posicion_punto_direccion_madre)
        punto_direccion_y_desviacion_2.append(posicion_punto_desviacion_madre)
        binario_hijo_2 += lista_de_bits_padre
        lista_largo_variables_hijo_1 = lista_largo_variables_padre_por_parametro
        punto_direccion_y_desviacion_1.append(posicion_punto_direccion_padre)
        punto_direccion_y_desviacion_1.append(posicion_punto_desviacion_padre)
    else:
        flag = False
        for i in range(len(lista_largo_variables_padre)):
            if i == 0:
                pass
            if pivote_random >= lista_largo_variables_padre[i-1] and pivote_random <= lista_largo_variables_padre[i] and flag == False:
                flag = True
                binario_hijo_1 += parte_del_padre
                binario_hijo_1 += parte_de_la_madre
                lista_largo_variables_hijo_1 += lista_largo_variables_padre_por_parametro[:i]
                lista_largo_variables_hijo_1 += lista_largo_variables_madre_por_parametro[i:]
                punto_direccion_y_desviacion_1.append(posicion_punto_direccion_padre)
                punto_direccion_y_desviacion_1.append(posicion_punto_desviacion_madre)
                
                binario_hijo_2 += parte_de_la_madre
                binario_hijo_2 += parte_del_padre
                lista_largo_variables_hijo_2 += lista_largo_variables_madre_por_parametro[:i]
                lista_largo_variables_hijo_2 += lista_largo_variables_padre_por_parametro[i:]
                punto_direccion_y_desviacion_2.append(posicion_punto_direccion_madre)
                punto_direccion_y_desviacion_2.append(posicion_punto_desviacion_padre)

    result.append(binario_hijo_1)
    result.append(lista_largo_variables_hijo_1)
    result.append(punto_direccion_y_desviacion_1)
    result.append(binario_hijo_2)
    result.append(lista_largo_variables_hijo_2)
    result.append(punto_direccion_y_desviacion_2)

    resultado_hijo1 = resultadoHijo(binario_hijo_1, lista_largo_variables_hijo_1)
    resultado_hijo2 = resultadoHijo(binario_hijo_2, lista_largo_variables_hijo_2)

    #Pongo el punto de desviacion para hijo 1
    resultado_hijo1[0] = ponerPuntoPosicion(resultado_hijo1[0], punto_direccion_y_desviacion_1[0])
    #Pongo el punto de angulo para hijo 1
    resultado_hijo1[3] = ponerPuntoPosicion(resultado_hijo1[3], punto_direccion_y_desviacion_1[1])

    #Pongo el punto de desviacion para hijo 2
    resultado_hijo2[0] = ponerPuntoPosicion(resultado_hijo2[0], punto_direccion_y_desviacion_2[0])
    #Pongo el punto de angulo para hijo 2
    resultado_hijo2[3] = ponerPuntoPosicion(resultado_hijo2[3], punto_direccion_y_desviacion_2[1])

    resultado_enteros_hijo1 = obtengoNumerosEnteros(resultado_hijo1)
    resultado_enteros_hijo2 = obtengoNumerosEnteros(resultado_hijo2)

    resultado = []
    resultado.append(resultado_enteros_hijo1)
    resultado.append(resultado_enteros_hijo2)

    print("hijo1 %s" % binario_hijo_1)
    print("Punto de distancia y desviacion: %s" % punto_direccion_y_desviacion_1)
    print("Binario variables Hijo 1: %s" % resultado_hijo1)

    print("hijo2 %s" % binario_hijo_2)
    print("Punto de distancia y desviacion: %s" % punto_direccion_y_desviacion_2)
    print("Binario variables Hijo 2: %s" % resultado_hijo2)

    return resultado


def ponerPuntoPosicion(pLista, pNum):
    lista = pLista[:pNum]+"."+pLista[pNum:]
    return lista

def obtengoNumerosEnteros(pLista):
    lista = []

    for i in range(len(pLista)):
        if i == 0:
            p1, p2 = pLista[i].split(".")
            r1 = int(p1, 2)
            r2 = int(p2, 2)
            rr = str(r1)+"."+str(r2)
            lista.append(float(rr))
        elif i == 3:
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
    conter = 1
    nueva_variable = ""
    tamano = 0
    largo_binario = len(binario_hijo_1)
    tamano_total = sumaTotal(lista_largo_variables_hijo_1)
        
    if tamano_total > largo_binario:
        tamano = tamano_total-largo_binario
        lista_largo_variables_hijo_1[len(lista_largo_variables_hijo_1)-1]-=tamano
    elif tamano_total < largo_binario:
        tamano = largo_binario-tamano_total
        lista_largo_variables_hijo_1[len(lista_largo_variables_hijo_1)-1] += tamano

    for i in range(largo_binario):
        variable = lista_largo_variables_hijo_1[contador]
        if i == 0:
            nueva_variable += binario_hijo_1[i]
            conter += 1
        elif conter == variable:
            contador += 1
            resultado_hijo1.append(nueva_variable)
            nueva_variable = ""
            conter = 1
        else:
            nueva_variable += binario_hijo_1[i]
            conter += 1

    return resultado_hijo1


#Inicializo abejas Padres
abeja1 = AbejaIndividuo()
abeja2 = AbejaIndividuo()

abeja_hijo = prueba1(abeja1, abeja2)

for j in range(len(abeja_hijo)):
    print("Variables hijos: %s" % abeja_hijo[j])

print(Cruce.float_bin(0.3453,20))


#>> > bin(3453)
#'0b110101111101'


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
